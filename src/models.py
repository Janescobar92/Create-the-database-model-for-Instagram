import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    firstname = Column(String(255))
    lastname =  Column(String(255))
    email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('User.id'))

class Comment(Base):
    __tablename__='Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text())
    author_id = Column(Integer,ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))

class Media(Base):
    __tablename__='Media'
    id = Column(Integer,primary_key=True)
    type_of = Column(Enum("video","image", "audio"))
    url = Column(Text())
    post_id = Column(Integer, ForeignKey('Post.id'))

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')