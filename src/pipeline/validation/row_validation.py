from __future__ import annotations

from typing import TypeVar, Type, Any, get_origin, get_args
from pydantic import BaseModel, ValidationError

T = TypeVar("T", bound=BaseModel)


def _is_optional(annotation: Any) -> bool:
    return (
        get_origin(annotation) is not None
        and type(None) in get_args(annotation)
    )

def validate_rows_with_optional_cleanup(rows: list[dict], model: Type[T]) -> list[T]:
    result: list[T] = []

    for row in rows:
        validated: T | None = None

        try:
            validated = model.model_validate(row)
        except ValidationError as error:
            cleaned = dict(row)

            for err in error.errors():
                loc = err.get("loc", ())
                field: str | None = None

                if loc:
                    first = loc[0]
                    if isinstance(first, str):
                        field = first

                if field is not None:
                    field_info = model.model_fields.get(field)
                    if field_info and _is_optional(field_info.annotation):
                        cleaned[field] = None

            try:
                validated = model.model_validate(cleaned)
            except ValidationError:
                print("problem")

        if validated is not None:
            result.append(validated)

    return result

