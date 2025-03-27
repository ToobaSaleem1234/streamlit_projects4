# streamlit
import streamlit as st
import random

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 5em;
        color: #FF6347;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .instructions {
        font-size: 1.2em;
        color: #555;
        margin: 20px;
        background-color: #f4f4f9;
        padding: 20px;
        border-radius: 10px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.1em;
        border: none;
        border-radius: 5px;
        padding: 15px;
        cursor: pointer;
        margin-top: 20px;
    }
    .button:hover {
        background-color: #45a049;
    }
    .hint {
        color: #ff9800;
        font-size: 1.2em;
    }
    .error {
        color: #f44336;
        font-size: 1.3em;
    }
    .success {
        color: #4caf50;
        font-size: 1.3em;
    }
    </style>
""", unsafe_allow_html=True)

# Function to start the game
def number_guessing_game(lower=1, upper=10, max_tries=5):
    # Streamlit title with icon
    st.markdown('<p class="title">🎮 Project 02: Number Guessing Game (Computer)</p>', unsafe_allow_html=True)

    st.markdown("<p class='title'>**Welcome to the Number Guessing Game!**</p>",unsafe_allow_html=True)
    
    # Game Instructions
    st.markdown("""
    <div class="instructions">
    
    You need to guess a number between 1 and 100. You have a total of 5 attempts to get the correct number.
    
    **Game Instructions:**
    - Input your guess and hit the "Submit Guess" button below.
    - If your guess is too low or too high, the game will guide you.
    - Good luck and have fun!
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state variables if they don't exist
    if 'number_to_guess' not in st.session_state:
        st.session_state.number_to_guess = random.randint(lower, upper)
        st.session_state.attempts_left = max_tries
        st.session_state.guesses = []
    
    # Show current attempts and guesses
    st.write(f"Attempts left: {st.session_state.attempts_left}")
    st.write(f"Guessed numbers: {st.session_state.guesses}")
    
    # User input for guess
    user_guess = st.number_input("Enter your guess (1 to 100):", min_value=1, max_value=100, step=1)
    
    # Button to submit guess
    if st.button("Submit Guess"):
        if user_guess == st.session_state.number_to_guess:
            st.success(f"🎉 Congratulations! You guessed the correct number in {max_tries - st.session_state.attempts_left} attempts!")
            st.session_state.number_to_guess = random.randint(lower, upper)  # reset number for new game
            st.session_state.attempts_left = max_tries  # reset attempts
            st.session_state.guesses = []  # reset guesses
        elif user_guess < st.session_state.number_to_guess:
            st.warning("Hint: Try a Higher Number..")
            st.session_state.attempts_left -= 1
        else:
            st.warning("Hint: Try a Lower Number..")
            st.session_state.attempts_left -= 1

        st.session_state.guesses.append(user_guess)

        # Check if attempts are over
        if st.session_state.attempts_left == 0:
            st.error(f"Game Over! The correct number was {st.session_state.number_to_guess}.")
            st.session_state.number_to_guess = random.randint(lower, upper)  # reset number for new game
            st.session_state.attempts_left = max_tries  # reset attempts
            st.session_state.guesses = []  # reset guesses

# Run the game function
number_guessing_game()