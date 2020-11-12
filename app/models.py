#!/usr/bin/env python # coding: utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datatime

db = SQLAlchemy()

class Book(db.Model):
  """
  書籍モデル
  """
  __tablename__="books"
  id = Column(Integer, primary_key=True)
  title = Column(Unicode(255))
  auther = Column(Unicode(255))
  publisher - Column(Unicode(255))
  
  #初期化
  def __init__(title, auther, publisher)
    self.title = title.title()
    self.auther = auther.title()
    self.publisher = publisher.title()

class Diary(db.model):
    __tablename__ = "Diaries"
    id = Column(Integer, primary_key=True)
    date = Column(unicode(255))
    book_title = Column(unicode(255), ForeignKey('Books.title'))
    impression = Column(UnicodeText)

    book = relationship( "Book", backref('diaries', order_by=id))

    def __init__(book_title, impression):
        self.date = datetime.utcnow().strftime( '%Y-%m-%d %H:%M:%S' )
        self.book_title = book_title.title()
        self.impression = impression.title()
