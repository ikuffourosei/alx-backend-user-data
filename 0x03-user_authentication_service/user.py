#!/usr/bin/env python3
"""User"""
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    hashed_password = Column(String(length=250), nullable=False)
    session_id = Column(String(length=250), nullable=True)
    reset_token = Column(String(length=250), nullable=True)
