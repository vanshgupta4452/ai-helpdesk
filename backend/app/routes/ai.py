from fastapi import APIRouter
from services.ai_service import process_query

router = APIRouter()

@router.post("/ai/query")
def ai_query(data: dict):
    query = data["query"]
    response = process_query(query)
    return {"response": response}