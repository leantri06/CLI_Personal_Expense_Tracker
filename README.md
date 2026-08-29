# 💰 CLI Personal Expense Tracker (Ứng Dụng Quản Lý Chi Tiêu Cá Nhân)

> Một ứng dụng dòng lệnh (Command Line Interface - CLI) nhỏ gọn, mạnh mẽ giúp theo dõi và quản lý thu chi cá nhân hàng ngày, được xây dựng hoàn toàn bằng **Python** theo kiến trúc **Lập trình hướng đối tượng (OOP)** và phân tách module chuyên nghiệp.

---

## ✨ Tính Năng Nổi Bật

- ➕ **Quản lý giao dịch (CRUD):** Thêm, xem và xóa các khoản thu nhập / chi tiêu dễ dàng.
- 📊 **Báo cáo & Thống kê thông minh:**
  - Tự động tính **Tổng thu nhập**, **Tổng chi tiêu** và **Số dư hiện tại**.
  - Tự động phân tích và tìm ra **Danh mục chiếm chi tiêu nhiều nhất**.
- 💾 **Lưu trữ dữ liệu bền vững:** Tự động đồng bộ và lưu trữ dữ liệu vào file `expenses.json`, dữ liệu không bị mất khi thoát ứng dụng.
- 🛡️ **Chống Crash an toàn (Error Handling):** Bắt ngoại lệ `try - except` chặt chẽ, kiểm tra hợp lệ số tiền và ngày tháng theo định dạng chuẩn Việt Nam (`DD-MM-YYYY`).
- 🏗️ **Kiến trúc OOP sạch sẽ (Clean Architecture):** Tách biệt rõ ràng giữa tầng dữ liệu (Model), tầng lưu trữ (Storage), tầng nghiệp vụ (Tracker) và tầng giao diện (CLI).

---

## 🏛️ Cấu Trúc Dự Án

```text
CLI_Personal_Expense_Tracker/
│
├── models.py        # Định nghĩa lớp Transaction (Khuôn mẫu dữ liệu, to_dict, from_dict)
├── storage.py       # Định nghĩa lớp JsonStorage (Đọc/Ghi file JSON an toàn)
├── tracker.py       # Định nghĩa lớp ExpenseTracker (Quản lý nghiệp vụ, thêm/xóa/thống kê)
├── main.py          # Giao diện dòng lệnh CLI (Menu tương tác & nhận input)
├── expenses.json    # File cơ sở dữ liệu JSON (Tự động tạo)
├── .gitignore       # Bỏ qua các file tạm/rác khi đẩy lên Git
└── README.md        # Tài liệu hướng dẫn sử dụng dự án
```

---

## 🛠️ Kiến Thức Python Áp Dụng

| Thành phần | Khái niệm & Kỹ thuật Python |
| :--- | :--- |
| **Giao diện dòng lệnh** | Vòng lặp `while True`, câu lệnh rẽ nhánh `if-elif-else`, `input()`, `f-strings` format căn lề. |
| **Xử lý ngoại lệ** | Bắt lỗi `ValueError`, `TypeError` với `try - except`. |
| **Xử lý thời gian** | Module `datetime`: `strftime` (định dạng chuỗi) & `strptime` (kiểm tra ngày hợp lệ). |
| **Lưu trữ dữ liệu** | Context Manager `with open(...)`, module `json` (`json.dump`, `json.load`), bắt lỗi `FileNotFoundError`. |
| **Thuật toán & Thống kê** | List Comprehension, `sum()`, Dictionary grouping với `.get()`, tìm cực trị với `max(key=...)`. |
| **Lập trình Hướng đối tượng (OOP)** | Class, Object, Constructor `__init__`, `@classmethod` (Factory Method), Dependency Injection. |

---

## 🚀 Hướng Dẫn Cài Đặt & Chạy Ứng Dụng

### 1. Yêu cầu hệ thống
* Đã cài đặt **Python 3.8** trở lên trên máy tính.

### 2. Tải mã nguồn về máy
```bash
git clone https://github.com/<tên-tài-khoản-của-bạn>/CLI_Personal_Expense_Tracker.git
cd CLI_Personal_Expense_Tracker
```

### 3. Chạy chương trình
Chạy trực tiếp file `main.py` qua Terminal:

```bash
python main.py
```

---

## 🖥️ Minh Họa Sử Dụng

```text
=============================================
  💰 QUẢN LÝ CHI TIÊU CÁ NHÂN (CLI Tracker)
=============================================
1. Thêm giao dịch mới
2. Xem danh sách giao dịch
3. Xoá giao dịch
4. Báo cáo thống kê
0. Thoát
=============================================
👉 Nhập lựa chọn của bạn (0-4): 4

--- 📊 BÁO CÁO THỐNG KÊ CHI TIÊU ---
💰 Tổng thu nhập:  +15,000,000 VNĐ
💸 Tổng chi tiêu:  -3,500,000 VNĐ
💵 Số dư hiện tại:  11,500,000 VNĐ
-----------------------------------
🔥 Chi tiêu nhiều nhất cho: Ăn uống (2,100,000 VNĐ)
```

---
