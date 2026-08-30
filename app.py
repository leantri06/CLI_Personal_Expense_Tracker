import streamlit as st
import pandas as pd
from tracker import ExpenseTracker

st.set_page_config(page_title = "Expense Tracker", page_icon = "💰", layout = "wide")

# 1. CSS tăng cỡ chữ to và rõ ràng
st.markdown("""
<style>
    /* Tăng cỡ chữ nội dung trong bảng lên 18px */
    [data-testid="stDataFrame"] div, [data-testid="stDataFrame"] span {
        font-size: 20px !important;
    }
    /* Tăng cỡ chữ và in đậm tiêu đề các cột */
    [data-testid="stDataFrame"] div[role="columnheader"] span {
        font-size: 19px !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# 2. Khởi tạo Tracker
tracker = ExpenseTracker()

# ==========================================
# 3. THANH BÊN TRÁI (SIDEBAR): THÊM & XÓA
# ==========================================
with st.sidebar:
    # --- PHẦN 1: THÊM GIAO DỊCH ---
    st.header("➕ Thêm Giao Dịch Mới")
    with st.form("add_form", clear_on_submit=True):
        trans_type = st.selectbox("Loại", ["Expense", "Income"], format_func=lambda x: "💸 Chi tiêu (Expense)" if x == "Expense" else "💰 Thu nhập (Income)")
        amount = st.number_input("Số tiền (VNĐ)", min_value=1000, step=5000, value=50000)
        category = st.selectbox("Danh mục", ["Ăn uống", "Lương", "Mua sắm", "Giải trí", "Học tập", "Khác"])
        date_selected = st.date_input("Ngày giao dịch")
        note = st.text_input("Ghi chú", placeholder="Ví dụ: Cà phê sáng...")
        
        btn_add = st.form_submit_button("➕ Thêm Ngay", use_container_width=True)
        
        if btn_add:
            date_str = date_selected.strftime("%d-%m-%Y")
            new_item = tracker.add_transaction(
                trans_type=trans_type,
                amount=float(amount),
                category=category,
                date=date_str,
                note=note.strip() if note.strip() else "Không"
            )
            st.success(f"✅ Đã thêm giao dịch #{new_item.id} thành công!")
            st.rerun() # Tải lại trang web để cập nhật số liệu
    st.divider()
    # --- PHẦN 2: XÓA GIAO DỊCH ---
    st.header("🗑️ Xóa Giao Dịch")
    if tracker.transactions:
        # Lấy danh sách các ID hiện có để người dùng chọn
        available_ids = [t.id for t in tracker.transactions]
        id_to_delete = st.selectbox("Chọn Mã ID cần xóa", options=available_ids)
        
        if st.button("❌ Xóa Giao Dịch Này", use_container_width=True, type="primary"):
            if tracker.delete_transaction(id_to_delete):
                st.success(f"Đã xóa giao dịch #{id_to_delete}!")
                st.rerun()
    else:
        st.caption("Chưa có giao dịch nào để xóa.")

# ==========================================
# 4. MÀN HÌNH CHÍNH: TIÊU ĐỀ & 5 THẺ THỐNG KÊ
# ==========================================
st.title("💰 Quản Lý Chi Tiêu Cá Nhân")
st.divider()
summary = tracker.get_summary()
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("💰 Tổng Thu Nhập", f"+{summary['total_income']:,.0f} VNĐ")
col2.metric("💸 Tổng Chi Tiêu", f"-{summary['total_expense']:,.0f} VNĐ")
col3.metric("💵 Số Dư Hiện Tại", f"{summary['balance']:,.0f} VNĐ")
col4.metric("🍕 Chi Nhiều Nhất", f"{summary['top_category']}")
col5.metric("😱 Số Tiền Chi", f"{summary['top_amount']:,.0f} VNĐ")
st.divider()
st.subheader("📋 Lịch sử giao dịch")
if not tracker.transactions:
    st.info("Chưa có giao dịch nào được ghi lại!")
else:
    df = pd.DataFrame([t.to_dict() for t in tracker.transactions])
    df = df.rename(columns={
        "id": "Mã ID",
        "type": "Loại",
        "amount": "Số tiền",
        "category": "Danh mục",
        "date": "Ngày giao dịch",
        "note": "Ghi chú"
    })
    df["Mã ID"] = df["Mã ID"].astype(str)
    df["Số tiền"] = df["Số tiền"].apply(lambda x: f"{x:,.0f} VNĐ")
    st.dataframe(df, use_container_width=True, hide_index=True)