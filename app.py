
import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(
    page_title="Love Heart ❤️",
    page_icon="❤️",
    layout="wide"
)

# ---------------- PAGE DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background: #050505;
    color: white;
}
header, footer, #MainMenu {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False


# ---------------- NAME DIALOG ----------------

@st.dialog("A Little Surprise For You ❤️")
def name_dialog():

    st.markdown("""
    <h3 style="text-align:center;color:#ff6685;">
        Someone has a surprise for you!
    </h3>
    <p style="text-align:center;color:#aaa;">
        Enter your name to unlock it.
    </p>
    """, unsafe_allow_html=True)

    name = st.text_input(
        "Enter Your Name",
        placeholder="Your name..."
    )

    if st.button("Unlock My Surprise ❤️", use_container_width=True):

        if name.strip().lower() == "zoya":

            st.session_state.unlocked = True
            st.rerun()

        else:

            st.warning("Tarique Only loves Zoya ❤️")


# ---------------- SHOW DIALOG ----------------

if not st.session_state.unlocked:
    name_dialog()


# ---------------- LOVE HEART ----------------

if st.session_state.unlocked:

    st.markdown("""
    <h2 style="
        text-align:center;
        color:#ff6685;
        font-family:cursive;">
        Made With Love For Zoya
    </h2>
    """, unsafe_allow_html=True)

    love_words = [
        "I love you Zoya",
        "Ich liebe dich Zoya",
        "Je t'aime Zoya",
        "Te amo Zoya",
        "Ti amo Zoya",
        "Seni seviyorum Zoya",
        "Aku cinta kamu Zoya",
        "Eu te amo Zoya",
        "愛してる Zoya",
        "사랑해 Zoya",
        "我爱你 Zoya",
        "Я тебя люблю Zoya",
        "Ik hou van jou Zoya",
        "أحبك Zoya",
        "Kocham cię Zoya",
        "Te quiero Zoya",
        "ฉันรักคุณ Zoya",
        "আমি তোমাকে ভালোবাসি Zoya",
        "मैं तुमसे प्यार करता हूँ Zoya"
    ]

    words_json = json.dumps(love_words, ensure_ascii=False)

    html = f"""
    <!DOCTYPE html>
    <html>

    <head>
    <meta charset="UTF-8">

    <style>

    * {{
        box-sizing: border-box;
    }}

    body {{
        margin: 0;
        background: #050505;
        font-family: Arial, sans-serif;
        overflow: hidden;
    }}

    .container {{
        width: 100%;
        min-height: 700px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }}

    /* MAIN HEART - COMPLETELY STATIC */

    .heart {{
        width: min(96vw, 850px);
        display: flex;
        flex-direction: column;
        align-items: center;
        filter: drop-shadow(0 0 9px rgba(255, 40, 85, 0.55));
    }}

    .heart-row {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 29px;
        margin: 1px 0;
    }}

    .lobe-row {{
        justify-content: space-between;
    }}

    .segment {{
        display: flex;
        justify-content: space-around;
        align-items: center;
        gap: 5px;
    }}

    /* INDIVIDUAL WORD ANIMATION */

    .word {{
        color: #ff637d;
        font-size: clamp(7px, 1.2vw, 13px);
        font-weight: bold;
        white-space: nowrap;

        opacity: 0;
        transform: translateY(9px);
        text-shadow: 0 0 8px #ff3158;

        animation: wordAppear 0.65s ease forwards;
        animation-delay: calc(var(--i) * 0.12s);

        transition:
            color 0.3s ease,
            text-shadow 0.3s ease;
    }}

    @keyframes wordAppear {{

        0% {{
            opacity: 0;
            transform: translateY(9px);
            filter: blur(5px);
        }}

        100% {{
            opacity: 1;
            transform: translateY(0);
            filter: blur(0);
        }}

    }}

    /* RANDOM WHITE GLOW */

    .word.flash {{
        color: #ffffff !important;

        text-shadow:
            0 0 5px #ffffff,
            0 0 12px #ffffff,
            0 0 22px #ffffff,
            0 0 35px #ffb6c5;

        filter: brightness(1.5);
    }}

    /* FLOATING BACKGROUND HEARTS */

    .floating {{
        position: fixed;
        bottom: -30px;
        color: #ff3158;
        pointer-events: none;
        animation: floatUp 8s linear infinite;
    }}

    @keyframes floatUp {{

        0% {{
            transform: translateY(0);
            opacity: 0;
        }}

        20% {{
            opacity: 0.7;
        }}

        100% {{
            transform: translateY(-750px);
            opacity: 0;
        }}

    }}

    .message {{
        margin-top: 25px;
        color: #ff7891;
        font-size: 24px;
        font-family: cursive;
        text-shadow: 0 0 12px #ff3158;
    }}

    </style>
    </head>

    <body>

    <div class="container">

        <div class="heart" id="heart"></div>

        <div class="message">
            Forever Yours, Zoya ❤️
        </div>

    </div>


    <script>

    const words = {words_json};

    const heart = document.getElementById("heart");

    let index = 0;

    // Improved symmetrical heart structure

    const shape = [

        {{width: 76, lobes: true, count: 3}},
        {{width: 92, lobes: true, count: 4}},
        {{width: 100, lobes: false, count: 9}},
        {{width: 100, lobes: false, count: 9}},
        {{width: 98, lobes: false, count: 9}},
        {{width: 94, lobes: false, count: 8}},
        {{width: 87, lobes: false, count: 8}},
        {{width: 79, lobes: false, count: 7}},
        {{width: 70, lobes: false, count: 6}},
        {{width: 60, lobes: false, count: 5}},
        {{width: 49, lobes: false, count: 4}},
        {{width: 38, lobes: false, count: 3}},
        {{width: 27, lobes: false, count: 2}},
        {{width: 16, lobes: false, count: 1}},
        {{width: 7, lobes: false, count: 1}}

    ];


    // CREATE HEART ROWS

    shape.forEach((data) => {{

        const row = document.createElement("div");

        row.className = "heart-row";

        row.style.width = data.width + "%";


        // TWO ROUNDED TOP LOBES

        if(data.lobes) {{

            row.classList.add("lobe-row");

            for(let side = 0; side < 2; side++) {{

                const segment = document.createElement("div");

                segment.className = "segment";
                segment.style.width = "45%";

                for(let j = 0; j < data.count; j++) {{

                    const span = document.createElement("span");

                    span.className = "word";

                    span.innerText =
                        words[index % words.length];

                    span.style.setProperty("--i", index);

                    segment.appendChild(span);

                    index++;

                }}

                row.appendChild(segment);

            }}

        }} else {{

            // HEART BODY

            for(let j = 0; j < data.count; j++) {{

                const span = document.createElement("span");

                span.className = "word";

                span.innerText =
                    words[index % words.length];

                span.style.setProperty("--i", index);

                row.appendChild(span);

                index++;

            }}

        }}

        heart.appendChild(row);

    }});


    // RANDOM WHITE GLOW AFTER HEART COMPLETES

    const totalWords = index;

    const totalAnimationTime =
        (totalWords - 1) * 120 + 900;

    setTimeout(() => {{

        const allWords = Array.from(
            document.querySelectorAll(".word")
        );

        function randomGlow() {{

            const randomIndex =
                Math.floor(Math.random() * allWords.length);

            const selectedWord = allWords[randomIndex];

            selectedWord.classList.add("flash");

            setTimeout(() => {{

                selectedWord.classList.remove("flash");

            }}, 650);

        }}

        // Keep randomly highlighting words

        randomGlow();

        setInterval(() => {{

            randomGlow();

        }}, 550);

    }}, totalAnimationTime);


    // FLOATING HEARTS

    for(let i = 0; i < 15; i++) {{

        const floating = document.createElement("div");

        floating.className = "floating";

        floating.innerHTML = "♥";

        floating.style.left =
            Math.random() * 100 + "%";

        floating.style.animationDelay =
            Math.random() * 8 + "s";

        floating.style.fontSize =
            (12 + Math.random() * 20) + "px";

        document.body.appendChild(floating);

    }}

    </script>

    </body>
    </html>
    """

    components.html(
        html,
        height=740,
        scrolling=False
    )

    if st.button("Close Surprise", use_container_width=True):

        st.session_state.unlocked = False
        st.rerun()
