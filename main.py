"""
Ứng dụng Quản Lý Chi Tiêu Cá Nhân (CLI Personal Expense Tracker)
Giai đoạn 1: Nền tảng & Vòng lặp cơ bản
"""
from datetime import datetime
from tracker import ExpenseTracker

tracker = ExpenseTracker()
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
        category_choice = input("Nhập danh mục (1: Ăn uống, 2: Lương, 3: Mua sắm): ")
        if category_choice == "1":
            category = "Ăn uống"
            break
        elif category_choice == "2":
            category = "Lương"
            break
        elif category_choice == "3":
            category = "Mua sắm"
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
    new_item = tracker.add_transaction(trans_type, amount, category, date, note)
    print(f"Đã thêm giao dịch #{new_item.id} thành công")

def list_transactions():
    """Hàm hiển thị tất cả các giao dịch"""
    print("\n--- DANH SÁCH GIAO DỊCH ---")
    if not tracker.transactions:
        print("Chưa có giao dịch nào!")
        return
    for t in tracker.transactions:
        print(f"Mã: {t.id:<5} | Ngày: {t.date} | Loại: {t.type} | Số tiền: {t.amount:,.0f} | Danh mục: {t.category} | Ghi chú: {t.note}")

def delete_transaction():
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
    if tracker.delete_transaction(delete_id):
        print("Xóa giao dịch thành công!")
    else:
        print(f"Không tìm thấy giao dịch có mã #{delete_id}!")

def view_summary():
    summary = tracker.get_summary()
    print(f"Tổng thu nhập:  {summary['total_income']:,.0f} VNĐ")
    print(f"Tổng chi tiêu:  {summary['total_expense']:,.0f} VNĐ")
    print(f"Số dư hiện tại: {summary['balance']:,.0f} VNĐ")
    if summary['top_category']:
        print(f"Chi tiêu nhiều nhất cho: {summary['top_category']} ({summary['top_amount']:,.0f} VNĐ)")

def main():
    """Vòng lặp chính điều khiển chương trình"""
    while True:
        show_menu()
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
