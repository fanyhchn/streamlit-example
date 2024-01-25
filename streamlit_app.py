import streamlit as st
from datetime import datetime, timedelta
import time

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

# Function to be called every hour
def request_service():
    # Add your service request logic here
    from gradio_client import Client

    client = Client("https://aistudio.baidu.com/serving/app/16223/")
    result = client.predict(
				    "2024-01-25",	# str in '请输入预产期（YYYY-MM-DD）：' Textbox component
				    "2024-01-25",	# str in '请输入今天的日期（YYYY-MM-DD）：' Textbox component
				    fn_index=0
    )
    print(result)
    st.write("Service requested!")

# Streamlit app
st.title("孕周计算器")

# Input form
due_date = st.text_input("请输入预产期（YYYY-MM-DD）：")
today_date = st.text_input("请输入今天的日期（YYYY-MM-DD）：", value=datetime.now().date())

# Calculate button
if st.button("计算"):
    result = calculate_pregnancy_info_interface(due_date, today_date)
    st.write(result)

# Set up timer to request service every hour
while True:
    request_service()
    time.sleep(3600)  # Sleep for 1 hour
