import re
from typing import Any

# from pydantic.validators import str_validator

NAME_PATTERN = r"^[A-Za-z ]+$"

#
# class NameField(str):
#     """
#     Name validation field.
#
#     The name attribute must only contain letters and spaces.
#     """
#     max_length = 100
#     min_length = 1
#
#     @classmethod
#     def __modify_schema__(cls, field_schema: dict[str, Any]):
#         """Modify schema."""
#         field_schema.update(
#             examples=["John Doe", "Jane Doe"],
#             maxLength=cls.max_length,
#             minLength=cls.min_length,
#         )
#
#     @classmethod
#     def __get_validators__(cls):
#         """Get Validator."""
#         yield str_validator
#         yield cls.validate
#
#     @classmethod
#     def validate(cls, value):
#         """Name validator."""
#         if not value:
#             raise ValueError("required a valid NameField.")
#
#         if not re.match(NAME_PATTERN, value):
#             raise ValueError("Name must only contain letters and spaces.")
#
#         return value
