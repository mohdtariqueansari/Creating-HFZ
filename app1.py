import math
import random
import streamlit as st

st.set_page_config(
    page_title="Special Heart for Zoya", page_icon="❤️", layout="centered"
)

# Custom CSS styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .warning-text {
        font-size: 24px;
        color: #ff4b4b;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .success-text {
        font-size: 28px;
        color: #ff69b4;
        font-weight: bold;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("❤️ Special Check ❤️")

user_name = st.text_input("Apna naam darj karein (Enter your name):")

if user_name:
  if user_name.strip().lower() == "zoya":
    st.markdown(
        '<p class="success-text">✨ Zoya detected! Here is your special heart! ✨</p>',
        unsafe_allow_html=True,
    )

    phrases = [
        "I love you",
        "Te amo",
        "Seni seviyorum",
        "Je t'aime",
        "Ich liebe dich",
        "Jag älskar dig",
        "Kocham cię",
        "Aish iteru wa",
        "Ai shiteru",
        "Eu te amo",
        "Obicham te",
        "Te quiero",
        "Mahal kita",
        "Saranghae",
        "Anh yêu em",
    ]

    # Single combined HTML block so Streamlit doesn't break rendering
    heart_html = """
        <div style="position: relative; width: 100%; height: 450px; background-color: #000000; border-radius: 15px; overflow: hidden;">
        <div style="position: absolute; color: #ff69b4; font-family: monospace; width: 100%; height: 100%;">
        """

    random.seed(42)
    for _ in range(50):
      t = random.uniform(0, 2 * math.pi)
      x = 16 * (math.sin(t) ** 3)
      y = -(
          13 * math.cos(t)
          - 5 * math.cos(2 * t)
          - 2 * math.cos(3 * t)
          - math.cos(4 * t)
      )

      left_pos = 50 + x * 2.2
      top_pos = 45 + y * 2.2
      font_size = random.randint(11, 16)
      phrase = random.choice(phrases)

      heart_html += f"""
            <div style="position: absolute; left: {left_pos}%; top: {top_pos}%; font-size: {font_size}px; transform: translate(-50%, -50%); white-space: nowrap;">
                {phrase}
            </div>
            """

    heart_html += """
        </div>
        <div style="position: absolute; bottom: 10px; width: 100%; text-align: center; font-size: 12px; color: #666;">
            Tarique & Zoya ❤️
        </div>
        </div>
        """

    # Rendering the complete block properly with unsafe_allow_html
    st.markdown(heart_html, unsafe_allow_html=True)

  else:
    st.markdown(
        '<p class="warning-text">⚠️ Warning: Tarique only love Zoya ⚠️</p>',
        unsafe_allow_html=True,
    )