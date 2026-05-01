import importlib.util
import io
import sys
import unittest
from contextlib import redirect_stdout
from datetime import datetime as dt
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parent.parent / "personal-expense-tracker.py"


def load_tracker_module():
    spec = importlib.util.spec_from_file_location("personal_expense_tracker", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class PersonalExpenseTrackerTests(unittest.TestCase):
    def setUp(self):
        self.tracker = load_tracker_module()
        self.original_expenses = list(self.tracker.expenses)
        self.original_categories = set(self.tracker.categories)
        self.tracker.expenses.clear()

    def tearDown(self):
        self.tracker.expenses[:] = self.original_expenses
        self.tracker.categories.clear()
        self.tracker.categories.update(self.original_categories)

    def test_expense_string_format(self):
        expense = self.tracker.Expense(12.5, "Groceries", dt(2026, 5, 1), "Milk")

        self.assertEqual(
            str(expense),
            "Spend $12.50 on Groceries on 2026-05-01 00:00:00. Milk",
        )

    def test_add_expense_appends_to_global_list(self):
        expense_date = dt(2026, 5, 1)

        self.tracker.addExpense(19.99, "Dining Out", expense_date, "Lunch")

        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].amount, 19.99)
        self.assertEqual(self.tracker.expenses[0].category, "Dining Out")
        self.assertEqual(self.tracker.expenses[0].date, expense_date)
        self.assertEqual(self.tracker.expenses[0].description, "Lunch")

    def test_spending_sums_all_expenses(self):
        self.tracker.addExpense(10.0, "Groceries", dt(2026, 5, 1), "Bread")
        self.tracker.addExpense(25.5, "Transportation", dt(2026, 5, 2), "Bus pass")

        self.assertEqual(self.tracker.spending(), 35.5)

    def test_get_oldest_date_returns_earliest_expense(self):
        first = dt(2026, 4, 29)
        second = dt(2026, 5, 1)
        self.tracker.addExpense(5.0, "Shopping", second, "Pen")
        self.tracker.addExpense(15.0, "Health", first, "Medicine")

        self.assertEqual(self.tracker.getOldestDate(), first)

    def test_organize_list_by_date_sorts_expenses(self):
        first = dt(2026, 4, 29)
        second = dt(2026, 5, 1)
        self.tracker.addExpense(20.0, "Shopping", second, "Notebook")
        self.tracker.addExpense(8.0, "Health", first, "Bandage")

        self.tracker.organizeListByDate()

        self.assertEqual(self.tracker.expenses[0].date, first)
        self.assertEqual(self.tracker.expenses[1].date, second)

    def test_delete_expense_removes_item_by_number(self):
        self.tracker.addExpense(10.0, "Groceries", dt(2026, 5, 1), "Milk")
        self.tracker.addExpense(20.0, "Shopping", dt(2026, 5, 2), "Shirt")

        self.tracker.deleteExpense(1)

        self.assertEqual(len(self.tracker.expenses), 1)
        self.assertEqual(self.tracker.expenses[0].category, "Shopping")

    def test_view_expenses_prints_numbered_list(self):
        self.tracker.addExpense(7.25, "Entertainment", dt(2026, 5, 1), "Movie")

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.tracker.viewExpenses()

        self.assertIn("1. Spend $7.25 on Entertainment on 2026-05-01 00:00:00. Movie", buffer.getvalue())


if __name__ == "__main__":
    unittest.main()
