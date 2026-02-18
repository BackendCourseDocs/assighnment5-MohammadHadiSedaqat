from fastapi import FastAPI, Query
import requests
from pydantic import BaseModel, Field
from typing import Optional


class Book_Validation(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    author: str = Field(..., min_length=3, max_length=100)
    publisher: str = Field(..., min_length=3, max_length=100)
    first_publish_year: int = Field(..., ge=0)


app = FastAPI()

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
            "first_publish_year": book.get("first_publish_year"),
        }
    )


@app.get("/books")
async def search_books(
    q: str = Query(..., min_length=3, max_length=100, description="Search query"),
    skip: Optional[int] = Query(None, ge=0, le=100, description="Number of results to skip"),
    limit: Optional[int] = Query(None, ge=0, le=100, description="Number of results to return")
):
    query = q.lower()

    results = [
        book
        for book in books
        if query in book["title"].lower()
        or query in book["author"].lower()
        or query in book["publisher"].lower()
        or query in str(book["first_publish_year"])
    ]

    if skip is None:
        skip = 0
    if limit is None:
        limit = len(results)
    paginated = results[skip: skip + limit]

    return {
        "query": q,
        "count": len(paginated),
        "results": paginated,
        "skip": skip,
        "limit": limit,
    }


@app.post("/books")
async def add_book(task: Book_Validation):
    books.append(
        {
            "title": task.title,
            "author": task.author,
            "publisher": task.publisher,
            "first_publish_year": task.first_publish_year,
        }
    )
    return task
