from pydantic import BaseModel, ConfigDict
from typing import List

class TodoItem(BaseModel):
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "item": "Read the next chapter of the book"
            }
        }
    )

class TodoItems(BaseModel):
    todos: List[TodoItem]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "todos": [
                    {"item": "Example schema 1!"},
                    {"item": "Example schema 2!"}
                ]
            }
        }
    )

class Todo(BaseModel):
    id: int
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "item": "Пример задачи разработчика Митрофанова Льва"
            }
        }
    )
