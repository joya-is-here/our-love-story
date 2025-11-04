import streamlit as st
import datetime
from PIL import Image
import random
import time
import json
import requests
from streamlit_lottie import st_lottie


# Page configuration
st.set_page_config(
    page_title="Our Love Story",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with romantic theme
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 12px 28px;
        font-size: 16px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
    }
    .romantic-text {
        font-family: 'Georgia', serif;
        color: #2c3e50;
        text-align: center;
        font-size: 18px;
        line-height: 1.6;
    }
    .heart-animation {
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .special-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 25px;
        margin: 10px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
</style>
""", unsafe_allow_html=True)

# Load Lottie animations
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animations
love_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_CTaize.json")
heart_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ohgwtqbb.json")

# Initialize session state
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0
if 'love_notes' not in st.session_state:
    st.session_state.love_notes = []

def main():
    # Header with animation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<h1 class="heart-animation">💖 Our Special Place 💖</h1>', unsafe_allow_html=True)
        st.markdown('<p class="romantic-text">A digital garden of love, just for you</p>', unsafe_allow_html=True)
    
    # Sidebar with enhanced features
    with st.sidebar:
        st.markdown('<div class="special-card">', unsafe_allow_html=True)
        st.header("🌸 Our Love Stats")
        
        # Anniversary counter
        anniversary = st.date_input("Our Anniversary Date", datetime.date(2023, 1, 1))
        today = datetime.date.today()
        days_together = (today - anniversary).days
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("💕 Days Together", days_together)
        with col2:
            st.metric("🌟 Messages Sent", st.session_state.message_count)
        
        # Love meter (just for fun)
        st.subheader("Our Love Meter")
        love_level = st.slider("How much do you love us today?", 1, 100, 100)
        st.progress(love_level)
        st.write(f"Love Level: {love_level}% 💘")
        
        # Quick mood check
        st.subheader("How are you feeling?")
        mood = st.radio("", ["😔 Sad", "😐 Okay", "😊 Good", "😄 Great", "🤩 Amazing!"], index=2)
        
        st.markdown('</div>', unsafe_allow_html=True)

    # Main content with tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["💌 Sweet Messages", "📸 Memory Lane", "🎵 Our Playlist", "🎮 Fun Together", "📝 Love Notes", "✨ Secret Garden"])

    with tab1:
        display_sweet_messages()
    
    with tab2:
        display_memory_lane()
    
    with tab3:
        display_music_player()
    
    with tab4:
        display_fun_activities()
    
    with tab5:
        display_love_notes()
    
    with tab6:
        display_secret_garden()

def display_sweet_messages():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("💌 Sweet Messages")
        st.write("Whenever you need a little pick-me-up...")
    
    with col2:
        if heart_animation:
            st_lottie(heart_animation, height=100, key="heart")
    
    # Enhanced message database
    sweet_messages = {
        "Comfort": [
            "You are my safe place in this chaotic world 🏡",
            "No matter what happens, we'll face it together 🤝",
            "Your strength inspires me every day 💪",
            "It's okay to not be okay. I'm here 🫂",
            "You are enough, just as you are 🌟"
        ],
        "Love": [
            "My love for you grows stronger every day 🌱",
            "You're the first thing I think of when I wake up ☀️",
            "Being with you feels like home 🏠",
            "You make ordinary moments extraordinary ✨",
            "I fall for you more every single day 💫"
        ],
        "Encouragement": [
            "You are capable of amazing things! 🚀",
            "I believe in you more than you know 💫",
            "Your potential is limitless 🌈",
            "You've got this! And I've got you 💝",
            "Small steps still move you forward 👣"
        ],
        "Funny": [
            "You're the avocado to my toast - basic but perfect 🥑",
            "If you were a vegetable, you'd be a cute-cumber 🥒",
            "You're the WiFi to my internet - can't live without you 📶",
            "We go together like coffee and morning ☕",
            "You're my favorite notification 🔔"
        ]
    }
    
    category = st.selectbox("Choose your vibe:", list(sweet_messages.keys()))
    
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Send Me Love 💝", use_container_width=True):
            message = random.choice(sweet_messages[category])
            st.session_state.message_count += 1
            st.balloons()
            st.success(f"**{message}**")
            st.audio("https://www.soundjay.com/button/beep-07.wav", format='audio/wav')
    
    # Daily affirmation
    st.subheader("🌞 Today's Affirmation")
    affirmations = [
        "I am worthy of love and happiness",
        "I embrace today with an open heart",
        "I choose to see the beauty around me",
        "I am strong, capable, and loved",
        "My heart is full of gratitude"
    ]
    st.info(f"**{random.choice(affirmations)}**")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_memory_lane():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    st.header("📸 Our Memory Lane")
    
    # Photo gallery (placeholder - you can add real images)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("First Date")
        st.image("https://via.placeholder.com/300x200/ff6b6b/white?text=Our+First+Date", use_column_width=True)
        st.caption("That magical coffee shop ☕")
    
    with col2:
        st.subheader("Adventures")
        st.image("https://via.placeholder.com/300x200/4ecdc4/white?text=Our+Adventures", use_column_width=True)
        st.caption("Exploring the world together 🌎")
    
    with col3:
        st.subheader("Cozy Nights")
        st.image("https://via.placeholder.com/300x200/45b7d1/white?text=Cozy+Moments", use_column_width=True)
        st.caption("Movie nights and cuddles 🎬")
    
    # Memory timeline
    st.subheader("📅 Our Timeline")
    memories = [
        {"date": "Jan 1, 2023", "event": "The day we met 💘", "description": "Everything changed"},
        {"date": "Mar 15, 2023", "event": "First trip together ✈️", "description": "So many laughs"},
        {"date": "Jul 4, 2023", "event": "Met each other's families 👨‍👩‍👧‍👦", "description": "They loved you!"},
        {"date": "Dec 25, 2023", "event": "First Christmas 🎄", "description": "Best gift was you"},
    ]
    
    for memory in memories:
        with st.expander(f"{memory['date']} - {memory['event']}"):
            st.write(memory['description'])
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_music_player():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    st.header("🎵 Our Love Playlist")
    
    # Virtual music player
    st.subheader("Songs That Tell Our Story")
    
    love_songs = [
        {"title": "Perfect", "artist": "Ed Sheeran", "emoji": "🎸"},
        {"title": "All of Me", "artist": "John Legend", "emoji": "🎹"},
        {"title": "Thinking Out Loud", "artist": "Ed Sheeran", "emoji": "💃"},
        {"title": "A Thousand Years", "artist": "Christina Perri", "emoji": "⏳"},
        {"title": "You Are The Reason", "artist": "Calum Scott", "emoji": "🌟"}
    ]
    
    for song in love_songs:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{song['emoji']} {song['title']}** - {song['artist']}")
        with col2:
            if st.button("▶️ Play", key=song['title']):
                st.success(f"Now playing: {song['title']} 🎶")
    
    # Add your song feature
    st.subheader("Add Our Song")
    with st.form("add_song"):
        song_name = st.text_input("Song Name")
        artist = st.text_input("Artist")
        why_special = st.text_area("Why this song is special")
        if st.form_submit_button("Add to Our Playlist"):
            st.success(f"Added '{song_name}' to our special playlist! 🎉")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_fun_activities():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    st.header("🎮 Fun Together")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Date Night Ideas")
        activities = [
            "Virtual movie night with sync",
            "Cook the same recipe together",
            "Online puzzle competition",
            "Stargazing video call",
            "Read books to each other"
        ]
        
        selected_activity = st.selectbox("Choose an activity:", activities)
        if st.button("Let's Do This! 🎯"):
            st.success(f"Amazing! Let's {selected_activity.lower()}!")
            st.balloons()
    
    with col2:
        st.subheader("Love Quiz")
        st.write("How well do you know us?")
        
        quiz_questions = [
            "What's my favorite color?",
            "Where was our first date?",
            "What's our song?",
            "What's my dream vacation?"
        ]
        
        with st.form("love_quiz"):
            for i, question in enumerate(quiz_questions):
                st.text_input(f"Q{i+1}: {question}")
            if st.form_submit_button("Submit Answers"):
                st.success("Perfect! Let's compare answers on our next call! 💞")
    
    # Interactive game
    st.subheader("🎲 Would You Rather?")
    questions = [
        "Would you rather have a beach vacation or mountain cabin?",
        "Would you rather watch romance movies or action movies?",
        "Would you rather cook together or order takeout?",
        "Would you rather dance in the rain or watch the sunset?"
    ]
    
    if st.button("New Question"):
        question = random.choice(questions)
        st.info(f"**{question}**")
        st.write("Share your answer! 💭")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_love_notes():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    st.header("📝 Our Love Notes")
    
    # Write a love note
    st.subheader("Write a Love Note")
    with st.form("love_note"):
        note = st.text_area("Pour your heart out...", height=100)
        urgency = st.select_slider("How romantic is this?", ["Sweet", "Loving", "Passionate", "Over-the-moon!"])
        if st.form_submit_button("Send This Note 💘"):
            if note:
                st.session_state.love_notes.append({
                    "note": note,
                    "urgency": urgency,
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                })
                st.success("Love note sent! Your heart has been heard 💞")
    
    # Display previous notes
    st.subheader("Recent Love Notes")
    if st.session_state.love_notes:
        for i, love_note in enumerate(reversed(st.session_state.love_notes[-5:])):
            with st.expander(f"Note {len(st.session_state.love_notes)-i} - {love_note['timestamp']}"):
                st.write(love_note['note'])
                st.caption(f"Romance level: {love_note['urgency']}")
    else:
        st.info("No love notes yet. Write the first one! ✨")
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_secret_garden():
    st.markdown('<div class="special-card">', unsafe_allow_html=True)
    st.header("✨ Our Secret Garden")
    st.write("A special place just for us...")
    
    # Password protected section (simple version)
    password = st.text_input("Enter our secret code:", type="password")
    
    if password == "forever":  # Change this to your actual secret code
        st.success("Welcome to our secret garden! 🌷")
        
        # Special secret features
        st.subheader("🤫 Our Secret Messages")
        
        secret_messages = [
            "You're the reason I believe in soulmates",
            "I still get butterflies when I see you",
            "My favorite sound is your laughter",
            "I love the way your eyes crinkle when you smile",
            "You're my happy thought"
        ]
        
        if st.button("Reveal Secret Message"):
            st.success(f"**{random.choice(secret_messages)}**")
        
        # Future dreams
        st.subheader("🌠 Our Future Dreams")
        dreams = st.text_area("What dreams shall we chase together?")
        if st.button("Seal Our Dreams 🔒"):
            st.balloons()
            st.success("Our dreams are sealed with love! They'll come true! 🌈")
    
    elif password and password != "forever":
        st.error("Hmm, that's not our special code... try again! 💭")
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()