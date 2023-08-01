import pytest
from assignment.trader.schema import TraderRequestWithoutValidation


@pytest.fixture
def sample_traders():
    traders = [
        TraderRequestWithoutValidation(
            name="trader one",
            transaction_type="buy",
            assetType="stock",
            assetValue=100.0,
            quantity=10,
        ),
        TraderRequestWithoutValidation(
            name="trader two",
            transaction_type="sell",
            assetType="crypto",
            assetValue=200.0,
            quantity=5,
        ),
        TraderRequestWithoutValidation(
            name="trader three",
            transaction_type="buy",
            assetType="stock",
            assetValue=150.0,
            quantity=8,
        ),
        TraderRequestWithoutValidation(
            name="trader four",
            transaction_type="sell",
            assetType="crypto",
            assetValue=180.0,
            quantity=7,
        ),
        TraderRequestWithoutValidation(
            name="trader5",
            transaction_type="buy",
            assetType="stock",
            assetValue=120.0,
            quantity=15,
        ),
        TraderRequestWithoutValidation(
            name="trader six",
            transaction_type="sell",
            assetType="crypto",
            assetValue=250.0,
            quantity=3,
        ),
        TraderRequestWithoutValidation(
            name="trader seven",
            transaction_type="buy",
            assetType="stock",
            assetValue=300.0,
            quantity=20,
        ),
    ]
    return traders


async def test_create_trade(client):
    trader_data = {
        "name": "trader one",
        "transaction_type": "buy",
        "assetType": "stock",
        "assetValue": 100.0,
        "quantity": 10,
    }

    response = await client.post("/trader-queue", json=trader_data)
    print (response.json())

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["transaction_type"] == trader_data["transaction_type"]
    assert response.json()["assetType"] == trader_data["assetType"]
    assert response.json()["assetValue"] == trader_data["assetValue"]
    assert response.json()["quantity"] == trader_data["quantity"]


async def test_get_errors_count(client):
    response = await client.get("/trader-queue/errors/count")
    assert response.status_code == 200
    assert response.json() == 0


async def test_create_trade_with_invalid_that_contain_invalid_data(client, sample_traders):
    for trader in sample_traders:
        response = await client.post("/trader-queue", json=trader.model_dump(exclude_unset=True))

    response = await client.get("/trader-queue/errors/count")
    assert response.status_code == 200
    assert response.json() == 1


async def test_start_analysis(client, sample_traders):
    for trader_req in sample_traders:
        await client.post("/trader-queue", json=trader_req.dict())

    response = await client.post("/trader/analyse")

    assert response.status_code == 200
    data = response.json()
    assert data['highest_trader']['name'] == "trader seven"
    assert data['lowest_trader']['name'] == "trader one"
    assert data["most_frequently_traded_asset_type"] == "stock"
    assert data["average_value_of_assets_traded"] == 196.67
