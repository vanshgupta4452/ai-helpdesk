# AI Helpdesk

An AI-assisted helpdesk and ticketing system. Tickets are handled by an LLM agent backed by retrieval-augmented generation over support documentation, with a chat interface for users and automated ticket management.

## Features

- **Ticket management** — create, track, and resolve support tickets
- **AI agent** — LangChain ReAct agent that reasons over tools (e.g. ticket creation) and drafts resolutions
- **RAG pipeline** — ingest support docs and retrieve relevant context to ground answers
- **Chat interface** — React frontend with a live chat box

## Stack

`FastAPI` `LangChain` `OpenAI` `React` `RAG` `Python`

## Project Structure

```
backend/
  app/
    agents/     # LLM agent (tools + execution)
    rag/        # document ingestion + retriever
    routes/     # user, ticket, AI endpoints
    services/   # business logic
    db/         # database setup
frontend/
  src/          # React app (chat UI)
```

## Getting Started

```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend
cd frontend
npm install && npm start
```
