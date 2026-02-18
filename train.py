from fastapi import FastAPI, Query
import requests
from pydantic import BaseModel
app = FastAPI()

class Book_Validation(BaseModel):
    title: str
    author: str
    publisher: str

url = "https://openlibrary.org/search.json"
params = {"q": "python", "limit": 58}

response = requests.get(url, params=params)
data = response.json()

books = []

for book in data.get("docs", []):
    books.append(
        {
            "title": book.get("title"),
            "author": (
                book.get("author_name", ["Unknown"])[0]
                if book.get("author_name")
                else "Unknown"
            ),
            "publisher": (
                book.get("publisher", ["Unknown"])[0]
                if book.get("publisher")
                else "Unknown"
            ),
        }
    )


@app.get("/books")
def search_books(q: str = Query(..., description="Search query")):
    query = q.lower()

    results = [
        book
        for book in books
        if query in book["title"].lower()
        or query in book["author"].lower()
        or query in book["publisher"].lower()
    ]

    return {"query": q, "count": len(results), "results": results}



@app.post("/books")
async def add_book(task: Book_Validation):
    books.append(
        {
            "title": task.title,
            "author": task.author,
            "publisher": task.publisher,
        }
    )
    return task
