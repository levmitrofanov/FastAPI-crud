from pydantic import BaseModel, ConfigDict

class TodoItem(BaseModel):
    item: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "item": "Read the next chapter of the book"
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
