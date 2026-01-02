from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Decision(Base):
    __tablename__ = "decisions"

    id = Column(Integer, primary_key=True, index=True)
    decision_id = Column(String, unique=True, index=True)
    company_id = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class DecisionUpdate(Base):
    __tablename__ = "decision_updates"

    id = Column(Integer, primary_key=True, index=True)
    decision_id = Column(String, index=True)

    chosen_cost = Column(Float)
    alternatives = Column(JSON)

    regret = Column(Float)
    risk = Column(String)
    explanation = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
