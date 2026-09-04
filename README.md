# 💰 Personal Expense Tracker (Ứng Dụng Quản Lý Chi Tiêu Cá Nhân)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Architecture](https://img.shields.io/badge/architecture-OOP%20Clean%20Code-brightgreen.svg)]()
[![Storage](https://img.shields.io/badge/storage-JSON-orange.svg)]()

> Một ứng dụng quản lý thu chi cá nhân nhỏ gọn, trực quan và mạnh mẽ được phát triển bằng **Python**. Ứng dụng hỗ trợ đồng thời 2 giao diện: **Giao diện Dòng lệnh (CLI)** truyền thống và **Giao diện Web Trực quan (Streamlit Dashboard)** hiện đại, cùng chia sẻ một nền tảng lưu trữ dữ liệu bền vững theo chuẩn **Lập trình hướng đối tượng (OOP)**.

---

## 📌 Mục Lục

1. [Tính Năng Nổi Bật](#-tính-năng-nổi-bật)
2. [Cấu Trúc Thư Mục](#️-cấu-trúc-thư-mục)
3. [Cài Đặt & Khởi Chạy](#-cài-đặt--khởi-chạy)
4. [📖 Hướng Dẫn Sử Dụng Chi Tiết](#-hướng-dẫn-sử-dụng-chi-tiết)
   - [Cách 1: Sử dụng Giao diện Dòng lệnh (CLI)](#1-sử-dụng-giao-diện-dòng-lệnh-cli---python-mainpy)
   - [Cách 2: Sử dụng Giao diện Web (Streamlit)](#2-sử-dụng-giao-diện-web-trực-quan-streamlit---streamlit-run-apppy)
5. [Cấu Trúc Lưu Trữ Dữ Liệu](#-cấu-trúc-lưu-trữ-dữ-liệu-expensesjson)
6. [Xử Lý Lỗi & An Toàn Dữ Liệu](#-xử-lý-lỗi--an-toàn-dữ-liệu)

---

## ✨ Tính Năng Nổi Bật

- ➕ **Quản lý giao dịch linh hoạt (CRUD):** Thêm khoản thu/chi, xem danh sách và xóa giao dịch dễ dàng.
- 📊 **Thống kê & Phân tích tức thời:**
  - Tự động tính toán **Tổng thu nhập**, **Tổng chi tiêu** và **Số dư hiện tại**.
  - Phân tích danh mục chiếm tỷ trọng chi tiêu nhiều nhất kèm số tiền cụ thể.
- 🖥️ **Đa nền tảng giao diện:**
  - **CLI (Terminal):** Nhẹ, nhanh, thao tác bàn phím thuận tiện, không cần thư viện ngoài.
  - **Web Dashboard (Streamlit):** Giao diện đẹp mắt, bảng dữ liệu linh hoạt, thẻ metric trực quan.
- 💾 **Lưu trữ dữ liệu bền vững:** Tự động đồng bộ vào file `expenses.json`, dữ liệu không bị mất khi thoát ứng dụng.
- 🛡️ **Kiểm tra dữ liệu chặt chẽ:** Bắt lỗi số tiền âm, ký tự lạ, tự động chuẩn hóa ngày tháng theo định dạng `DD-MM-YYYY`.
- 🏗️ **Kiến trúc OOP phân lớp sạch sẽ:** Tách bạch giữa Model (`models.py`), Storage (`storage.py`), Tracker (`tracker.py`) và Giao diện (`main.py` / `app.py`).

---

## 🏛️ Cấu Trúc Thư Mục

```text
Expense_Tracker/
│
├── models.py          # Lớp Transaction: Định nghĩa khuôn mẫu dữ liệu (to_dict, from_dict)
├── storage.py         # Lớp JsonStorage: Đọc/ghi dữ liệu bền vững vào file JSON
├── tracker.py         # Lớp ExpenseTracker: Nghiệp vụ quản lý thu chi, tính toán thống kê
├── main.py            # Giao diện dòng lệnh CLI (Menu tương tác & vòng lặp điều khiển)
├── app.py             # Giao diện Web Dashboard phát triển bằng Streamlit & Pandas
├── expenses.json      # Cơ sở dữ liệu JSON (Tự động tạo khi thêm giao dịch)
├── requirements.txt   # Danh sách thư viện Python cần thiết (streamlit, pandas)
├── .gitignore         # Cấu hình các file bỏ qua không commit lên Git
└── README.md          # Tài liệu hướng dẫn sử dụng chi tiết
```

---

## 🚀 Cài Đặt & Khởi Chạy

### 1. Yêu cầu hệ thống
- Máy tính đã cài đặt **Python 3.8** trở lên ([Tải Python](https://www.python.org/downloads/)).
- Đã cài đặt Git.

### 2. Tải mã nguồn về máy
Mở Terminal / Command Prompt / PowerShell và chạy:

```bash
git clone https://github.com/leantri06/Expense_Tracker.git
cd Expense_Tracker
```

### 3. Cài đặt thư viện phụ thuộc (Dành cho bản Web)
Chạy lệnh sau để cài đặt các thư viện cần thiết (`streamlit`, `pandas`):

```bash
pip install -r requirements.txt
```

*(Lưu ý: Nếu bạn chỉ sử dụng bản dòng lệnh CLI `main.py`, bạn không cần cài đặt thêm thư viện nào).*

---

## 📖 Hướng Dẫn Sử Dụng Chi Tiết

Ứng dụng cung cấp **2 cách sử dụng** tùy theo sở thích và nhu cầu của bạn:

---

### 1. Sử dụng Giao diện Dòng lệnh (CLI) - `python main.py`

Khởi chạy ứng dụng qua Terminal:
```bash
python main.py
```

Khi chạy, màn hình sẽ hiển thị Menu chính:

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
👉 Nhập lựa chọn của bạn (0-4):
```

#### 🔹 Chức năng 1: Thêm giao dịch mới (`Phím 1`)
Hệ thống sẽ hướng dẫn bạn nhập từng thông tin:
1. **Loại giao dịch:** Nhập `1` cho Chi tiêu (*Expense*) hoặc `2` cho Thu nhập (*Income*).
2. **Số tiền:** Nhập số tiền bằng số (VNĐ), ví dụ: `50000`, `15000000`. Hệ thống tự động kiểm tra số tiền phải > 0.
3. **Danh mục:** Chọn theo danh sách có sẵn:
   - `1`: Ăn uống
   - `2`: Lương
   - `3`: Mua sắm
4. **Ngày giao dịch:** 
   - Nhập theo định dạng `DD-MM-YYYY` (Ví dụ: `04-09-2026`).
   - **Mẹo:** Nhấn **Enter** để trống thì hệ thống sẽ **tự động lấy ngày hôm nay**.
5. **Ghi chú:** Nhập mô tả chi tiết (ví dụ: `Ăn trưa cơm tấm`). Nếu để trống, mặc định ghi chú là `Không`.

*Sau khi nhập xong, hệ thống sẽ cấp phát một mã ID tự tăng và thông báo thêm thành công.*

#### 🔹 Chức năng 2: Xem danh sách giao dịch (`Phím 2`)
Hiển thị toàn bộ lịch sử các khoản thu chi đã ghi nhận với đầy đủ: Mã ID, Ngày tháng, Loại giao dịch, Số tiền (đã định dạng dấu phẩy dễ nhìn), Danh mục và Ghi chú.

```text
--- DANH SÁCH GIAO DỊCH ---
Mã: 1     | Ngày: 04-09-2026 | Loại: Income  | Số tiền: 15,000,000 | Danh mục: Lương    | Ghi chú: Lương tháng 8
Mã: 2     | Ngày: 04-09-2026 | Loại: Expense | Số tiền: 50,000     | Danh mục: Ăn uống  | Ghi chú: Ăn sáng
```

#### 🔹 Chức năng 3: Xoá giao dịch (`Phím 3`)
- Nhập **Mã ID** của giao dịch bạn muốn xóa (tham khảo ID từ Chức năng 2).
- Nếu tìm thấy ID: Giao dịch sẽ được xóa khỏi bộ nhớ và đồng bộ ngay vào file `expenses.json`.
- Nếu nhập ID không tồn tại hoặc nhập sai định dạng số: Hệ thống sẽ hiển thị cảnh báo an toàn mà không bị crash.

#### 🔹 Chức năng 4: Báo cáo thống kê (`Phím 4`)
Tổng hợp nhanh bức tranh tài chính hiện tại của bạn:
- **Tổng thu nhập (Total Income)**: Tổng số tiền từ các giao dịch loại Thu nhập.
- **Tổng chi tiêu (Total Expense)**: Tổng số tiền từ các giao dịch loại Chi tiêu.
- **Số dư hiện tại (Balance)**: `Tổng thu nhập - Tổng chi tiêu`.
- **Danh mục chi nhiều nhất (Top Category)**: Tìm ra danh mục nào đang "ngốn" nhiều tiền nhất và tổng tiền đã chi cho mục đó.

```text
--- 📊 BÁO CÁO THỐNG KÊ CHI TIÊU ---
Tổng thu nhập:  15,000,000 VNĐ
Tổng chi tiêu:  3,500,000 VNĐ
Số dư hiện tại: 11,500,000 VNĐ
Chi tiêu nhiều nhất cho: Ăn uống (2,100,000 VNĐ)
```

#### 🔹 Thoát chương trình (`Phím 0`)
Lưu toàn bộ thay đổi và kết thúc phiên làm việc an toàn.

---

### 2. Sử dụng Giao diện Web Trực quan (Streamlit) - `streamlit run app.py`

Khởi chạy ứng dụng Web cục bộ bằng lệnh:
```bash
streamlit run app.py
```
> Trình duyệt web của bạn sẽ tự động mở trang dashboard tại địa chỉ: `http://localhost:8501`.

#### 🧭 Bố cục và Thao tác trên Giao diện Web:

| Khu vực | Chức năng | Chi tiết thao tác |
| :--- | :--- | :--- |
| **Thanh bên trái (Sidebar)** | **➕ Thêm Giao Dịch Mới** | - Chọn loại giao dịch qua menu thả xuống (*💸 Chi tiêu* hoặc *💰 Thu nhập*).<br>- Nhập số tiền (có nút tăng giảm bước nhảy 5.000 VNĐ).<br>- Chọn danh mục đa dạng: *Ăn uống, Lương, Mua sắm, Giải trí, Học tập, Xăng, Khác*.<br>- Chọn ngày giao dịch trực quan qua bảng lịch Date Picker.<br>- Điền ghi chú và nhấn **➕ Thêm Ngay** (Hệ thống tự reload và cập nhật). |
| **Thanh bên trái (Sidebar)** | **🗑️ Xóa Giao Dịch** | - Chọn trực tiếp Mã ID cần xóa từ danh sách có sẵn.<br>- Nhấn nút đỏ **❌ Xóa Giao Dịch Này** để loại bỏ giao dịch an toàn. |
| **Màn hình chính (Dashboard)** | **5 Thẻ Thống Kê (Metrics)** | Hiển thị to, rõ các chỉ số:<br>1. 💰 **Tổng Thu Nhập**<br>2. 💸 **Tổng Chi Tiêu**<br>3. 💵 **Số Dư Hiện Tại**<br>4. 🍕 **Chi Nhiều Nhất** (Tên danh mục)<br>5. 😱 **Số Tiền Chi** (Số tiền của danh mục cao nhất) |
| **Màn hình chính (Dashboard)** | **📋 Bảng Lịch Sử Giao Dịch** | - Hiển thị toàn bộ bảng dữ liệu với font chữ lớn, dễ nhìn.<br>- Hỗ trợ sort theo cột, xem chi tiết từng dòng.<br>- Định dạng số tiền kèm đơn vị `VNĐ` chuẩn hóa. |

---

## 💾 Cấu Trúc Lưu Trữ Dữ Liệu (`expenses.json`)

Mọi giao dịch được lưu trữ dưới định dạng JSON tiêu chuẩn, cho phép dễ dàng sao lưu hoặc tích hợp với các hệ thống khác:

```json
[
    {
        "id": 1,
        "type": "Income",
        "amount": 15000000.0,
        "category": "Lương",
        "date": "04-09-2026",
        "note": "Lương tháng"
    },
    {
        "id": 2,
        "type": "Expense",
        "amount": 45000.0,
        "category": "Ăn uống",
        "date": "04-09-2026",
        "note": "Cà phê sáng"
    }
]
```

---

## 🛡️ Xử Lý Lỗi & An Toàn Dữ Liệu

- **Chống lỗi định dạng số:** Nhập chữ hoặc ký tự đặc biệt ở trường số tiền hay ID sẽ được chặn bằng `try - except ValueError`, hướng dẫn nhập lại thay vì tắt ứng dụng.
- **Ràng buộc số tiền:** Không chấp nhận số tiền nhỏ hơn hoặc bằng 0.
- **Tự động khôi phục:** Nếu file `expenses.json` chưa tồn tại trong lần đầu chạy, ứng dụng tự khởi tạo danh sách trống mà không báo lỗi `FileNotFoundError`.
- **Tự sinh ID thông minh:** Tự động tính toán `next_id = max(id) + 1` để đảm bảo không bao giờ trùng lặp mã giao dịch kể cả sau khi khởi động lại.

---

## 👨‍💻 Tác Giả & Giấy Phép

- Phát triển bởi: **leantri06**
- GitHub: [@leantri06](https://github.com/leantri06)
- Giấy phép: [MIT License](LICENSE) (Tự do học tập, sử dụng và phát triển mở rộng).
