from dataclasses import dataclass
from datatime import date
import json

@dataclass
class Expense:
    amount: float
    category: str
    date: str
    description: str


categories = {
    "Housing", "Utilities", "Groceries", "Transportation", 
    "Dining Out", "Entertainment", "Shopping", "Health"
}

expense 

while true: 

    command = input("Press: \n [1] to add a new expense \n [2] to view all expenses \n [3] to view total spending \n [4] to view spending by category \n [5] to delete an expense \n [6] to save or load data \n [7] to close program")

    if command == "1":



def addExpense(amount: int , category: str, date = "today", description = ""):


def validateCategory(cat: str) -> None:
    if cat not in categories:
        addOrNotAdd = input("Would you like to add " + cat + " as a category")
        if addOrNotAdd:
            cateogries.add(cat)

    return None

def saveCateogries() -> None:
    # turn set of categories into a list




