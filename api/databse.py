from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:major-ring:', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__   = 'user'
    id       = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email    = Column(String(120), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f"<User('{self.id}', '{self.username}', '{self.email}')>"

# User.__table__.create(bind=engine, checkfirst=True)
#
from sqlalchemy.orm import sessionmaker
#
Session = sessionmaker(bind=engine)
session = Session()
#
# input_data = User(
#     username='test',
#     email='test@test.com'
# )
# session.add(input_data)
# session.commit()
