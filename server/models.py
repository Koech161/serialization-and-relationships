from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin


convention = {
    "ix" : "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(metadata=metadata)

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'
    serialize_rules = ('-books.author',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    books = db.relationship('Book', back_populates='author')

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'
    serialize_rules = ('-author.books',)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)
    review = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    author = db.relationship('Author', back_populates ='books')