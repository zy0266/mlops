from pydantic import BaseModel


class InputData(BaseModel):
    cut: float = 1
    color: float = 1
    clarity: float = 1


class PredictionOut(BaseModel):
    price: float
