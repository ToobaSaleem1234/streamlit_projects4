import streamlit as st
import os
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the web app
st.title("My Streamlit Python Website")

# Sidebar navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choose a section", ["Home", "About", "User Input", "Data Visualization", "File Upload"])

# Home Section
if app_mode == "Home":
    st.subheader("Welcome to My Professional Python Website!")
    st.status("Explore my skills, projects, and expertise in Python development.")

    # Skills Section with Progress Bars
    st.header("My Skills")
    
    st.subheader("Python Programming")
    st.progress(90)
    
    st.subheader("Game Development")
    st.progress(80)
    
    st.subheader("Data Science & Visualization")
    st.progress(70)
    
    st.subheader("Web Development")
    st.progress(60)
    
    
    # Recent Projects Section
    st.header("Recent Projects")
    
    st.write("Here are a few of the projects I've been working on:")
    
    # Project 1: Password Strength Checker
    st.subheader("Password Strength Checker")
    st.write("""
        A tool built using Python that analyzes the strength of a password based on length, character variety, and complexity. 
        It provides feedback on how to strengthen a password and secure it against common attacks.
    """)
    
    # Project 2: Personal Library Management
    st.subheader("Personal Library Management")
    st.write("""
        A personal library management system where users can add, remove, and search for books. It helps track reading progress and organizes books by author, title, and genre.
    """)
    
    # Project 3: Growth Mindset Challenge
    st.subheader("Growth Mindset Challenge")
    st.write("""
        A motivational app that provides daily challenges aimed at fostering a growth mindset. Users can track their progress 
        and achieve goals related to personal development and learning.
    """)
    
    # Project 4: BMI Calculator
    st.subheader("BMI Calculator")
    st.write("""
        A simple web app that allows users to input their height and weight to calculate their Body Mass Index (BMI). It provides 
        health-related feedback based on BMI categories.
    """)
    
    # Project 5: Number Guessing Game
    st.subheader("Number Guessing Game")
    st.write("""
        A fun number guessing game where the player has to guess a randomly generated number within a specified range. 
        It provides feedback on whether the guess is too high or too low until the correct number is guessed.
    """)
    
    # Project 6: Countdown Timer
    st.subheader("Countdown Timer")
    st.write("""
        A countdown timer application that allows users to set a timer for a specified amount of time. The timer will count down and notify the user when the time is up.
    """)
    
    # Project 7: Hangman Game
    st.subheader("Hangman Game")
    st.write("""
        A word guessing game where players try to guess the word by suggesting letters. If the player guesses wrong too many times, they lose. It’s a classic game that tests both vocabulary and strategy.
    """)

    # Call to Action Section
    st.write("---")
    st.header("Let's Connect!")
    st.write("I'm always open to new opportunities and collaborations. Feel free to reach out to me via email or social media!")
    
    # Contact Button
    if st.button("Contact Me"):
        st.write("You can reach me at: saleemtooba365@gmail.com")
        st.write("Follow me on [LinkedIn](https://www.linkedin.com) and [GitHub](https://github.com/ToobaSaleem1234)")
    
# About Section
elif app_mode == "About":
    st.header("About Me")
    st.button("Hi, I am Tooba Saleem, a student of GIAIC and a future passionate developor with 2 years of experience in IT.My exprties lies in HTML,Custom CSS,Tailwind CSS,Typescript UI/UX Design for web Development.")
    st.button("I believe in blending different creativity with functionality to deliever meaningful results.Every project I made with so much effort and hardworking.These all projects are the the part of my learning journey.Every project i work on is a chance to push boundaries and explore innovative solutions.")
    st.button("My expertise also lies in Python, and I have a strong passion for building various projects using this powerful language. Over the years, I've developed several games, ranging from simple text-based ones to interactive graphical games. My experience also extends to data analysis, web development, and automation, where I’ve created impactful solutions for real-world problems.")
    st.button("I enjoy creating data-driven web applications for various purposes.In this demo website, you can interact with different sections.")
    st.info("Feel free to explore and have fun!")

# User Input Section (Registration Form)
elif app_mode == "User Input":
    st.header("User Registration Form")
    # User input
    full_name = st.text_input("Full Name", "")
    email = st.text_input("Email", "")
    password = st.text_input("Password", type="password")
    age = st.number_input("Age", min_value=1, max_value=100)
    gender = st.radio("Gender", ("Male", "Female"))
    country = st.selectbox("Country", ["Pakistan","USA", "India", "UK", "Canada", "Australia", "Other"])
    agree = st.checkbox("I agree to the terms and conditions.")
    # Submit Button
    if st.button("Submit"):
        if agree:
            st.success("Registration Successful!")
            st.info(f"Name: {full_name}")
            st.info(f"Email: {email}")
            st.info(f"Age: {age}")
            st.info(f"Gender: {gender}")
            st.info(f"Country: {country}")
        else:
            st.warning("Please agree to the terms and conditions to submit the form.")

# Data Visualization Section
elif app_mode == "Data Visualization":
    st.header("Simple Data Visualization")
    st.write("Below is a simple plot showing a sine wave.")
    
    # Generate sine wave data

    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave", color="blue")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_title("Sine Wave Plot")
    ax.legend()

    st.pyplot(fig)

# File Upload Section (allowing any file type)
elif app_mode == "File Upload":
    st.header("Upload Any File")
    st.caption("You can upload any file, including Python files, or drag and drop files here!")

    # File uploader allowing any file type (no restriction on file types)
    uploaded_file = st.file_uploader("Choose a file", type=None)
    
    if uploaded_file is not None:
        # Temporary saving the uploaded file locally
        with open("uploaded_file", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Button to display the uploaded file content
        if st.button("Upload File"):
            file_name = uploaded_file.name
            file_content = uploaded_file.read()
            
            # Display file details
            st.subheader(f"File name: {file_name}")
            st.subheader(f"File size: {len(file_content)} bytes")
            
            # If the file is a Python file, show the content (or any other file type handling as needed)
            if file_name.endswith(".py"):
                st.success("Python file content:")
                st.code(file_content.decode(), language="python")
            
            else:
                st.write("File content preview (first 200 characters):")
                st.text(file_content[:200].decode(errors="ignore"))
            
            # Download Button for the uploaded file
            if st.button("Download File"):
                with open("uploaded_file", "rb") as f:
                    st.download_button(
                        label="Download File",
                        data=f,
                        file_name=file_name,
                        mime="application/octet-stream"
                    )
