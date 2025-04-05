import random
import streamlit as st

# Initialize session state variables
def initialize_game(lower=1, upper=100, max_tries=10):
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(lower, upper)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'max_tries' not in st.session_state:
        st.session_state.max_tries = max_tries
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'message' not in st.session_state:
        st.session_state.message = "Guess the Number between 1 - 100"

# Reset the game
def reset_game():
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = "Guess the Number between 1 - 100"

# Main game logic
def number_guess_user():
    initialize_game()

    st.title("Number Guessing Game (User)")
    st.subheader("Welcome to the Number Guessing Game!")
    st.info(st.session_state.message)

    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game()
    else:
        guess = st.number_input("Enter your Guess Number:", min_value=1, max_value=100, step=1, key="guess_input")
        if st.button("Submit Guess"):
            st.session_state.attempts += 1
            if guess > st.session_state.number:
                st.session_state.message = "Hint: Try a Lower Number..."
            elif guess < st.session_state.number:
                st.session_state.message = "Hint: Try a Higher Number..."
            else:
                st.session_state.message = "Congratulations! You guessed the Correct Number!"
                st.session_state.game_over = True

            if st.session_state.attempts >= st.session_state.max_tries and not st.session_state.game_over:
                st.session_state.message = f"Game Over! The correct number was {st.session_state.number}."
                st.session_state.game_over = True

        st.write(f"Attempts Left: {st.session_state.max_tries - st.session_state.attempts}")

# Run the game
number_guess_user()