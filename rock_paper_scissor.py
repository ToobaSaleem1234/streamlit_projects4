import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissor Game", page_icon=":rock:", layout="centered")

st.title("Rock Paper Scissor Game")
st.write("Welcome to the Rock Paper Scissor game!")
st.write("Choose your option and see if you can beat the computer!")

def rock_paper_scissor():
    user_choice = st.radio("Choose your option:", ("Rock", "Paper", "Scissor"))
    computer_choice = random.choice(["Rock", "Paper", "Scissor"])

    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        st.warning("Oops!......It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        st.success("Congratulations!.....You win!")
    else:
        st.warning("Sorry!......You lose!")
rock_paper_scissor()