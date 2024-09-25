from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Define the Books table
class Book(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String)
    price = Column(Float)
    author_id = Column(Integer, ForeignKey('authors.author_id'))

    # Relationship with Author
    author = relationship('Author', back_populates='books')

# Define the Authors table
class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    bio = Column(String)

    # Relationship with Books
    books = relationship('Book', back_populates='author')

# Define the Customers table
class Customer(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

# Define the Transactions table
class Transaction(Base):
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    book_id = Column(Integer, ForeignKey('books.book_id'))
    transaction_date = Column(Date)

    # Relationships
    customer = relationship('Customer')
    book = relationship('Book')

# Function to create the database
def create_db():
    engine = create_engine('sqlite:///bookhaven.db')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_db()
    print("Database schema created!")
