import streamlit as st
from dotenv import load_dotenv
import os
from google import genai


# =========================================================
#                  LOAD GEMINI API
# =========================================================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


# =========================================================
#                  PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Lumi AI",
    page_icon="🦊",
    layout="centered"
)


# =========================================================
#                       CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       OCTONAUTS BACKGROUND
       ===================================================== */

    .stApp {

        background-image:
            linear-gradient(
                rgba(240, 250, 248, 0.72),
                rgba(255, 239, 248, 0.76)
            ),
            url("https://m.media-amazon.com/images/M/MV5BYmU1M2YzYjItODU3NS00YjRiLWE2YTMtMDI5NDE5MTRiNjQxXkEyXkFqcGdeQXVyNzU1NzE3NTg@._V1_.jpg");

        background-size: cover;

        background-position: center;

        background-attachment: fixed;

        min-height: 100vh;
    }


    /* =====================================================
       HIDE DEFAULT STREAMLIT UI
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* =====================================================
       MAIN CONTAINER
       ===================================================== */

    .block-container {

        max-width: 820px;

        padding-top: 3rem;

        padding-bottom: 4rem;
    }


    /* =====================================================
       TITLE
       ===================================================== */

    h1 {

        text-align: center !important;

        font-size: 48px !important;

        font-weight: 800 !important;

        letter-spacing: 1px;

        color: #315d68 !important;

        text-shadow:
            0 3px 10px
            rgba(255,255,255,0.95);

        animation:
            titleFloat 3s ease-in-out infinite;
    }


    @keyframes titleFloat {

        0%, 100% {
            transform: translateY(0);
        }

        50% {
            transform: translateY(-6px);
        }
    }


    /* =====================================================
       SUBTITLE
       ===================================================== */

    .stApp p {

        color: #526c70;

        font-size: 17px;

        text-align: center;
    }


    /* =====================================================
       ANIMAL EMOJIS
       ===================================================== */

    .stMarkdown {

        text-align: center;
    }


    /* =====================================================
       REMOVE TEXT AREA LABEL
       ===================================================== */

    .stTextArea label {

        display: none !important;
    }


    /* =====================================================
       TEXT AREA
       ===================================================== */

    .stTextArea textarea {

        background:
            rgba(255, 255, 255, 0.86) !important;

        color:
            #40565b !important;

        border:
            2px solid
            rgba(150, 205, 205, 0.80) !important;

        border-radius:
            22px !important;

        padding:
            18px !important;

        font-size:
            16px !important;

        line-height:
            1.6 !important;

        box-shadow:
            0 10px 30px
            rgba(55, 130, 135, 0.18) !important;

        backdrop-filter:
            blur(8px);

        transition:
            all 0.35s ease !important;
    }


    /* =====================================================
       TEXT AREA HOVER
       ===================================================== */

    .stTextArea textarea:hover {

        border-color:
            #77c5c7 !important;

        transform:
            translateY(-2px);

        box-shadow:
            0 14px 35px
            rgba(55, 130, 135, 0.25) !important;
    }


    /* =====================================================
       TEXT AREA FOCUS
       ===================================================== */

    .stTextArea textarea:focus {

        border-color:
            #5eb3b8 !important;

        outline:
            none !important;

        box-shadow:
            0 0 0 4px
            rgba(94,179,184,0.16),

            0 14px 35px
            rgba(55, 130, 135, 0.24) !important;
    }


    /* =====================================================
       PLACEHOLDER
       ===================================================== */

    .stTextArea textarea::placeholder {

        color:
            #8ca5a8 !important;

        opacity:
            1 !important;
    }


    /* =====================================================
       GENERATE BUTTON
       ===================================================== */

    .stButton > button {

        width:
            100% !important;

        min-height:
            55px !important;

        border:
            none !important;

        border-radius:
            20px !important;

        padding:
            14px 20px !important;

        margin-top:
            10px !important;

        font-size:
            17px !important;

        font-weight:
            700 !important;

        color:
            white !important;

        background:
            linear-gradient(
                135deg,
                #67c8c5,
                #8fcfd0,
                #e5a9c4
            ) !important;

        box-shadow:
            0 10px 25px
            rgba(60, 150, 155, 0.28);

        transition:
            all 0.3s ease !important;
    }


    /* =====================================================
       BUTTON HOVER
       ===================================================== */

    .stButton > button:hover {

        transform:
            translateY(-4px)
            scale(1.015);

        box-shadow:
            0 16px 35px
            rgba(60, 150, 155, 0.38);

        background:
            linear-gradient(
                135deg,
                #55bdbb,
                #82c7c9,
                #dc96b6
            ) !important;
    }


    /* =====================================================
       BUTTON CLICK
       ===================================================== */

    .stButton > button:active {

        transform:
            scale(0.97);
    }


    /* =====================================================
       SUCCESS MESSAGE
       ===================================================== */

    .stSuccess {

        border-radius:
            17px !important;

        background:
            rgba(224, 249, 237, 0.90) !important;

        border:
            1px solid
            rgba(105, 190, 145, 0.45) !important;
    }


    /* =====================================================
       WARNING MESSAGE
       ===================================================== */

    .stWarning {

        border-radius:
            17px !important;

        background:
            rgba(255, 244, 218, 0.90) !important;
    }


    /* =====================================================
       SPINNER
       ===================================================== */

    .stSpinner > div {

        border-top-color:
            #62bfc0 !important;
    }


    /* =====================================================
       RESPONSE HEADING
       ===================================================== */

    h3 {

        color:
            #315d68 !important;

        text-align:
            center !important;

        margin-top:
            25px !important;

        padding:
            13px;

        border-radius:
            18px;

        background:
            rgba(255,255,255,0.72);

        box-shadow:
            0 8px 22px
            rgba(60,130,140,0.14);

        animation:
            responseAppear 0.6s ease;
    }


    /* =====================================================
       RESPONSE ANIMATION
       ===================================================== */

    @keyframes responseAppear {

        from {

            opacity: 0;

            transform:
                translateY(15px);
        }

        to {

            opacity: 1;

            transform:
                translateY(0);
        }
    }
    /* Response area */
