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
footer, #MainMenu {
    visibility: hidden;
}
header[data-testid="stHeader"] {
    background: transparent;
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

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>

* { box-sizing: border-box; }

body {
    margin: 0;
    background: #050505;
    font-family: Arial, sans-serif;
    overflow: hidden;
}

.container {
    width: 100%;
    min-height: 860px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

#heart {
    position: relative;
    filter: drop-shadow(0 0 9px rgba(255, 40, 85, 0.5));
}

/* WORDS */

.word {
    position: absolute;
    white-space: nowrap;
    font-weight: bold;
    transform-origin: center;
    opacity: 0;
    animation: wordAppear 0.6s ease forwards;
    transition: color 0.3s ease, text-shadow 0.3s ease;
}

.word.border {
    color: #ff2e63;
    text-shadow: 0 0 10px #ff2e63, 0 0 18px #ff0040;
}

.word.fill {
    color: #ff7a90;
    text-shadow: 0 0 8px #ff3158;
}

@keyframes wordAppear {
    0%   { opacity: 0; filter: blur(5px); }
    100% { opacity: 1; filter: blur(0); }
}

/* RANDOM WHITE GLOW (same as before) */

.word.flash {
    color: #ffffff !important;
    text-shadow:
        0 0 5px #ffffff,
        0 0 12px #ffffff,
        0 0 22px #ffffff,
        0 0 35px #ffb6c5 !important;
}

/* FLOATING BACKGROUND HEARTS */

.floating {
    position: fixed;
    bottom: -30px;
    color: #ff3158;
    pointer-events: none;
    animation: floatUp 8s linear infinite;
}

@keyframes floatUp {
    0%   { transform: translateY(0); opacity: 0; }
    20%  { opacity: 0.7; }
    100% { transform: translateY(-750px); opacity: 0; }
}

.message {
    margin-top: 18px;
    color: #ff7891;
    font-size: 24px;
    font-family: cursive;
    text-shadow: 0 0 12px #ff3158;
}

</style>
</head>

<body>

<div class="container">
    <div id="heart"></div>
    <div class="message">Forever Yours, Zoya ❤️</div>
</div>

<script>
(function () {

const words = __WORDS_JSON__;
const BORDER_WORD = "Zoya";

const wrap = document.getElementById("heart");

const W = Math.min(window.innerWidth || 860, 860);
const H = Math.round(W * 0.92);
wrap.style.width  = W + "px";
wrap.style.height = H + "px";

const borderFont = Math.max(10, W * 0.02);
const fillFont   = Math.max(7,  W * 0.0135);

// ---------- text measuring ----------

const mctx = document.createElement("canvas").getContext("2d");

function measure(text, size) {
    mctx.font = "bold " + size + "px Arial";
    return mctx.measureText(text).width;
}

// ---------- PERFECT HEART CURVE ----------

const N = 1600;
const raw = [];

for (let i = 0; i <= N; i++) {
    const t = (i / N) * Math.PI * 2;
    raw.push({
        x: 16 * Math.pow(Math.sin(t), 3),
        y: 13 * Math.cos(t) - 5 * Math.cos(2 * t) - 2 * Math.cos(3 * t) - Math.cos(4 * t)
    });
}

let xmin = Infinity, xmax = -Infinity, ymin = Infinity, ymax = -Infinity;
raw.forEach(p => {
    xmin = Math.min(xmin, p.x); xmax = Math.max(xmax, p.x);
    ymin = Math.min(ymin, p.y); ymax = Math.max(ymax, p.y);
});

const scale = Math.min((W * 0.86) / (xmax - xmin), (H * 0.86) / (ymax - ymin));
const mx = (xmin + xmax) / 2;
const my = (ymin + ymax) / 2;

const P = raw.map(p => ({
    x: W / 2 + (p.x - mx) * scale,
    y: H / 2 - (p.y - my) * scale
}));

// cumulative length
const cum = [0];
for (let i = 1; i < P.length; i++) {
    cum.push(cum[i - 1] + Math.hypot(P[i].x - P[i - 1].x, P[i].y - P[i - 1].y));
}
const L = cum[cum.length - 1];

function posAt(d) {
    let lo = 0, hi = cum.length - 1;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (cum[mid] < d) lo = mid + 1; else hi = mid;
    }
    const i = Math.max(1, Math.min(P.length - 2, lo));
    const a = P[Math.max(0, i - 3)];
    const b = P[Math.min(P.length - 1, i + 3)];
    return {
        x: P[i].x,
        y: P[i].y,
        angle: Math.atan2(b.y - a.y, b.x - a.x) * 180 / Math.PI
    };
}

function addWord(text, x, y, angle, cls, size, delay) {
    const span = document.createElement("span");
    span.className = "word " + cls;
    span.innerText = text;
    span.style.fontSize = size + "px";
    span.style.left = x + "px";
    span.style.top = y + "px";
    span.style.transform = "translate(-50%, -50%) rotate(" + angle + "deg)";
    span.style.animationDelay = delay + "s";
    wrap.appendChild(span);
}

// ---------- STEP 1 : BORDER (Zoya, one by one) ----------

const bw = measure(BORDER_WORD, borderFont);
const baseGap = borderFont * 0.45;
const nBorder = Math.floor(L / (bw + baseGap));
const step = L / nBorder;
const BORDER_DELAY = 0.055;

for (let k = 0; k < nBorder; k++) {
    const d = step * k + step / 2;
    const p = posAt(d);
    let a = p.angle;
    if (a > 90 || a < -90) a += 180;     // keep text readable
    addWord(BORDER_WORD, p.x, p.y, a, "border", borderFont, k * BORDER_DELAY);
}

const borderTotal = nBorder * BORDER_DELAY + 0.6;

// ---------- STEP 2 : FILL (top -> bottom) ----------

const inset = borderFont * 1.5 + fillFont * 0.6;
const shrink = 1 - inset / (W * 0.43);

const Q = P.map(p => ({
    x: W / 2 + (p.x - W / 2) * shrink,
    y: H / 2 + (p.y - H / 2) * shrink
}));

let yTop = Infinity, yBottom = -Infinity;
Q.forEach(p => { yTop = Math.min(yTop, p.y); yBottom = Math.max(yBottom, p.y); });

const rowH = fillFont * 1.6;
const FILL_DELAY = 0.045;
const heartChar = "♥";

let idx = 0;
let order = 0;

for (let y = yTop + rowH / 2; y < yBottom - rowH * 0.3; y += rowH) {

    // find where this row is inside the heart
    const xs = [];
    for (let i = 0; i < Q.length - 1; i++) {
        const a = Q[i], b = Q[i + 1];
        if ((a.y <= y && b.y > y) || (b.y <= y && a.y > y)) {
            xs.push(a.x + (y - a.y) * (b.x - a.x) / (b.y - a.y));
        }
    }
    xs.sort((m, n) => m - n);

    for (let s = 0; s + 1 < xs.length; s += 2) {

        const pad = fillFont * 0.4;
        const x1 = xs[s] + pad;
        const x2 = xs[s + 1] - pad;
        const avail = x2 - x1;

        if (avail < fillFont) continue;

        const items = [];
        let total = 0;
        const minGap = fillFont * 0.7;

        while (true) {
            const t = words[idx % words.length];
            const w = measure(t, fillFont);
            const need = total + (items.length ? minGap : 0) + w;
            if (need > avail) break;
            items.push({ t: t, w: w });
            total += (items.length > 1 ? minGap : 0) + w;
            idx++;
        }

        if (items.length === 0) {
            const hw = measure(heartChar, fillFont);
            if (avail >= hw) items.push({ t: heartChar, w: hw });
        }

        if (items.length === 0) continue;

        const sumW = items.reduce((acc, it) => acc + it.w, 0);
        let gap = items.length > 1 ? (avail - sumW) / (items.length - 1) : 0;
        gap = Math.min(gap, fillFont * 2.2);

        const groupW = sumW + gap * (items.length - 1);
        let cx = x1 + (avail - groupW) / 2;

        items.forEach(it => {
            addWord(
                it.t,
                cx + it.w / 2,
                y,
                0,
                "fill",
                fillFont,
                borderTotal + 0.3 + order * FILL_DELAY
            );
            cx += it.w + gap;
            order++;
        });
    }
}

// ---------- STEP 3 : RANDOM WHITE GLOW (same as before) ----------

const totalAnimationTime = (borderTotal + 0.3 + order * FILL_DELAY + 0.7) * 1000;

setTimeout(() => {

    const allWords = Array.from(document.querySelectorAll(".word"));

    function randomGlow() {
        const el = allWords[Math.floor(Math.random() * allWords.length)];
        el.classList.add("flash");
        setTimeout(() => el.classList.remove("flash"), 650);
    }

    randomGlow();
    setInterval(randomGlow, 550);

}, totalAnimationTime);

// ---------- FLOATING HEARTS ----------

for (let i = 0; i < 15; i++) {
    const f = document.createElement("div");
    f.className = "floating";
    f.innerHTML = "♥";
    f.style.left = Math.random() * 100 + "%";
    f.style.animationDelay = Math.random() * 8 + "s";
    f.style.fontSize = (12 + Math.random() * 20) + "px";
    document.body.appendChild(f);
}

})();
</script>
</body>
</html>
"""

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
    html = HTML_TEMPLATE.replace("__WORDS_JSON__", words_json)

    components.html(
        html,
        height=880,
        scrolling=False
    )

    if st.button("Close Surprise", use_container_width=True):
        st.session_state.unlocked = False
        st.rerun()