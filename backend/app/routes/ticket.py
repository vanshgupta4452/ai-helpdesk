from fastapi import APIRouter

router = APIRouter()

tickets = []

@router.post("/ticket/create")
def create_ticket(data: dict):
    ticket = {
        "id": len(tickets) + 1,
        "title": data["title"],
        "user_id": data["user_id"]
    }
    tickets.append(ticket)
    return {"message": "Ticket created", "ticket": ticket}