import streamlit as st

# 🎨 Page config
st.set_page_config(page_title="Personality Test 💖")

# 🌸 Custom pink background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffc0cb;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 Fun Personality Test 💖")
st.write("Answer these questions to discover your personality! 😊")

# Questions
questions = [
    ("1. What do you enjoy most?", ["Reading 📚", "Partying 🎉", "Gaming 🎮", "Traveling ✈️"]),
    ("2. How do you react to stress?", ["Stay calm 😌", "Talk to friends 🗣️", "Ignore it 😐", "Get anxious 😰"]),
    ("3. Your ideal weekend?", ["Relax at home 🏠", "Go out 🛍️", "Try something new 🌟", "Sleep 😴"]),
    ("4. Pick a color:", ["Blue 💙", "Red ❤️", "Yellow 💛", "Black 🖤"]),
    ("5. You prefer:", ["Planning 📅", "Going with flow 🌊", "Leading 👑", "Following 👥"]),
    ("6. Your social style:", ["Introvert 🤫", "Extrovert 😄", "Ambivert 😎", "Depends 🤔"]),
    ("7. Favorite activity:", ["Music 🎵", "Sports ⚽", "Art 🎨", "Technology 💻"]),
    ("8. Decision making:", ["Logical 🧠", "Emotional ❤️", "Quick ⚡", "Slow 🐢"]),
    ("9. You value:", ["Honesty 🤝", "Success 🏆", "Fun 🎈", "Peace ☮️"]),
    ("10. Your energy level:", ["High 🔥", "Medium ⚡", "Low 🌙", "Varies 🌈"])
]

answers = []

# Display questions
for i, (q, options) in enumerate(questions):
    answer = st.radio(q, options, key=i)
    answers.append(answer)

# Submit button
if st.button("✨ Show My Personality ✨"):
    score = len(set(answers))  # simple logic

    st.subheader("🌟 Your Result:")

    if score <= 3:
        st.success("😌 You are Calm & Thoughtful!")
    elif score <= 6:
        st.success("😎 You are Balanced & Adaptable!")
    else:
        st.success("🔥 You are Energetic & Adventurous!")

    st.balloons()
