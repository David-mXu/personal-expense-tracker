from dataclasses import dataclass, asdict
from datetime import dt
import json

@dataclass
class Expense:
    amount: float
    category: str
    date: dt
    description: str

    def __str__ (self):
        return f"Spend ${self.amount:.2f} on {self.category} on {self.date}. {self.description}"


categories = {
    "Housing", "Utilities", "Groceries", "Transportation", 
    "Dining Out", "Entertainment", "Shopping", "Health"
}

expenses = [] # for storing the list of expenses

while true: 

    changesMade = false
    
    command = input("Press: \n [1] to add a new expense \n [2] to view all expenses \n [3] to view total spending \n [4] to view spending by category \n [5] to delete an expense \n [6] to save or load data \n [7] to close program")

    if command == "1":
            new_expense = input("Add an expense in the following format: amount category date description")
            # need some way to determine category, date and description from each other

            # then input it into addExpense function

            changesMade = true
    elif command == "2":
        viewExpenses()
    elif command == "3":
        viewTotalSpending()
    elif command == "4":
        category_to_view = input("Enter category to view: ")
        viewSpendingByCategory(category_to_view)
    elif command == "5":
        expense_to_delete = input("Enter expense number to delete: ")
        deleteExpense(expense_to_delete)
        changesMade = true
    elif command == "6":
        save_or_load = input("Press S to save or L to load: ")
        if save_or_load.Lower() == "s":
            save()
            changesMade = false
        elif save_or_load.Lower() == "l":
            load()
        else:
            print("Invalid Input")
    elif command == "7":
        if(changesMade):
            warn = input("Would you like to save before you quit? [Y/N] ")
            if warn.Lower() == "y":
                save()
                changesMade = false
            elif warn.Lower() == "n":
                changesMade = false
                break
            else:
                print("Invalid Input")




# main functions
def addExpense(amount: float , category: str, date = dt.today(), description: str = "") -> None:
    newExpense = Expense(amount, category, date, description)
    expenses.append(newExpense)

def viewExpenses() -> None:
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense}")

def viewTotalSpending() -> None:
    print(spending())

def viewSpendingByCategory(category: str) -> None:
    return None

def deleteExpense(number: int) -> None:
    expenses.pop(number-1)

def save() -> None:
    saveCateogries()
    saveExpenses()
    print("Saved!")

def load() -> None:
    loadCategories()
    loadExpenses()
    print("Loaded!")

 
# helper functions
def spending(since: dt = expense.getOldestDate) -> float:
    spent = 0.0
    for expense in expenses:
        spent = spent + expense.amount
    return spent

def getOldestDate() -> dt:
    oldestDate = dt.today()
    for expense in expenses:
        if expense.date < oldestDate:
            oldestDate = expense.date
    return oldestDate

# helper functions for list of expenses
def organizeListByDate() -> None:
    expenses.sort(key=lambda x: x.date)

def validateCategory(cat: str) -> None:
    if cat not in categories:
        addOrNotAdd = input("Would you like to add " + cat + " as a category")
        if addOrNotAdd:
            cateogries.add(cat)

    return None


# functions for saving and loading data
def saveCateogries() -> None:
    # turn set of categories into a list
    with open("categories.json", "w") as file:
        json.dump(list(categories), file, indent=4)

def saveExpenses(expenses, filename: str = "expenses.json") -> None:
    # turn the expense objs to dictionaries (since json only takes in basic) 
    # ie list of objects to list of dictionaries

    save_expenses = [asdict(e) for e in expense]

    for e in expenses:
        # Convert object to a dictionary
        temp_dict = asdict(e)
        # JSON can't handle date objects, so convert to string
        temp_dict['date'] = temp_dict['date'].isoformat()
        save_data.append(temp_dict)

    with open(filename, "w") as file:
        json.dump(save_expenses, file, indent=4)  
    
def loadCategories() -> None:

    with open("categories.json", "r") as file:
        categories = set(json.load(file))
    
def loadExpenses(filename: str = "expenses.json"):

    try:
        with open(filename, "r") as f:
            raw_json = json.load(f)

        for expense in raw_json:
            # convert str date data to date objects
            expense['date'] = date.fromisoformat(item['date'])
            # Convert list of dictionaries back into Expense objects
            loaded_expenses.append(Expense(**item))
            return loaded_expenses
    except FileNotFoundError:
        return[]




