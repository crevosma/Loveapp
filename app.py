import streamlit as st
import random

# Love messages and poems
love_messages = [
    "Your love shines brighter than city lights on a starry night. This connection is something truly special.",
    "A perfect blend of laughter, deep conversations, and shared dreams—this bond is meant to last.",
    "You both complement each other in ways that words cannot express. A love story written in the stars.",
    "Some people spend a lifetime looking for what you two have. Hold onto it, cherish it, and let it grow.",
    "A connection that feels effortless, a love that feels like home—this is what real love looks like.",
]

love_poems = [
    "Two hearts, one rhythm, a love so true,\nEvery day feels like something new.\nIn your laughter, in your touch,\nThis love means so much.",
    "Hand in hand, step by step,\nA journey of love you'll never regret.\nThrough all the seasons, come what may,\nThis love is here to stay.",
    "In morning light and midnight skies,\nYour love is seen through loving eyes.\nA story written, a tale untold,\nA bond so rare, more precious than gold.",
    "Side by side, through thick and thin,\nLove like yours will always win.\nNo distance, no time, no force too strong,\nFor your love will last forever long.",
    "Your love is laughter, your love is grace,\nA warm embrace, a safe place.\nTogether, always side by side,\nA love so strong, so full of pride."
]

# Streamlit Page Configuration
st.set_page_config(page_title="💖 AI Love Predictor 💖", page_icon="💌", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #ffe6f2;
        }
        .main {
            background: linear-gradient(to bottom right, #ffd6e8, #fff5fa);
            border-radius: 15px;
            padding: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2, p {
            font-family: 'Dancing Script', cursive;
            color: #e6005c;
        }
        .stButton>button {
            background-color: #ff3385;
            color: white;
            font-weight: bold;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# App UI
st.title("💌 A Love Test for You 💌")

# Form Inputs
with st.form("love_form"):
    name1 = st.text_input("Your Name")
    name2 = st.text_input("Your Special Someone")
    answer1 = st.text_input("What makes your love special?")

    submitted = st.form_submit_button("💖 Reveal My Love Message 💖")

if submitted:
    message = random.choice(love_messages)
    poem = random.choice(love_poems)

    # Result Display (like an envelope opening)
    st.markdown("""
        <div style='background-color: #ffb3c6; padding: 20px; border-radius: 20px; text-align: center;'>
            <h2>💌 Your Love Letter 💌</h2>
            <p style='font-size: 20px;'>{}</p>
            <p style='font-style: italic; color: #d63384;'>{}</p>
        </div>
    """.format(message, poem), unsafe_allow_html=True)

    # Share Button for WhatsApp
    share_text = f"💌 Love Message 💌\n{name1} & {name2}: {message}\nPoem: {poem}"
    whatsapp_url = f"https://api.whatsapp.com/send?text={share_text}"

    st.markdown(f"[📤 Share on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
