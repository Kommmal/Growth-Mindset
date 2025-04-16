import streamlit as st
import random
from quotes import quotes

# Page title
st.set_page_config(page_title="Growth Mindset App", page_icon="🌱")

# Title
st.title("🌱 Growth Mindset Tracker")
st.write("Welcome! This app will help you build a positive and strong mindset through reflection and learning.")

# Ask for user's name
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hi {name}, let's start growing! 💪")

    # 1. Set Learning Goals
    st.header("🎯 Set a Learning Goal")
    learning_goal = st.text_input("What is one skill or topic you want to learn?")
    if st.button("Save Goal"):
        st.success(f"Great goal, {name}! Keep working on: {learning_goal}")

    # 2. Reflect on Your Learning
    st.header("✍️ Reflect on Your Learning")
    reflection = st.text_area("What did you learn today? Did you face any challenges? How did you handle them?")
    if st.button("Save Reflection"):
        st.success("Reflection saved! You're doing great!")

    # 3. Seek Feedback
    st.header("📢 Feedback Section")
    feedback = st.text_area("Write any feedback or suggestions you received from teachers, friends, or others:")
    if st.button("Save Feedback"):
        st.info("Thanks! Feedback is a great way to improve.")

    # 4. Stay Positive
    st.header("😊 Stay Positive!")
    positive_messages = [
        "You are growing every day!",
        "Mistakes help you learn.",
        "Your effort matters more than perfection.",
        "Believe in yourself and keep going!",
        "Challenges help you become stronger."
    ]
    st.success(random.choice(positive_messages))

    # Motivation Quote of the Day
    st.header("💬 Quote of the Day")
    st.info(random.choice(quotes))



else:
    st.warning("Please enter your name to begin.")

