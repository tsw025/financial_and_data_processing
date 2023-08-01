from pydantic_core._pydantic_core import ValidationError
from fastapi import Depends

from assignment.trader.exceptions import TraderServiceValidationException
from assignment.trader.models import TraderRequestErrors
from assignment.trader.repository import TraderRequestErrorsRepository
from assignment.trader import schema as trader_schema

from queue import Queue


class SingletonQueue:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonQueue, cls).__new__(cls)
            cls._instance.queue = Queue()
        return cls._instance

    def put(self, item):
        self.queue.put(item)

    def get(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()

    def qsize(self):
        return self.queue.qsize()

    def task_done(self):
        return self.queue.task_done()

    def join(self):
        return self.queue.join()


class DataAnalyserQueueService:

    def __init__(self,
                 queue: Queue = Depends(SingletonQueue),
                 trader_req_errors_repo: TraderRequestErrorsRepository = Depends(),
                 ):
        self.trader_req_errors_repo = trader_req_errors_repo
        self.queue = queue
        # Assuming that traders get reset after every request
        self.trader_list = []

    async def create(self, trader_req: trader_schema.TraderRequestWithoutValidation) -> trader_schema.TraderResponse:
        try:
            trader_req = trader_schema.TraderRequest(**trader_req.model_dump(exclude_unset=True))
        except ValidationError as e:
            await self.trader_req_errors_repo.add(
                TraderRequestErrors(
                    error=e.json()
                )
            )
            await self.trader_req_errors_repo.commit()
            raise TraderServiceValidationException(e.errors())

        self.queue.put(trader_req)
        return trader_schema.TraderResponse(**trader_req.model_dump(exclude_unset=True))

    async def get_errors_count(self) -> int:
        return await self.trader_req_errors_repo.count()

    def set_traders(self):
        while not self.queue.empty():
            trader = self.queue.get()
            self.trader_list.append(trader)

    def get_highest_total_asset_value_trader(self):
        if self.trader_list:
            yield max(self.trader_list, key=lambda x: x.assetValue)

        yield None

    def get_lowest_total_asset_value_trader(self):
        if self.trader_list:
            yield min(self.trader_list, key=lambda x: x.assetValue)

        yield None

    def get_most_frequently_traded_asset_type(self):
        asset_type_dict = {}
        for trader in self.trader_list:
            if trader.assetType in asset_type_dict:
                asset_type_dict[trader.assetType] += 1
            else:
                asset_type_dict[trader.assetType] = 1
        if not asset_type_dict:
            yield None
        most_frequently_traded_asset_type = max(asset_type_dict, key=asset_type_dict.get)
        yield most_frequently_traded_asset_type

    def get_average_value_of_assets_traded(self):
        total_asset_value = 0
        for trader in self.trader_list:
            total_asset_value += trader.assetValue
        if not self.trader_list:
            yield 0
        average_value_of_assets_traded = total_asset_value / len(self.trader_list)
        yield round(average_value_of_assets_traded, 2)

    def start_analysis(self) -> trader_schema.DataAnalyserResponse:
        # Assuming that the queue is filled with traders,
        # and no more traders are added to the queue
        self.set_traders()
        highest_trader = next(self.get_highest_total_asset_value_trader())
        lowest_trader = next(self.get_lowest_total_asset_value_trader())
        mft_asset_type = next(self.get_most_frequently_traded_asset_type())
        avg_asset_traded = next(self.get_average_value_of_assets_traded())

        return trader_schema.DataAnalyserResponse(
            highest_trader=highest_trader,
            lowest_trader=lowest_trader,
            most_frequently_traded_asset_type=mft_asset_type,
            average_value_of_assets_traded=avg_asset_traded
        )
