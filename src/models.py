import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'Follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname =  Column(String(250))
    email = Column(String(250), nullable=False)
    # person = relationship(Person)

class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__='Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    author_id = Column(Integer,ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class Media(Base):
    __tablename__='Media'
    id = Column(Integer,primary_key=True)
    type = Column(Enum)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('Post.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')