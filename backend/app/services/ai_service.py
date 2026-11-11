def process_query(query: str):
    query = query.lower()

    if "ticket" in query:
        return "ACTION: create_ticket"
    elif "password" in query:
        return "ACTION: reset_password"
    else:
        return "QUESTION"