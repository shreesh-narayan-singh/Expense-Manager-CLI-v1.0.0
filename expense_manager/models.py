from typing import TypedDict


class Expense(TypedDict):
    id: int
    description: str
    amount: float
    category: str