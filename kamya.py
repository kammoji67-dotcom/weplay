import streamlit as st
import random

# 🎨 Different backgrounds with animal images
backgrounds = [
    ("#FFD1DC", "https://cdn-icons-png.flaticon.com/512/616/616408.png"),  # dog
    ("#D0F0C0", "https://cdn-icons-png.flaticon.com/512/616/616430.png"),  # cat
    ("#ADD8E6", "https://cdn-icons-png.flaticon.com/512/3069/3069172.png"), # rabbit
    ("#FFFACD", "https://cdn-icons-png.flaticon.com/512/1998/1998610.png"), # bird
]

# Pick random background
bg_color, animal_img = random.choice(backgrounds)

# Apply background
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🐾 Animal Lover Chat 💬")
st.image(animal_img, width=120)
st.write("Ask me anything about pets 🐶🐱🐰🐦")

# Simple chatbot logic
def pet_bot(user_input):
    user_input = user_input.lower()

    if "dog" in user_input:
        return "🐶 Dogs need daily walks, proper food, and lots of love!"
    elif "cat" in user_input:
        return "🐱 Cats love clean spaces, quiet time, and playful toys."
    elif "food" in user_input:
        return "🍖 Pets need balanced food. Avoid giving human junk food!"
    elif "routine" in user_input:
        return "⏰ A good routine includes feeding, playtime, and rest."
    elif "life" in user_input:
        return "❤️ Pets need care, attention, and regular vet checkups."
    elif "bird" in user_input:
        return "🐦 Birds need clean cages, fresh water, and social interaction."
    elif "rabbit" in user_input:
        return "🐰 Rabbits love carrots, leafy greens, and space to hop!"
    elif "care" in user_input:
        return "🩺 Regular grooming, hygiene, and vet visits are important."
    else:
        return "😊 I'm here to help! Ask about pets, food, care, or routines."

# Input box
user_question = st.text_input("💭 Ask your question:")

if st.button("Ask 🐾"):
    if user_question:
        response = pet_bot(user_question)
        st.success(response)
    else:
        st.warning("Please type a question first!")

# Refresh background button
if st.button("🎨 Change Theme"):
    st.rerun()
