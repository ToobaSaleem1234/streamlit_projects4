import streamlit as st
import time

# display app:
st.set_page_config(page_title="CountDown Timer", page_icon='🕕', layout="centered")

# Countdown function:
def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # 00:59
        st.write(time_format, end='\r')  # Display time
        time.sleep(1)  # Delay
        seconds -= 1
    st.write("00:00 \nTime's Up!\n")

# Streamlit app UI
st.title("Countdown Timer")
st.subheader("Enter the time in seconds for countdown:")

# User input for total seconds
time_seconds = st.number_input("Time in seconds", min_value=1, step=1)

# Start countdown button
if st.button("Start Countdown"):
    st.status("Starting countdown...")
    countdown_timer(time_seconds)
