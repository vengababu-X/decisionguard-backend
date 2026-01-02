from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Decision(Base):
    __tablename__ = "decisions"
    id = Column(Integer, primary_key=True)
    decision_id = Column(String, unique=True)
    company_id = Column(String)

class DecisionState(Base):
    __tablename__ = "decision_states"
    id = Column(Integer, primary_key=True)
    decision_id = Column(Integer, ForeignKey("decisions.id"))
    chosen_cost = Column(Float)
    best_alternative = Column(Float)
    regret = Column(Float)
    risk = Column(String)
    explanation = Column(String)
