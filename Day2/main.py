# simple hello world fastapi code by areesha kainat

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

# ----------------------------------------------------------------

# simple fastapi code that print msg,date,time and quote by areesha kainat

from fastapi import FastAPI, Request
from datetime import datetime
app = FastAPI(title="Creative Hello API", description="A playful and welcoming FastAPI server", version="1.0")

@app.get("/")
def read_root():
    return {
        "message": "Hello, Developer! Welcome to the FastAPI Universe.",
        "date": datetime.now().strftime("%A, %d %B %Y"),
        "time": datetime.now().strftime("%I:%M %p"),
        "quote": "Keep building. The future belongs to creators like you "
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {
        "item_id": item_id,
        "query": q or "Nothing specific, just exploring ",
        "tip": "Try / to get inspired again!"
    }
