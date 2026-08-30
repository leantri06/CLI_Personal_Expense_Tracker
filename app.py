import streamlit as st
import pandas as pd
from tracker import ExpenseTracker

st.set_page_config(page_title = "Expense Tracker", page_icon = "💰", layout = "wide")
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
tracker = ExpenseTracker()
st.title("💰 Quản Lý Chi Tiêu Cá Nhân")
st.divider()
summary = tracker.get_summary()
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("💰 Tổng Thu Nhập", f"+{summary['total_income']:,.0f} VNĐ")
col2.metric("💸 Tổng Chi Tiêu", f"-{summary['total_expense']:,.0f} VNĐ")
col3.metric("💵 Số Dư Hiện Tại", f"{summary['balance']:,.0f} VNĐ")
col4.metric("🍕 Danh Mục Chi Tiêu Nhiều Nhất", f"{summary['top_category']}")
col5.metric(f"😱 Số tiền chi cho {summary['top_category']}", f"{summary['top_amount']:,.0f} VNĐ")
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