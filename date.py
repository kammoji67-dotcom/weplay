import streamlit as st

# 💗 Heart themed background
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    }
    h1, h2, h3, p {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💖 Lucknow Travel Date Planner 💖")
st.write("Plan a cute outing with family 👨‍👩‍👧 or friends 🧑‍🤝‍🧑")

# 🎯 Select type
person_type = st.radio("Who are you going with? 💕", ["Family 👨‍👩‍👧", "Friends 🧑‍🤝‍🧑"])

st.divider()

# 📍 Places data
places = [
    {
        "name": "Bara Imambara 🕌",
        "img": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Bara_Imambara_Lucknow.jpg",
        "special": "Famous for Bhool Bhulaiya maze!"
    },
    {
        "name": "Rumi Darwaza 🏛️",
        "img": "https://upload.wikimedia.org/wikipedia/commons/0/0c/Rumi_Darwaza_Lucknow.jpg",
        "special": "Iconic gateway of Lucknow!"
    },
    {
        "name": "Janeshwar Mishra Park 🌳",
        "img": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Janeshwar_Mishra_Park.jpg",
        "special": "Perfect for picnics & cycling!"
    },
    {
        "name": "Ambedkar Memorial 🏰",
        "img": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Ambedkar_Park_Lucknow.jpg",
        "special": "Grand architecture & evening lights!"
    },
    {
        "name": "Eco Garden 🌿",
        "img": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Eco_Garden_Lucknow.jpg",
        "special": "Relaxing nature + sculptures!"
    }
]

# ☕ Cafes data
cafes = [
    {
        "name": "Cherry Tree Cafe 🍰",
        "img": "https://images.unsplash.com/photo-1559925393-8be0ec4767c8",
        "special": "Cozy vibe & desserts!"
    },
    {
        "name": "Roastery Coffee House ☕",
        "img": "https://images.unsplash.com/photo-1509042239860-f550ce710b93",
        "special": "Premium coffee & aesthetic vibes!"
    },
    {
        "name": "Cafe Repertwahr 🎭",
        "img": "https://images.unsplash.com/photo-1521017432531-fbd92d768814",
        "special": "Art + food combo!"
    }
]

# 🌸 Show places
st.subheader("📍 Best Places in Lucknow")

for place in places:
    st.image(place["img"], use_column_width=True)
    st.markdown(f"### ❤️ {place['name']}")
    st.write(f"✨ {place['special']}")
    st.divider()

# ☕ Show cafes
st.subheader("☕ Cute Cafes in Lucknow")

for cafe in cafes:
    st.image(cafe["img"], use_column_width=True)
    st.markdown(f"### 💕 {cafe['name']}")
    st.write(f"✨ {cafe['special']}")
    st.divider()

# 💡 Suggestion logic
st.subheader("💡 Your Perfect Plan")

if st.button("✨ Suggest My Date Plan ✨"):
    if person_type == "Family 👨‍👩‍👧":
        st.success("""
        💖 Family Plan:
        🌳 Visit park → 🕌 Explore heritage → 🍽️ Eat together  
        Example: Park + Bara Imambara + Cafe  
        """)
    else:
        st.success("""
        💖 Friends Plan:
        📸 Photos + Fun + Cafe hangout  
        Example: Rumi Darwaza + Memorial + Roastery Cafe  
        """)

    st.balloons()
