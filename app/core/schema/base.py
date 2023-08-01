from dataclasses import Field

from pydantic import BaseModel

from core.schema.fields import NameField


class Person(BaseModel):
    name: NameField
