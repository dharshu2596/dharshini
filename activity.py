import streamlit as st
import random

# Portfolio Section (Creative Part)
def portfolio():
    st.title("My Portfolio")
    st.header("About Me")
    st.write("Welcome to my creative portfolio! Here, you can learn more about who I am.")
    
    # Add an image or something creative
    st.image("https://via.placeholder.com/300.png?text=My+Picture", caption="Here's a picture of me.")
    
    # Add an interactive text box
    name = st.text_input("Enter your name:", "")
    if name:
        st.write(f"Hello, {name}! Nice to meet you!")
    
    # A little bit about the user
    st.write("""
    I am passionate about creating innovative applications using Python and Streamlit. 
    I enjoy solving challenges and creating meaningful experiences. 
    Let's play a guessing game now!
    """)

# Guessing Game Section
def guessing_game():
    st.title("Guessing Game")
    
    mode = st.radio("Choose your mode:", ["User Guessing", "Machine Guessing"])

    if mode == "User Guessing":
        user_guessing_game()

    elif mode == "Machine Guessing":
        machine_guessing_game()

# User Guessing Game
def user_guessing_game():
    st.subheader("User Guessing Mode")
    st.write("""
    In this mode, the computer will pick a number, and you will try to guess it. 
    You will receive hints if your guess is too high or too low.
    """)
    
    # Dynamic range setting
    lower_limit = st.number_input("Enter the lower limit:", min_value=1, value=1)
    upper_limit = st.number_input("Enter the upper limit:", min_value=1, value=100)

    if lower_limit < upper_limit:
        number_to_guess = random.randint(lower_limit, upper_limit)
        attempts = 0
        max_attempts = int(upper_limit - lower_limit) // 2 + 1

        st.write(f"Try to guess the number between {lower_limit} and {upper_limit}.")

        while True:
            guess = st.number_input(f"Enter your guess (Attempt {attempts + 1}):", min_value=lower_limit, max_value=upper_limit)
            attempts += 1
            if guess < number_to_guess:
                st.write("Too low!")
            elif guess > number_to_guess:
                st.write("Too high!")
            else:
                st.write(f"Correct! You guessed the number in {attempts} attempts.")
                if attempts <= max_attempts:
                    st.write("Great job! You guessed it within the optimal number of attempts!")
                break

            if attempts >= max_attempts:
                st.write(f"Oops! You've reached the maximum number of attempts ({max_attempts}). The number was {number_to_guess}.")
                break
    else:
        st.write("Please make sure the lower limit is less than the upper limit.")

# Machine Guessing Game (Binary Search)
def machine_guessing_game():
    st.subheader("Machine Guessing Mode")
    st.write("""
    In this mode, think of a number in your mind between a given range, 
    and the machine will try to guess it using binary search!
    """)
    
    # Dynamic range setting
    lower_limit = st.number_input("Enter the lower limit:", min_value=1, value=1)
    upper_limit = st.number_input("Enter the upper limit:", min_value=1, value=100)

    if lower_limit < upper_limit:
        st.write(f"Think of a number between {lower_limit} and {upper_limit}, and the machine will try to guess it.")
        st.write("Respond with: 'too high', 'too low', or 'correct' for each guess.")

        low = lower_limit
        high = upper_limit
        attempts = 0

        while low <= high:
            guess = (low + high) // 2
            st.write(f"Is the number {guess}?")
            response = st.radio("What is the response?", ['Too Low', 'Too High', 'Correct'], key=attempts)
            attempts += 1

            if response == "Too Low":
                low = guess + 1
            elif response == "Too High":
                high = guess - 1
            elif response == "Correct":
                st.write(f"The machine guessed your number {guess} in {attempts} attempts!")
                break
    else:
        st.write("Please make sure the lower limit is less than the upper limit.")

# Main app
def main():
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.radio("Choose an option", ["Portfolio", "Guessing Game"])

    if app_mode == "Portfolio":
        portfolio()
    elif app_mode == "Guessing Game":
        guessing_game()

if _name_ == "_main_":
    main()