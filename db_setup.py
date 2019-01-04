#!/usr/bin/env python

import sys
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_context
import random, string
from itsdangerous import(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    username = Column(String(250), index = True, nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))
    pw_hash = Column(String(64))

    # def hash_pw(self, password):
    #     self.pw_hash = pwd_context.encrypt(password)
    #
    # def verify_pw(self, password):
    #     return pwd_context.verify(password, self.pw_hash)
    #
    # def generate_auth_token(self, expiration = 600):
    #     s = Serializer(secret_key, expires_in = expiration)
    #     return s.dumps({'id': self.id})
    #
    # @staticmethod
    # def verify_auth_token(token):
    #     s = Serializer(secret_key)
    #     try:
    #         data = s.loads(token)
    #     except SignatureExpired:
    #         return None
    #     except BadSignature:
    #         return None
    #     user_id = data['id']
    #     return user_id


class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                'name': self.name,
                'id': self.id,
                'user_id': self.user_id,
        }


class Item(Base):
    __tablename__ = 'item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(800))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category, backref='item')
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
                'name': self.name,
                'id': self.id,
                'description': self.description,
                'category': self.category.name,
        }


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
