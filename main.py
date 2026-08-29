"""
Ứng dụng Quản Lý Chi Tiêu Cá Nhân (CLI Personal Expense Tracker)
Giai đoạn 1: Nền tảng & Vòng lặp cơ bản
"""
from datetime import datetime
import json
# ==========================================
# 1. KHỞI TẠO BỘ NHỚ TẠM (RAM)
# ==========================================
# TODO 1.1: Khai báo 1 danh sách rỗng để chứa các giao dịch
transactions = []

# TODO 1.2: Khai báo biến ID khởi đầu
next_id = 1


def show_menu():
    """Hiển thị menu chính"""
    print("\n" + "=" * 45)
    print("  💰 QUẢN LÝ CHI TIÊU CÁ NHÂN (CLI Tracker)")
    print("=" * 45)
    # TODO 1.3: In ra các lựa chọn:
    # 1. Thêm giao dịch mới
    print("1. Thêm giao dịch mới")
    # 2. Xem danh sách giao dịch
    print("2. Xem danh sách giao dịch")
    # 3. Xoá giao dịch
    print("3. Xoá giao dịch")
    # 4. Báo cáo thống kê
    print("4. Báo cáo thống kê")
    # 0. Thoát
    print("0. Thoát")
    # (Gợi ý: Dùng các lệnh print())
    print("=" * 45)


def add_transaction():
    """Hàm thêm một giao dịch mới vào danh sách transactions"""
    global next_id
    today_str = datetime.now().strftime("%d-%m-%Y")
    print("\n--- THÊM GIAO DỊCH MỚI ---")
    
    # TODO 1.4: Nhập loại giao dịch (Thu hay Chi)
    # Gợi ý: Dùng input() để nhận '1' (Chi) hoặc '2' (Thu)
    while True:
        type_choice = input("Loại (1: Chi tiêu, 2: Thu nhập): ").strip()
        if type_choice == "1":
            trans_type = "Expense"
            break
        elif type_choice == "2":
            trans_type = "Income"
            break
        else:
            print("Nhập sai thông tin. Yêu cầu nhập lại")
    # TODO 1.5: Nhập số tiền và ép kiểu sang float
    # Gợi ý: float(input(...))
    while True:
        try:
            amount = float(input("Nhập số tiền (VNĐ): "))
            if amount <= 0:
                print(" Số tiền phải lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Lỗi: Vui lòng nhập số, không nhập ký tự lạ!")
    # TODO 1.6: Nhập danh mục (Ăn uống, Lương...), ngày tháng, và ghi chú
    while True:
        catagory_choice = input("Nhập danh mục (1: Ăn uống, 2: Lương, 3: Mua sắm): ")
        if catagory_choice == "1":
            catagory = "Ăn uống"
            break
        elif catagory_choice == "2":
            catagory = "Lương"
            break
        elif catagory_choice == "3":
            catagory = "Mua sắm"
            break
        else:
            print("Nhập sai thông tin. Yêu cầu nhập lại")
    date_input = input(f"Nhập ngày (DD-MM-YYYY, mặc định {today_str}): ").strip()
    if not date_input:
        date = today_str
    else:
        try:
            datetime.strptime(date_input, "%d-%m-%Y")
            date = date_input
        except ValueError:
            print("Định dạng ngày không hợp lệ, tự động lấy ngày hôm nay.")
            date = today_str
    note = input("Nhập ghi chú: ")
    if note == "":
        note = "Không"
    # TODO 1.7: Tạo 1 dictionary chứa đầy đủ các thông tin: id, type, amount, category, date, note
    transaction = {
        "id": next_id,
        "type": trans_type,
        "amount": amount,
        "category": catagory,
        "date": date,
        "note": note
    }
    # TODO 1.8: Thêm dictionary vừa tạo vào danh sách transactions (dùng .append())
    transactions.append(transaction)
    # TODO 1.9: Tăng next_id lên 1 đơn vị
    print(f"Đã thêm giao dịch #{next_id} thành công!")
    save_to_json()
    next_id += 1


