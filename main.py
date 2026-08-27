"""
Ứng dụng Quản Lý Chi Tiêu Cá Nhân (CLI Personal Expense Tracker)
Giai đoạn 1: Nền tảng & Vòng lặp cơ bản
"""

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
    # 0. Thoát
    print("0. Thoát")
    # (Gợi ý: Dùng các lệnh print())
    print("=" * 45)


def add_transaction():
    """Hàm thêm một giao dịch mới vào danh sách transactions"""
    global next_id

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
    amount = float(input("Nhập số tiền (VNĐ): "))
    # TODO 1.6: Nhập danh mục (Ăn uống, Lương...), ngày tháng, và ghi chú
    catagory = input("Nhập danh mục (Ăn uống, Lương, Mua sắm): ")
    date = input("Nhập ngày giao dịch: ")
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
    next_id += 1
    print(f"Đã thêm giao dịch #{next_id} thành công!")

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


def main():
    """Vòng lặp chính điều khiển chương trình"""
    while True:
        show_menu()
        
        # TODO 1.12: Nhận lựa chọn từ người dùng bằng input()
        # TODO 1.13: Dùng if / elif / else để gọi các hàm tương ứng:
                # - Nếu chọn 1 -> gọi add_transaction()
                # - Nếu chọn 2 -> gọi list_transactions()
                # - Nếu chọn 0 -> in lời chào và dùng 'break' để thoát vòng lặp
                # - Khác -> in thông báo lựa chọn không hợp lệ
        choice = input("Nhập lựa chọn của bạn (0-2): ")
        if choice == "0":
            print("\n Cảm ơn bạn đã sử dụng ứng dụng! Tạm biệt.")
            break
        elif choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions()
        else:
            print("\n Lựa chọn không hợp lệ! Vui lòng chọn lại.")
        


if __name__ == "__main__":
    main()
