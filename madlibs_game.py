import streamlit as st

# MadLibs Game: Short Story
def madlibs_game():
    st.title("MadLibs Game: Short Story")
    st.info("Fill in the blanks to complete the story!")

    # User inputs
    name = st.text_input("Enter a name (person):")
    place = st.text_input("Enter a place:")
    adjective = st.text_input("Enter an adjective:")
    noun = st.text_input("Enter a noun:")
    verb = st.text_input("Enter a verb:")
    person = st.text_input("Enter another name (person):")

    # Generate story when all inputs are provided
    if st.button("Generate Story"):
        if name and place and adjective and noun and verb and person:
            # Story template
            story = f"""
            Once upon a time, {name} went to {place}. It was a very {adjective} day.
            Suddenly, {name} saw a {noun} that was trying to {verb}. 
            To their surprise, {person} appeared and joined them!
            It was the most unforgettable day for them.
            """
            st.subheader("Here is your story:")
            st.write(story)
        else:
            st.warning("Please fill in all the fields to generate the story.")
madlibs_game()