div[data-testid="stMarkdownContainer"] {
    animation: fadeIn 0.8s ease-in-out;
}

    /* Floating animal */
.animal {
    position: fixed;
    font-size: 30px;
    z-index: 999;
    pointer-events: none;
    animation: floatanimal 8s linear infinite;
    opacity: 0.75;
}

.animal1 {
    left: 5%;
    top: 85%;
    animation-delay: 0s;
}
.animal2 {
    left: 18%;
    top: 90%;
    animation-delay: 2s;
    font-size: 24px;
}
.animal3 {
    left: 80%;
    top: 88%;
    animation-delay: 1s;
    font-size: 28px;
}
.animal4 {
    left: 92%;
    top: 75%;
    animation-delay: 3s;
    font-size: 22px;
}
.animal5 {
    left: 50%;
    top: 95%;
    animation-delay: 4s;
    font-size: 25px;
}
/* Floating animal animation */
@keyframes floatanimal {

    0% {
        transform: translateY(0px) rotate(0deg);
        opacity: 0;
    }

    20% {
        opacity: 0.8;
    }

    50% {
        transform: translateY(-250px) rotate(180deg);
        opacity: 0.9;
    }

    80% {
        opacity: 0.7;
    }

    100% {transform: translateY(-550px) rotate(360deg);
        opacity: 0;
    }
}

/* Fade animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}


    /* =====================================================
       MOBILE
       ===================================================== */

    @media (max-width: 700px) {

        .block-container {

            padding-left:
                18px;

            padding-right:
                18px;
        }

        h1 {

            font-size:
                38px !important;
        }

        .stApp p {

            font-size:
                15px;
        }

        .stTextArea textarea {

            font-size:
                15px !important;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<div class="animal animal1">🐰</div>
<div class="animal animal2">🐻</div>
<div class="animal animal3">🐻‍❄️</div>
<div class="animal animal4">🐨</div>
<div class="animal animal5">🐼</div>
""", unsafe_allow_html=True)

# =========================================================
#                  TITLE
# =========================================================

st.title(" CORAL AI 🐻")


# =========================================================
#                  SUBTITLE
# =========================================================

st.write(
    "🐻‍❄️Your pawsome little AI buddy 🐾🐶"
)



# =========================================================
#                  PROMPT BOX
# =========================================================

prompt = st.text_area(
    "",
    placeholder="🐧Let’s explore something new....",
    height=150,
    label_visibility="collapsed"
)


# =========================================================
#                  GENERATE RESPONSE
# =========================================================

if st.button("🐻 Coral is ready to explore your questions!🐼"):

    if prompt:

        with st.spinner("🐻 CORAL AI is thinking... "):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success(
            "Your response is ready!🐾🗣🐰"
        )


        st.write(
            response.text
        )

    else:

        st.warning(
            "Please enter something first! 🗣 "
        )








