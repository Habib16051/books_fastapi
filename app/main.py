from fastapi import FastAPI, HTTPException


#  This is fastapi instance that are using as container of this entire application.
#  And it controls all the routes and endpoints, middleware, request responses, and all the other things that are going to be used in this application.
app = FastAPI(title="My First API", description="API for learning FastAPI", version="0.1")

BOOKS = [
    {"id": 1, "title": "Book One", "author": "Author A", 'category': 'Fiction'},
    {"id": 2, "title": "Book Two", "author": "Author B", 'category': 'Non-Fiction'},
    {"id": 3, "title": "Book Three", "author": "Author C", 'category': 'Science'},
    {"id": 4, "title": "Book Four", "author": "Author D", 'category': 'History'},
    {"id": 5, "title": "Book Five", "author": "Author E", 'category': 'Biography'},
    {"id": 6, "title": "Book Six", "author": "Author F", 'category': 'Fantasy'},
    {"id": 7, "title": "Book Seven", "author": "Author G", 'category': 'Mystery'},
    {"id": 8, "title": "Book Eight", "author": "Author H", 'category': 'Romance'},
    {"id": 9, "title": "Book Nine", "author": "Author I", 'category': 'Thriller'},
    {"id": 10, "title": "Book Ten", "author": "Author J", 'category': 'Horror'}
]

# This is a get method in order to get all the books altogether
@app.get("/books")
async def read_all_books():
    return BOOKS

# For getting the book one by one dynamically
@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
