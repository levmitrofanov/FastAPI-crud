from fastapi import FastAPI
from todo import todo_router

app = FastAPI(
    title="Todos API — ПЗ №5",
    description="Разработка CRUD-приложения, моделей ответов и обработки ошибок (студент Митрофанов Лев)",
    version="1.0.0"
)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Митрофанов Лев — CRUD API"}

app.include_router(todo_router)
