import random
import streamlit as st

# List of programming words
programming_words = [
    "algorithm", "variable", "function", "loop", "array", "class", "object", "debugging",
    "compiler", "syntax", "module", "method", "condition", "recursion", "pointer", "data",
    "binary", "hashmap", "string", "constant", "framework", "inheritance", "polymorphism",
    "closure", "exception", "parameter", "stack", "queue", "interface", "algorithmic",
    "iteration", "database", "network", "thread", "concurrency", "asynchronous", "scripting",
    "html", "css", "javaScript", "python", "ruby", "java", "c++", "php", "sql"
]

# Initialize session state for the game
def initialize_game():
    # Initialize session state variables
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'guessed_letters' not in st.session_state:
        st.session_state.guessed_letters = []
    if 'guessed_words' not in st.session_state:
        st.session_state.random_generate = random.choice(programming_words)
        st.session_state.guessed_words = ["_"] * len(st.session_state.random_generate)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 5

# Function to start the game
def hangman_game():
    initialize_game()

    # Get the random word to guess
    random_generate = st.session_state.random_generate
    guessed_words = st.session_state.guessed_words
    attempts = st.session_state.attempts
    guessed_letters = st.session_state.guessed_letters

    # Streamlit page setup
    st.title("Hangman Game")
    st.subheader("Welcome to the Hangman Game!")
    st.markdown("Guess the word by entering letters.")
    st.info(f"The word has {len(random_generate)} letters... and you have {attempts} chances to guess...\n")

    # Game status
    if st.session_state.game_over:
        st.write(f"The correct word was: {random_generate}")
        if st.button("Restart"):
            reset_game()

    else:
        # Show current state of the word
        st.write("Word:", " ".join(guessed_words))
        st.write(f"Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        st.write(f"Remaining Attempts: {attempts}")

        # Get user guess
    guess = st.text_input("Enter your guess (single letter):").lower()

    if guess:
        if len(guess) == 1 and guess.isalpha():
            if guess in st.session_state.guessed_letters:
                st.warning("You already guessed this letter! Try another letter.")
            else:
                st.session_state.guessed_letters.append(guess)

            if guess in st.session_state.random_generate:
                st.success(f"Correct guess! {guess} is in the word.")
                for i in range(len(st.session_state.random_generate)):
                    if st.session_state.random_generate[i] == guess:
                        st.session_state.guessed_words[i] = guess
            else:
                st.error("Oops! Wrong guess! Try again.")
                st.session_state.attempts -= 1

            # Check for game over conditions
            if "_" not in st.session_state.guessed_words:
                st.success(f"Congratulations! You guessed the correct word: {st.session_state.random_generate}")
                st.session_state.game_over = True
            elif st.session_state.attempts == 0:
                st.error("Game Over! You ran out of attempts.")
                st.session_state.game_over = True
                st.success(f"The correct guess was: {st.session_state.random_generate}")
    else:
        st.warning("Please enter a valid single letter.")
#Reset the game
def reset_game():
    # Reset all necessary session state attributes for the new game
    st.session_state.game_over = False
    st.session_state.guessed_letters = []
    st.session_state.random_generate = random.choice(programming_words)
    st.session_state.guessed_words = ["_"] * len(st.session_state.random_generate)
    st.session_state.attempts = 5

# Start the game
if 'game_started' not in st.session_state:
    st.session_state.game_started = True
hangman_game()