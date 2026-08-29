# 🎉 TỔNG KẾT DỰ ÁN: CLI Personal Expense Tracker

Dự án **Ứng dụng Quản lý Chi tiêu Cá nhân trên dòng lệnh (CLI Personal Expense Tracker)** đã được hoàn thành 100% qua 4 giai đoạn học tập chủ động.

---

## 🏗️ Cấu trúc dự án hoàn chỉnh

```text
CLI_Personal_Expense_Tracker/
│
├── models.py       # [Lớp dữ liệu] Định nghĩa Transaction (to_dict, from_dict)
├── storage.py      # [Lưu trữ] Định nghĩa JsonStorage (Đọc/Ghi file expenses.json an toàn)
├── tracker.py      # [Nghiệp vụ] Định nghĩa ExpenseTracker (Thêm, Xóa, Thống kê, Quản lý ID)
├── main.py         # [Giao diện] Điều khiển Menu CLI và tương tác với người dùng
├── expenses.json   # [Dữ liệu] File lưu trữ dữ liệu bền vững
└── .gitignore      # Bỏ qua các file tạm/rác khi đẩy lên GitHub
```

---

## 📈 Kiến thức Python bạn đã làm chủ qua 4 giai đoạn

```mermaid
graph LR
    A["Giai đoạn 1: Nền tảng"] -->|input/print, list, dict, while| B["Giai đoạn 2: Bắt lỗi & Thống kê"]
    B -->|try-except, datetime, sum, list comprehension| C["Giai đoạn 3: File I/O"]
    C -->|with open, json.dump/load, FileNotFoundError| D["Giai đoạn 4: OOP & Tách Module"]
    D -->|Class, __init__, @classmethod, Dependency Injection| E["Hoàn thành Dự án Chuyên nghiệp"]
```

### 1. Giai đoạn 1: Nền tảng & Cấu trúc dữ liệu
* Sử dụng vòng lặp `while True` kết hợp `if - elif - else` và `break` để tạo Menu điều khiển.
* Quản lý dữ liệu bằng danh sách các từ điển (`list of dicts`) trong bộ nhớ RAM.
* Định dạng in chuỗi nâng cao với `f-string` (`:<5`, `:,.0f`).

### 2. Giai đoạn 2: Xử lý ngoại lệ & Tính toán thống kê
* Bắt ngoại lệ an toàn bằng khối `try - except ValueError` chống crash khi nhập sai số tiền/ID.
* Thư viện `datetime` chuẩn hóa ngày tháng, `strftime` (định dạng chuỗi) và `strptime` (phân tích chuỗi).
* Thuật toán thống kê: Tính tổng thu/chi bằng `sum()`, gom nhóm danh mục với `dict.get()`, tìm phần tử lớn nhất với `max()`.

### 3. Giai đoạn 3: Lưu trữ dữ liệu với File JSON
* Quản lý ngữ cảnh an toàn với Context Manager `with open(...) as f`.
* Chế độ file `"w"` (Write/Ghi đè) và `"r"` (Read/Đọc).
* Sử dụng thư viện `json` (`json.dump` và `json.load`).
* Bắt lỗi `FileNotFoundError` khi chạy lần đầu chưa có file.

### 4. Giai đoạn 4: Lập trình Hướng đối tượng (OOP) & Module hóa
* Khái niệm **Class & Object**: `Transaction`, `JsonStorage`, `ExpenseTracker`.
* Phương thức khởi tạo `__init__`, `self` (instance) và `cls` (`@classmethod` Factory Method).
* Kỹ thuật **Dependency Injection** và tham số mặc định (`storage=None`).
* Tách file theo chuẩn kiến trúc phân lớp chuyên nghiệp.

---

## 🚀 Lệnh Git để cập nhật toàn bộ dự án lên GitHub

Tại terminal, bạn chỉ cần chạy:

```bash
git add .
git commit -m "Complete CLI Personal Expense Tracker: Full OOP and Modular Architecture"
git push
```
