from pydantic import BaseModel
from typing import List

class DecisionCreate(BaseModel):
    decision_id: str
    company_id: str
    chosen_cost: float
    alternatives: List[float]

class DecisionUpdate(BaseModel):
    chosen_cost: float
    alternatives: List[float]
