import streamlit as st
import random
import datetime

# Motivational Prompts
motivation_prompts = [
    "Believe in yourself! You are capable of amazing things.",
    "Every day is a new beginning. Take a deep breath and start again.",
    "Success is the sum of small efforts, repeated daily.",
    "Keep going. Everything you need will come to you at the perfect time.",
    "Difficulties in life are intended to make us better, not bitter.",
    "You are stronger than you think. Keep pushing forward!",
    "Your potential is limitless. Never stop exploring your capabilities.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "You are capable, you are strong, and you can do this!"
]

# Study Planner Generator with Timestamps
def generate_study_plan(num_subjects, total_minutes):
    start_time = datetime.datetime.now().replace(second=0, microsecond=0)  # Current time
    study_duration = total_minutes // num_subjects  # Time per subject
    plan = []

    for i in range(1, num_subjects + 1):
        end_time = start_time + datetime.timedelta(minutes=study_duration)
        plan.append(f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}: Study Subject {i}")
        start_time = end_time  # Update start time for next subject

    return plan

# Streamlit UI
st.set_page_config(page_title="MindEase", layout="wide")
st.title("🌿 Welcome to MindEase")
st.subheader("Your personal companion for motivation, study tips, and self-care.")

# Study Planner Section
st.subheader("📖 Study Planner Generator")
num_subjects = st.number_input("Number of subjects:", min_value=1, max_value=10, step=1)
total_time = st.number_input("Total study time (minutes):", min_value=30, step=10)

if st.button("Generate Study Plan"):
    study_plan = generate_study_plan(int(num_subjects), int(total_time))
    st.write("### 🕒 Your Study Plan:")
    for entry in study_plan:
        st.write(entry)

# Daily Affirmation
st.subheader("✨ Daily Affirmation")
current_date = datetime.datetime.now().day
affirmation = motivation_prompts[current_date % len(motivation_prompts)]
st.write(affirmation)
