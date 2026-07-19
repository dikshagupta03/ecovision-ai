import streamlit as st
import pandas as pd
import random

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="EcoVision AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f4f9f4;
}

h1 {
    text-align: center;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- TITLE ----------------

st.title("🌍 EcoVision AI")

st.subheader(
    "Discover your environmental impact and become a greener you! 🌱"
)

st.write(
    "Answer a few questions about your lifestyle and our smart system "
    "will calculate your Eco Score and provide personalized recommendations."
)

st.divider()


# ---------------- SIDEBAR ----------------

st.sidebar.title("🌱 EcoVision AI")

page = st.sidebar.radio(
    "Navigate to:",
    [
        "🏠 Home",
        "🌿 Eco Score Calculator",
        "📊 My Results",
        "🤖 AI Suggestions",
        "🏆 Eco Challenge"
    ]
)


# =====================================================
# HOME
# =====================================================

if page == "🏠 Home":

    st.header("🌎 Welcome to EcoVision AI!")

    st.write(
        "Small actions can create a big difference."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌱 Eco Friendly",
            "Start Today"
        )

    with col2:
        st.metric(
            "♻️ Sustainable",
            "Lifestyle"
        )

    with col3:
        st.metric(
            "🌍 Planet",
            "Needs You"
        )

    st.info(
        "💡 Your goal: Get the highest Eco Score possible!"
    )

    st.markdown(
        """
        ### How it works:

        1. 🌿 Answer questions about your lifestyle.
        2. 📊 Calculate your Eco Score.
        3. 🤖 Get personalized suggestions.
        4. 🏆 Complete eco-friendly challenges.
        """
    )


# =====================================================
# ECO SCORE CALCULATOR
# =====================================================

elif page == "🌿 Eco Score Calculator":

    st.header("🌿 Calculate Your Eco Score")

    st.write(
        "Answer the questions below honestly."
    )

    # Transport

    st.subheader("🚗 1. How do you usually travel?")

    transport = st.selectbox(
        "Choose one:",
        [
            "Walking / Cycling",
            "Public Transport",
            "Electric Vehicle",
            "Car / Bike"
        ]
    )

    # Electricity

    st.subheader("💡 2. How careful are you with electricity?")

    electricity = st.slider(
        "Rate your electricity-saving habits:",
        1,
        10,
        5
    )

    # Water

    st.subheader("💧 3. How do you manage water?")

    water = st.selectbox(
        "Choose one:",
        [
            "I actively save water",
            "I sometimes save water",
            "I don't think about it"
        ]
    )

    # Food

    st.subheader("🍽️ 4. How often do you eat plant-based meals?")

    food = st.slider(
        "Meals per week:",
        0,
        21,
        5
    )

    # Recycling

    st.subheader("♻️ 5. How often do you recycle?")

    recycling = st.radio(
        "Choose one:",
        [
            "Always",
            "Often",
            "Sometimes",
            "Never"
        ]
    )

    # Calculate

    if st.button("🌍 Calculate My Eco Score"):

        score = 0

        # Transport score

        if transport == "Walking / Cycling":
            score += 25

        elif transport == "Public Transport":
            score += 20

        elif transport == "Electric Vehicle":
            score += 15

        else:
            score += 5

        # Electricity

        score += electricity * 2.5

        # Water

        if water == "I actively save water":
            score += 20

        elif water == "I sometimes save water":
            score += 12

        else:
            score += 5

        # Food

        score += (food / 21) * 15

        # Recycling

        if recycling == "Always":
            score += 15

        elif recycling == "Often":
            score += 10

        elif recycling == "Sometimes":
            score += 5

        score = round(score)

        # Save score

        st.session_state["eco_score"] = score

        st.success("Your Eco Score has been calculated! 🌱")

        st.metric(
            "🌍 YOUR ECO SCORE",
            f"{score}/100"
        )

        st.progress(
            min(score / 100, 1.0)
        )

        if score >= 80:

            st.balloons()

            st.success(
                "🌟 Amazing! You are an Eco Champion!"
            )

        elif score >= 60:

            st.info(
                "🌱 Great job! You have a sustainable lifestyle."
            )

        elif score >= 40:

            st.warning(
                "♻️ You're on the right path. "
                "There is room for improvement!"
            )

        else:

            st.error(
                "🌍 Let's work together to make your lifestyle greener!"
            )


# =====================================================
# RESULTS
# =====================================================

elif page == "📊 My Results":

    st.header("📊 Your Eco Dashboard")

    if "eco_score" not in st.session_state:

        st.warning(
            "Please calculate your Eco Score first!"
        )

    else:

        score = st.session_state["eco_score"]

        st.metric(
            "🌱 Your Eco Score",
            f"{score}/100"
        )

        # Data

        categories = [
            "Transport",
            "Energy",
            "Water",
            "Food",
            "Recycling"
        ]

        values = [
            random.randint(50, 100),
            random.randint(40, 100),
            random.randint(40, 100),
            random.randint(40, 100),
            random.randint(50, 100)
        ]

        df = pd.DataFrame(
            {
                "Category": categories,
                "Score": values
            }
        )

        st.subheader("📈 Your Environmental Impact")

        st.bar_chart(
            df.set_index("Category")
        )

        st.write(
            "💡 Focus on improving the categories with the lowest scores."
        )


# =====================================================
# AI SUGGESTIONS
# =====================================================

elif page == "🤖 AI Suggestions":

    st.header("🤖 Personalized Eco Suggestions")

    st.write(
        "Tell us about your biggest environmental challenge."
    )

    problem = st.selectbox(
        "What would you like to improve?",
        [
            "Reduce electricity usage",
            "Save water",
            "Reduce plastic",
            "Use greener transport",
            "Reduce food waste"
        ]
    )

    if st.button("✨ Generate Smart Suggestions"):

        if problem == "Reduce electricity usage":

            st.success(
                "💡 Try switching off unused lights, "
                "using natural light, and unplugging chargers."
            )

        elif problem == "Save water":

            st.success(
                "💧 Take shorter showers, fix leaking taps, "
                "and avoid leaving the tap running."
            )

        elif problem == "Reduce plastic":

            st.success(
                "♻️ Carry reusable bottles and bags "
                "and avoid single-use plastic."
            )

        elif problem == "Use greener transport":

            st.success(
                "🚲 Try walking, cycling, carpooling, "
                "or using public transport when possible."
            )

        else:

            st.success(
                "🍎 Plan meals carefully, store food properly, "
                "and use leftovers creatively."
            )


# =====================================================
# ECO CHALLENGE
# =====================================================

elif page == "🏆 Eco Challenge":

    st.header("🏆 Daily Eco Challenge")

    challenges = [

        "🚶 Walk or cycle instead of using a vehicle today.",

        "💡 Switch off unnecessary lights for the whole day.",

        "💧 Take a shorter shower today.",

        "♻️ Avoid single-use plastic for one day.",

        "🌱 Plant or care for a plant today.",

        "🥗 Try one plant-based meal today.",

        "🛍️ Carry a reusable shopping bag."
    ]

    challenge = random.choice(challenges)

    st.info(
        f"### Today's Challenge:\n\n{challenge}"
    )

    if st.button("✅ I Completed The Challenge"):

        st.balloons()

        st.success(
            "🎉 Amazing! You completed today's Eco Challenge!"
        )

        st.write(
            "Every small action makes a difference. 🌍💚"
        )


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "🌍 EcoVision AI | Created using Python & Streamlit"
)