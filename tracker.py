from models import Transaction
from storage import JsonStorage

class ExpenseTracker:
    def __init__(self, storage = None):
        """Khởi tạo Tracker, tự động nạp dữ liệu từ Storage"""
        self.storage = storage if storage else JsonStorage()
        self.transactions = self.storage.load()
        if self.transactions:
            self.next_id = max(t.id for t in self.transactions) + 1
        else: 
            self.next_id = 1
    def add_transaction(self, trans_type, amount, category, date, note="Không"):
        """Tạo đối tượng Transaction mới, lưu vào danh sách và ghi ra file"""
        new_trans = Transaction(self.next_id, trans_type, amount, category, date, note)
        self.transactions.append(new_trans)
        self.next_id += 1
        self.storage.save(self.transactions)
        return new_trans
    def delete_transaction(self, trans_id):
        for t in self.transactions:
            if t.id == trans_id:
                self.transactions.remove(t)
                self.storage.save(self.transactions)
                return True
        return False
    def get_summary(self):
        """Tính toán và trả về một dictionary chứa các số liệu thống kê"""
        total_income = sum(t.amount for t in self.transactions if t.type == "Income")
        total_expense = sum(t.amount for t in self.transactions if t.type == "Expense")
        balance = total_income - total_expense

        category_spending = {}
        for t in self.transactions:
            if t.type == "Expense":
                category_spending[t.category] = category_spending.get(t.category, 0) + t.amount
        top_cat = None
        top_amount = 0
        if category_spending:
            top_cat = max(category_spending, key=category_spending.get)
            top_amount = category_spending[top_cat]
        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "balance": balance,
            "top_category": top_cat,
            "top_amount": top_amount
        }