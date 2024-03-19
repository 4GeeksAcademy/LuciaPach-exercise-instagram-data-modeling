import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, Table, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyEnum(enum.Enum):
    video = 1
    photo = 2

follower_user = Table('follower_user', Base.metadata,
    Column('follower_id', Integer, ForeignKey('follower.id')),
    Column('user_id', Integer, ForeignKey('user.id')))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower_name = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", secondary=follower_user, back_populates="follower")
    

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    type = Column(Enum(MyEnum))
    post_id = Column(Integer, ForeignKey('post.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media = relationship(Media)
    comment = relationship(Comment)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    follower = relationship("Follower", secondary=follower_user, back_populates="user")



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

    #def to_dict(self):
     #  return {}
