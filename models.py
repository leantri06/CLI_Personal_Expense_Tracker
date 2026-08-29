class Transaction:
    def __init__(self, id, trans_type, amount, category, date, note = "Không"):
        self.id = id
        self.type = trans_type
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "note": self.note
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data['id'],
            trans_type = data['type'],
            amount = data['amount'],
            category = data['category'],
            date = data['date'],
            note = data['note', 'Không']
        )