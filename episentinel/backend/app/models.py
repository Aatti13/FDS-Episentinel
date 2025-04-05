import os
from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database import Base
from datetime import datetime

class Users(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String, unique=True, nullable=False)
  email = Column(String, unique=True, nullable=False)
  password_hash = Column(String, nullable=False)
  created_at = Column(DateTime, default=datetime.now)

class EpidemicReport(Base):
  __tablename__ = "epidemic_report"
  id = Column(Integer, primary_key=True, index=True)
  disease = Column(String, nullable=False)
  location = Column(String, nullable=False)
  source = Column(String, nullable=False)
  mention_count = Column(Integer, default=1)
  sentiment_score = Column(Float)
  reported_at = Column(DateTime, default=datetime.now)