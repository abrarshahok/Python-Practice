import json

books = {
    "To Kill a Mockingbird": {
        "author": "Harper Lee",
        "publication_year": 1960,
        "ISBN": "978-0-06-112008-4",
        "genre": "Fiction",
        "pages": 281,
        "publisher": "J.B. Lippincott & Co.",
        "language": "English"
    },
    "1984": {
        "author": "George Orwell",
        "publication_year": 1949,
        "ISBN": "978-0-452-28423-4",
        "genre": "Dystopian",
        "pages": 328,
        "publisher": "Secker & Warburg",
        "language": "English"
    }
}

json_form = json.dumps(books)
# print(json_form)

with open("/Users/abrar/Python Practice/info.txt", "w") as f:
    f.write(json_form)

f = open("/Users/abrar/Python Practice/info.txt", "r")
s = f.read()
# print(s)

book = json.loads(s)
print(book)