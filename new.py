import streamlit as st
import random
import datetime

# ---- App Config ----
st.set_page_config(page_title="MindEase", layout="wide")

# ---- Data ----
motivation_prompts = [
    "Believe in yourself! You are capable of amazing things.",
    "Every day is a new beginning. Take a deep breath and start again.",
    "Success is the sum of small efforts, repeated daily.",
    "Difficulties in life are intended to make us better, not bitter.",
    "Challenges make life interesting; overcoming them makes life meaningful.",
    "You are stronger than you think. Keep pushing forward!",
    "Your potential is limitless. Keep exploring your capabilities!",
    "Keep going! Everything you need will come at the perfect time.",
    "You are capable, strong, and unstoppable!",
    "Dream big, work hard, and stay positive!"
]

anxiety_relief_prompts = [
    "Take a deep breath. Inhale for 4 seconds, hold for 4, and exhale for 6.",
    "Close your eyes and picture your happy place for a few moments.",
    "Write down what’s bothering you and set it aside for later.",
    "Try progressive muscle relaxation – tense each muscle, then relax it.",
    "Step outside for fresh air or take a short walk.",
    "Hydrate yourself – sometimes, a sip of water helps relax your mind.",
    "Focus on the present: Name 5 things you see and hear right now.",
    "Listen to calming music or nature sounds.",
    "Talk to someone you trust about how you're feeling.",
    "Remind yourself: You have overcome challenges before, and you will again."
]

study_tips = [
    "Use the Feynman technique: Teach what you learn in simple terms.",
    "Try the Pomodoro technique: Study for 25 mins, take a 5-min break.",
    "Summarize notes in your own words for better retention.",
    "Use active recall – test yourself instead of rereading.",
    "Break large tasks into smaller chunks to avoid feeling overwhelmed.",
    "Use mnemonic devices to memorize complex concepts.",
    "Find a distraction-free study environment.",
    "Use visual aids like mind maps and diagrams to retain concepts.",
    "Get enough sleep! Rest is crucial for memory retention.",
    "Stay hydrated and take short breaks to keep your mind fresh."
]

self_care_tips = [
    "Take a 5-minute stretch break to ease muscle tension.",
    "Maintain a good posture while studying to avoid back pain.",
    "Eat brain-boosting foods like nuts, fruits, and dark chocolate.",
    "Avoid excessive caffeine; try herbal tea instead.",
    "Get sunlight exposure to boost your mood and energy levels.",
    "Set realistic goals and celebrate small achievements.",
    "Listen to calming music while studying to reduce stress.",
    "Practice gratitude – write down three things you are grateful for.",
    "Give yourself permission to take breaks without guilt.",
    "Limit screen time before bed to improve sleep quality."
]

emotion_prompts = {
    "Happy": "Keep spreading the joy! Happiness is contagious.",
    "Sad": "It’s okay to feel sad. Take it one step at a time, and be kind to yourself.",
    "Anxious": random.choice(anxiety_relief_prompts),
    "Motivated": "Keep up the great work! Channel your motivation into your goals.",
    "Frustrated": "Take a deep breath. A short break might help clear your mind.",
    "Tired": "Rest is just as important as work. Give yourself a moment to recharge."
}

# ---- Sidebar (MindEase Tools) ----
st.sidebar.title("🧘 MindEase Tools")

if st.sidebar.button("✨ Inspire Me!"):
    st.sidebar.write(random.choice(motivation_prompts))

if st.sidebar.button("😌 Anxiety Relief"):
    st.sidebar.write(random.choice(anxiety_relief_prompts))

if st.sidebar.button("📚 Study Tips"):
    st.sidebar.write(random.choice(study_tips))

if st.sidebar.button("💆‍♀️ Self-Care Tips"):
    st.sidebar.write(random.choice(self_care_tips))

# ---- Main Page ----
st.title("🌿 Welcome to MindEase")
st.subheader("Your personal companion for motivation, study tips, and self-care.")

# ---- Emotion-Based Prompt System ----
st.subheader("🧠 How do you feel today?")
emotion = st.selectbox("", ["Happy", "Sad", "Anxious", "Motivated", "Frustrated", "Tired"])
st.write(emotion_prompts[emotion])

# ---- Interactive Chat Box ----
st.subheader("💬 I am all ears...")
user_input = st.text_input("Tell me more...")

if user_input:
    st.write("That's completely understandable. Would you like to talk about it more?")

# ---- Study Planner Generator ----
st.subheader("📖 Study Planner Generator")

num_subjects = st.selectbox("Number of subjects:", list(range(1, 11)))
subjects = {}

for i in range(1, num_subjects + 1):
    subject_name = st.text_input(f"Subject {i} Name:")
    num_lessons = st.number_input(f"Number of lessons in {subject_name}:", min_value=1, max_value=50, step=1)
    subjects[subject_name] = num_lessons

study_duration = st.number_input("Total study time (in minutes):", min_value=30, step=10)

if st.button("Generate Study Plan"):
    start_time = datetime.datetime.now().replace(second=0, microsecond=0)
    study_plan = []
    time_per_subject = study_duration // num_subjects

    for subject, lessons in subjects.items():
        end_time = start_time + datetime.timedelta(minutes=time_per_subject)
        study_plan.append(f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}: Study {subject} ({lessons} lessons)")
        start_time = end_time

    st.write("### 🕒 Your Study Plan:")
    for entry in study_plan:
        st.write(entry)

# ---- Daily Affirmations ----
st.subheader("🌟 Daily Affirmation")
current_date = datetime.datetime.now().strftime("%B %d, %Y")
affirmation = motivation_prompts[current_date.count("1") % len(motivation_prompts)]
st.write(f"**{current_date}**")
st.write(f"💡 {affirmation}")

# ---- Study Timer ----
st.subheader("⏳ Study Timer")
study_time = st.number_input("Set your study duration (minutes):", min_value=10, max_value=180, step=5)
break_time = st.selectbox("Break duration:", [5, 10])

if st.button("Start Timer"):
    st.write(f"Study for {study_time} minutes, then take a {break_time}-minute break.")

