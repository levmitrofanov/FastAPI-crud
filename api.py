from fastapi import FastAPI
from todo import todo_router
from nodes import nodes_router

app = FastAPI(
    title="Todos & Network Nodes CRUD API — ПЗ №5",
    description="Разработка CRUD-приложения, моделей ответов и обработки ошибок в FastAPI (студент Митрофанов Лев)",
    version="1.0.0"
)

@app.get("/")
async def welcome() -> dict:
    return {"message": "Митрофанов Лев — CRUD API на FastAPI (ПЗ №5)"}

app.include_router(todo_router)
app.include_router(nodes_router)