def list_transactions():
    """Hàm hiển thị tất cả các giao dịch"""
    print("\n--- DANH SÁCH GIAO DỊCH ---")
    # TODO 1.10: Kiểm tra nếu danh sách transactions rỗng (len == 0 hoặc not transactions)
    # thì thông báo và return
    if not transactions:
        print("Chưa có giao dịch nào!")
        return
    for item in transactions:
        print(f"Mã: {item['id']:<5} | Ngày: {item['date']} | Loại: {item['type']} | Số tiền: {item['amount']:,.0f} | Danh mục: {item['category']} | Ghi chú: {item['note']}")
    # TODO 1.11: Dùng vòng lặp for để duyệt qua từng giao dịch trong transactions và in ra màn hình

def delete_transaction():
    if not transactions:
        print("Chưa có giao dịch nào để xoá!")
        return
    while True:
        try:
            delete_id = int(input("Nhập id giao dịch cần xoá: "))
            if delete_id <= 0:
                print("Id phải là số lớn hơn 0!")
                continue
            break
        except ValueError:
            print("Nhập Id là một con số, không nhập ký tự lạ.")
    found = False
    for item in transactions:
        if item['id'] == delete_id:
            transactions.remove(item)
            print("Xoá giao dịch thành công!")
            found = True
            break
    if not found:
        print(f"Không tìm thấy giao dịch có mã #{delete_id}!")
    save_to_json()

def view_summary():
    if not transactions:
            print("Không tìm thấy giao dịch nào để thống kê!")
            return
    
    total_income = sum(item['amount'] for item in transactions if item['type'] == "Income")
    total_expense = sum(item['amount'] for item in transactions if item['type'] == "Expense")
    balance = total_income - total_expense

    print(f"Tổng thu nhập: {total_income:,.0f} VNĐ")
    print(f"Tổng chi tiêu: {total_expense:,.0f} VNĐ")
    print(f"Số dư hiện tại: {balance:,.0f} VNĐ")

    category_spending = {}
    for item in transactions:
        if item['type'] == "Expense":
            cat = item['category']
            if cat in category_spending:
                category_spending[cat] += item['amount']
            else:
                category_spending[cat] = item['amount']
    if category_spending:
        top_cat = max(category_spending, key=category_spending.get)
        print(f"Chi tiêu nhiều nhất cho: {top_cat}: {category_spending[top_cat]:,.0f} VNĐ")

def save_to_json(filename = "expenses.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(transactions, f, indent = 4, ensure_ascii=False)
    print("Đã lưu dữ liệu vào file thành công")

def load_from_json(filename = "expenses.json"):
    global transactions, next_id
    try:
        with open(filename, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            if transactions:
                max_id = max(item['id'] for item in transactions)
                next_id = max_id + 1
            else:
                next_id = 1
        print(f"Đã nạp thành công {len(transactions)} giao dịch từ bộ nhớ!")
    except FileNotFoundError:
        transactions = []
        next_id = 1
        print("Chưa tìm thấy file dữ liệu cũ, đã tạo phiên làm việc mới.")

def main():
    load_from_json()
    """Vòng lặp chính điều khiển chương trình"""
    while True:
        show_menu()
        
        # TODO 1.12: Nhận lựa chọn từ người dùng bằng input()
        # TODO 1.13: Dùng if / elif / else để gọi các hàm tương ứng:
                # - Nếu chọn 1 -> gọi add_transaction()
                # - Nếu chọn 2 -> gọi list_transactions()
                # - Nếu chọn 0 -> in lời chào và dùng 'break' để thoát vòng lặp
                # - Khác -> in thông báo lựa chọn không hợp lệ
        choice = input("Nhập lựa chọn của bạn (0-4): ")
        if choice == "0":
            print("\n Cảm ơn bạn đã sử dụng ứng dụng! Tạm biệt.")
            break
        elif choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        elif choice == "3":
            delete_transaction()
        elif choice == "4":
            view_summary()
        else:
            print("\n Lựa chọn không hợp lệ! Vui lòng chọn lại.")
        


if __name__ == "__main__":
    main()
