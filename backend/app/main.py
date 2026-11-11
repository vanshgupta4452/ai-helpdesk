from fastapi import FastAPI
from routes import ticket, user, ai

app = FastAPI()

app.include_router(ticket.router)
app.include_router(user.router)
app.include_router(ai.router)