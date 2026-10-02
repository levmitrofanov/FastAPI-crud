from fastapi import APIRouter, Path, HTTPException, status
from pydantic import BaseModel, ConfigDict
from typing import List

# Модели данных для персональной темы (Управление сетевыми узлами / вычислительной сетью)
class NetworkNode(BaseModel):
    id: int
    hostname: str
    ip_address: str
    role: str
    status: str = "active"

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "hostname": "gateway-core-01",
                "ip_address": "192.168.1.1",
                "role": "edge-router",
                "status": "active"
            }
        }
    )

class NetworkNodeUpdate(BaseModel):
    role: str
    status: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "role": "core-switch",
                "status": "maintenance"
            }
        }
    )

class NetworkNodeResponse(BaseModel):
    hostname: str
    ip_address: str
    status: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "hostname": "gateway-core-01",
                "ip_address": "192.168.1.1",
                "status": "active"
            }
        }
    )

class NetworkNodesList(BaseModel):
    nodes: List[NetworkNodeResponse]

nodes_router = APIRouter(prefix="/nodes", tags=["Сетевые узлы (Персональная тема)"])
nodes_db: List[NetworkNode] = []

@nodes_router.post("", status_code=status.HTTP_201_CREATED)
async def create_node(node: NetworkNode) -> dict:
    for existing in nodes_db:
        if existing.id == node.id or existing.ip_address == node.ip_address:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Сетевой узел с ID {node.id} или IP {node.ip_address} уже зарегистрирован (Митрофанов Лев)."
            )
    nodes_db.append(node)
    return {"message": "Сетевой узел успешно зарегистрирован (Митрофанов Лев).", "node_id": node.id}

@nodes_router.get("", response_model=NetworkNodesList)
async def list_nodes() -> dict:
    return {"nodes": nodes_db}

@nodes_router.get("/{node_id}")
async def get_node(node_id: int = Path(..., title="Идентификатор сетевого узла")) -> dict:
    for node in nodes_db:
        if node.id == node_id:
            return {"node": node}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сетевой узел с ID {node_id} не найден в топологии (Митрофанов Лев)."
    )

@nodes_router.put("/{node_id}")
async def update_node(
    update_data: NetworkNodeUpdate, 
    node_id: int = Path(..., title="Идентификатор сетевого узла для обновления")
) -> dict:
    for node in nodes_db:
        if node.id == node_id:
            node.role = update_data.role
            node.status = update_data.status
            return {"message": "Конфигурация сетевого узла успешно обновлена (Митрофанов Лев)."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сетевой узел с ID {node_id} не найден в топологии (Митрофанов Лев)."
    )

@nodes_router.delete("/{node_id}")
async def delete_node(node_id: int = Path(..., title="Идентификатор узла для удаления")) -> dict:
    for i, node in enumerate(nodes_db):
        if node.id == node_id:
            nodes_db.pop(i)
            return {"message": "Сетевой узел выведен из эксплуатации и удален (Митрофанов Лев)."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Сетевой узел с ID {node_id} не найден в топологии (Митрофанов Лев)."
    )
