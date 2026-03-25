import streamlit as st
import plotly.express as px

# ================= PAGE =================
st.set_page_config(page_title="EduGenie AI", page_icon="✨", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.block-container { padding-top: 2rem; }

.center-box { text-align: center; margin-top: 100px; }

.main-title { font-size: 3.5rem; font-weight: 700; color: #111; }

.subtitle { font-size: 1.3rem; color: #555; margin-top: 10px; margin-bottom: 30px; }

div.stTextInput > div > div > input {
    border-radius: 12px; padding: 12px; border: 1px solid #ddd;
}

div.stButton > button {
    background-color: black; color: white;
    border-radius: 12px; padding: 10px 25px;
    font-size: 16px; margin-top: 15px;
}

.card {
    background: white; padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION =================
if "step" not in st.session_state:
    st.session_state.step = "input"
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "topic" not in st.session_state:
    st.session_state.topic = ""

# ================= TOPICS DATA =================

topics = {

# ================= RECURSION =================
"recursion": {
    "explanation": """# 📘 Recursion
A function calling itself is recursion.

- Needs base case
- Uses stack
- Used in trees, DP

Example:
sum(n) = n + sum(n-1)
""",

    "questions": [
        {"id":0,"q":"What is recursion?","opt":{"A":"Function calling itself","B":"Loop","C":"Array","D":"Variable"},"ans":"A"},
        {"id":1,"q":"Base case means?","opt":{"A":"Start","B":"Stop condition","C":"Loop","D":"None"},"ans":"B"},
        {"id":2,"q":"No base case leads to?","opt":{"A":"Stop","B":"Infinite recursion","C":"Fast","D":"None"},"ans":"B"},
    ],

    "plan": ["Basics", "Parameterized", "Arrays", "Subsequences", "Backtracking", "Hard"]
},

# ================= DBMS =================
"dbms": {
    "explanation": """# 📘 DBMS (Database Management System)

DBMS is software to manage data efficiently.

- Organizes data in tables
- Ensures security & consistency
- Uses SQL

Types:
- Relational DB (MySQL)
- NoSQL (MongoDB)

Key concepts:
- Normalization
- ACID properties
- Transactions
""",

    "questions": [
        {"id":0,"q":"What is DBMS?","opt":{"A":"Database software","B":"Compiler","C":"OS","D":"IDE"},"ans":"A"},
        {"id":1,"q":"Which language used in DBMS?","opt":{"A":"C++","B":"SQL","C":"Java","D":"Python"},"ans":"B"},
        {"id":2,"q":"ACID stands for?","opt":{"A":"Atomicity","B":"Consistency","C":"Isolation","D":"All"},"ans":"D"},
    ],

    "plan": ["Basics", "ER Model", "Normalization", "SQL", "Transactions", "Indexing"]
},

# ================= OOPS =================
"oops": {
    "explanation": """# 📘 OOPs (Object Oriented Programming)

OOP is based on objects & classes.

4 Pillars:
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

Benefits:
- Code reuse
- Security
- Modularity
""",

    "questions": [
        {"id":0,"q":"OOP stands for?","opt":{"A":"Object Oriented Programming","B":"Only One Program","C":"Operating OS","D":"None"},"ans":"A"},
        {"id":1,"q":"Which is NOT OOP principle?","opt":{"A":"Encapsulation","B":"Inheritance","C":"Compilation","D":"Polymorphism"},"ans":"C"},
        {"id":2,"q":"Inheritance means?","opt":{"A":"Reuse code","B":"Delete code","C":"Compile","D":"None"},"ans":"A"},
    ],

    "plan": ["Basics", "Classes", "Inheritance", "Polymorphism", "Abstraction", "Projects"]
}

}

# ================= STEP 1 =================
if st.session_state.step == "input":

    st.markdown('<div class="center-box">', unsafe_allow_html=True)
    st.markdown('<div class="main-title">🚀 EduGenie AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your Personal AI Study Mentor</div>', unsafe_allow_html=True)

    topic = st.text_input("", placeholder="Enter topic (Recursion, DBMS, OOPs)").lower()

    if st.button("Generate"):
        if topic in topics:
            st.session_state.topic = topic
            st.session_state.step = "learn"
        else:
            st.error("❌ Topic not available (Try: recursion, dbms, oops)")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ================= STEP 2 =================
elif st.session_state.step == "learn":
    data = topics[st.session_state.topic]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(data["explanation"])
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🎯 Start Quiz"):
        st.session_state.step = "quiz"
        st.rerun()

# ================= STEP 3 =================
elif st.session_state.step == "quiz":
    data = topics[st.session_state.topic]

    st.subheader("📝 Quiz")

    for q in data["questions"]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.write(f"Q{q['id']+1}: {q['q']}")
        ans = st.radio(
            "Select your answer:",
            list(q["opt"].keys()),
            format_func=lambda x: q["opt"][x],
            key=q["id"],
            index=None
        )
        st.session_state.answers[q["id"]] = ans
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("📊 Submit"):
        score = 0
        for q in data["questions"]:
            if st.session_state.answers.get(q["id"]) == q["ans"]:
                score += 1

        st.session_state.score = score
        st.session_state.step = "analysis"
        st.rerun()

# ================= STEP 4 =================
elif st.session_state.step == "analysis":
    score = st.session_state.score
    total = len(topics[st.session_state.topic]["questions"])

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader(f"🎯 Score: {score}/{total}")
    st.markdown('</div>', unsafe_allow_html=True)

    fig = px.pie(names=["Correct","Wrong"], values=[score,total-score])
    st.plotly_chart(fig)

    if st.button("📅 Study Plan"):
        st.session_state.step = "plan"
        st.rerun()

# ================= STEP 5 =================
elif st.session_state.step == "plan":

    data = topics[st.session_state.topic]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📅 Study Plan")

    for i, day in enumerate(data["plan"],1):
        st.write(f"{i}) {day}")

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 Restart"):
        st.session_state.step = "input"
        st.session_state.answers = {}
        st.rerun()