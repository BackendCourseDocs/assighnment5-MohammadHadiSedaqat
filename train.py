from fastapi import FastAPI, Query, Form, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
import requests
from pydantic import BaseModel, Field
from typing import Optional
import os
import shutil


class Book_Validation(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    author: str = Field(..., min_length=3, max_length=100)
    publisher: str = Field(..., min_length=3, max_length=100)
    first_publish_year: int = Field(..., ge=0)
    image_url: Optional[str] = None



os.makedirs("images", exist_ok=True)
app = FastAPI()
app.mount("/images", StaticFiles(directory="images"), name="images")

url = "https://openlibrary.org/search.json"
params = {"q": "python", "limit": 58}
response = requests.get(url, params=params)
data = response.json()

books = []
id_nums = 1000

for book in data.get("docs", []):
    books.append(
        {
            "id": id_nums,
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
            "image_url": None,
        }
    )
    id_nums += 1


# GET: path or query
@app.get("/books")
async def search_books(
    q: str = Query(..., min_length=3, max_length=100, description="Search query"),
    skip: Optional[int] = Query(
        None, ge=0, le=100, description="Number of results to skip"
    ),
    limit: Optional[int] = Query(
        None, ge=0, le=100, description="Number of results to return"
    ),
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
    paginated = results[skip : skip + limit]

    return {
        "query": q,
        "count": len(paginated),
        "results": paginated,
        "skip": skip,
        "limit": limit,
    }


# POST: Form or Json
@app.post("/books")
async def add_book(
    title: str = Form(..., min_length=3, max_length=100),
    author: str = Form(..., min_length=3, max_length=100),
    publisher: str = Form(..., min_length=3, max_length=100),
    first_publish_year: int = Form(..., ge=0),
    image: Optional[UploadFile] = File(None),
):
    global id_nums

    image_url = None
    if image:
        image_path = f"images/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"http://127.0.0.1:8000/images/{image.filename}"

    book = {
        "id": id_nums,
        "title": title,
        "author": author,
        "publisher": publisher,
        "first_publish_year": first_publish_year,
        "image_url": image_url,
    }

    id_nums += 1
    books.append(book)
    return book


# DELETE: Path
@app.delete("/books/{id}")
def delete_book(id: int):
    for i, book in enumerate(books):
        if book["id"] == id:
            removed_book = books.pop(i)
            return {"message": "Book deleted", "Book": removed_book}
    raise HTTPException(status_code=404, detail="Book not found")


# PUT: Path, Form
@app.put("/books/{id}")
def update_fully_book(
    id: int,
    title: str = Form(..., min_length=3, max_length=100),
    author: str = Form(..., min_length=3, max_length=100),
    publisher: str = Form(..., min_length=3, max_length=100),
    first_publish_year: int = Form(..., ge=0),
    image: Optional[UploadFile] = File(None),
):

    image_url = None
    if image:
        image_path = f"images/{image.filename}"
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"http://127.0.0.1:8000/images/{image.filename}"

    for book in books:
        if book["id"] == id:
            book["title"] = title
            book["author"] = author
            book["publisher"] = publisher
            book["first_publish_year"] = first_publish_year
            book["image_url"] = image_url
            return {"message": "Book updated", "Book": book}

    raise HTTPException(status_code=404, detail="Book not found")


# PATCH: query, Form
@app.patch("/books/{id}")
def update_book_part(
    id: int,
    title: Optional[str] = Form(..., min_length=3, max_length=100),
    author: Optional[str] = Form(..., min_length=3, max_length=100),
    publisher: Optional[str] = Form(..., min_length=3, max_length=100),
    first_publish_year: Optional[int] = Form(..., ge=0),
    image: Optional[UploadFile] = File(None),
):
    image_url = None

    for book in books:
        if book["id"] == id:
            if title is not None:
                book["title"] = title
            if author is not None:
                book["author"] = author
            if publisher is not None:
                book["publisher"] = publisher
            if first_publish_year is not None:
                book["first_publish_year"] = first_publish_year
            if image:
                image_path = f"images/{image.filename}"
                with open(image_path, "wb") as buffer:
                    shutil.copyfileobj(image.file, buffer)
                image_url = f"http://127.0.0.1:8000/images/{image.filename}"
                book["image_url"] = image_url

            return {"message": "Book updated", "Book": book}

    raise HTTPException(status_code=404, detail="Book not found")
