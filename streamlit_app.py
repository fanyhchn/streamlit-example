import streamlit as st
from datetime import datetime

def calculate_pregnancy_info(due_date, today):
    today = datetime.strptime(today, "%Y-%m-%d").date()
    pregnancy_days = (due_date - today).days
    pregnancy_weeks = 39 - pregnancy_days // 7
    pregnancy_days %= 7
    return pregnancy_weeks, 7 - pregnancy_days

def calculate_pregnancy_info_interface(due_date_str, today_str):
    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
        weeks, days = calculate_pregnancy_info(due_date, today_str)
        result = f"孕周: {weeks} 周 {days} 天"
    except ValueError:
        result = "请输入有效的日期格式（YYYY-MM-DD）"
    return result

# Streamlit app
st.title("孕周计算器")

# Input form
due_date = st.text_input("请输入预产期（YYYY-MM-DD）：")
today_date = st.text_input("请输入今天的日期（YYYY-MM-DD）：", value=datetime.now().date())

# Calculate button
if st.button("计算"):
    result = calculate_pregnancy_info_interface(due_date, today_date)
    st.write(result)
