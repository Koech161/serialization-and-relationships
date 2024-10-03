from random import choice as rc
from faker import Faker
from app import app
from models import db, Author, Book

fake = Faker()
with app.app_context():
    Book.query.delete()
    Author.query.delete()

    authors = []
    for _ in range(20):
        author = Author(name=fake.name())
        authors.append(author)
    db.session.add_all(authors)    

    books = []
    genres = ['Fantasy', 'Fiction', 'Science','Non-Fiction', 'Biography','Mystery' ]

    for _ in range(100):
        title = fake.catch_phrase()
        while title in [b.title for b in books]:
            title = fake.catch_phrase()
        book = Book(title=title, review=fake.sentence(), author=rc(authors))
        books.append(book)   
    db.session.add_all(books) 
    db.session.commit()    