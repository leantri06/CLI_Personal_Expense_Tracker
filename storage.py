import json
from models import Transaction
class JsonStorage: 
    def __init__(self, filename = "expenses.json"):
        self.filename = filename
    def save(self, transactions):
        """
        Nhận vào 1 danh sách các đối tượng Transaction,
        chuyển đổi từng đối tượng thành dict bằng .to_dict()
        và ghi vào file JSON.
        """
        data = [t.to_dict() for t in transactions]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Đã lưu {len(data)} giao dịch vào expenses.json")
    def load(self):
        """
        Đọc file JSON và chuyển đổi từng dict thành đối tượng Transaction bằng .from_dict().
        Trả về: Danh sách các đối tượng Transaction.
        Nếu không có file (FileNotFoundError): Trả về danh sách rỗng [].
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                transactions = [Transaction.from_dict(item) for item in data]
                return transactions
        except FileNotFoundError:
            print("Không tìm thấy file expenses.json")
            return []