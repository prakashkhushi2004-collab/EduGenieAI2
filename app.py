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
    "explanation": """
# 📘 Introduction to Recursion

The process in which a function calls itself directly or indirectly is called *recursion* and the corresponding function is called a *recursive function*.

• A recursive algorithm takes one step toward the solution and then recursively calls itself to move further.  
• The algorithm stops once we reach the solution.  
• Since a function may call itself again and again, this process might continue forever.  
• So, it is essential to provide a *base case* to terminate recursion.

---

## ⚙️ Steps to Implement Recursion

🔷 *Step 1 – Define a base case*  
Identify the simplest case for which the solution is known.

🔷 *Step 2 – Define recursive case*  
Break problem into smaller subproblems and call recursively.

🔷 *Step 3 – Ensure termination*  
Make sure recursion reaches base case.

🔷 *Step 4 – Combine results*  
Combine subproblem results.

---

## 🧠 Need of Recursion?

• Improves logical thinking  
• Solves complex problems  
• Used in *DP* and *Divide & Conquer*  
• Examples: Trees, Graphs, Backtracking  

---

## 🎯 Example

sum(n) = n + sum(n-1)  
Base Case: n == 1
""",

    "questions": [
        {"id":0,"q":"What is recursion?","opt":{"A":"Function calling itself","B":"Loop only","C":"Conditional statement","D":"Array"},"ans":"A"},
        {"id":1,"q":"What is base case?","opt":{"A":"Start","B":"Stopping condition","C":"Loop","D":"Variable"},"ans":"B"},
        {"id":2,"q":"No base case leads to?","opt":{"A":"Stop","B":"Infinite recursion","C":"Fast","D":"No output"},"ans":"B"},
        {"id":3,"q":"Which data structure is used?","opt":{"A":"Queue","B":"Stack","C":"Heap","D":"Array"},"ans":"B"},
        {"id":4,"q":"Time complexity of Fibonacci (recursive)?","opt":{"A":"O(n)","B":"O(log n)","C":"O(2^n)","D":"O(n^2)"},"ans":"C"},
        {"id":5,"q":"What is tail recursion?","opt":{"A":"Loop","B":"Recursive call at end","C":"Multiple calls","D":"None"},"ans":"B"},
        {"id":6,"q":"Which is NOT suitable for recursion?","opt":{"A":"Tree traversal","B":"Binary search","C":"Simple iteration","D":"Backtracking"},"ans":"C"},
        {"id":7,"q":"Space complexity depends on?","opt":{"A":"O(1)","B":"O(log n)","C":"Recursion depth","D":"O(n^2)"},"ans":"C"},
        {"id":8,"q":"Why recursion is expensive?","opt":{"A":"Stack memory","B":"CPU","C":"Array","D":"No reason"},"ans":"A"},
        {"id":9,"q":"Optimization technique?","opt":{"A":"Loop","B":"Memoization","C":"Sorting","D":"Searching"},"ans":"B"}
    ],

    "plan": [
        "Day 1: Basics (Print, Sum, Factorial)",
        "Day 2: Parameterized & Functional Recursion",
        "Day 3: Arrays & Strings",
        "Day 4: Subsequences",
        "Day 5: Subsets & Combination",
        "Day 6: Backtracking",
        "Day 7: Hard Problems (Sudoku, N-Queens)"
    ]
},

# ================= DBMS =================
"dbms": {
    "explanation": """
# 📘 DBMS (Database Management System)

DBMS is software used to store, manage, and retrieve data efficiently.

---

## 🧠 Why DBMS?

• Avoids data redundancy  
• Ensures data consistency  
• Provides security  
• Supports multiple users  

---

## 📊 Types of DBMS

• Hierarchical  
• Network  
• Relational (RDBMS)  
• NoSQL  

---

## 🎯 Key Concepts

• Table, Row, Column  
• Primary Key  
• Foreign Key  
• Normalization  
• Transactions  

---

## ⚡ Example

A student database storing:
Roll No, Name, Marks
""",

    "questions": [
        {"id":0,"q":"What is DBMS?","opt":{"A":"Software","B":"Hardware","C":"Language","D":"OS"},"ans":"A"},
        {"id":1,"q":"Primary key is?","opt":{"A":"Unique","B":"Duplicate","C":"Null","D":"Optional"},"ans":"A"},
        {"id":2,"q":"DBMS avoids?","opt":{"A":"Redundancy","B":"Speed","C":"Storage","D":"CPU"},"ans":"A"},
        {"id":3,"q":"RDBMS stands for?","opt":{"A":"Relational DBMS","B":"Random DBMS","C":"Real DBMS","D":"None"},"ans":"A"},
        {"id":4,"q":"Foreign key is used for?","opt":{"A":"Relation","B":"Sorting","C":"Delete","D":"None"},"ans":"A"}
    ],

    "plan": [
        "Day 1: Basics of DBMS",
        "Day 2: ER Model",
        "Day 3: SQL Queries",
        "Day 4: Normalization",
        "Day 5: Transactions",
        "Day 6: Indexing",
        "Day 7: Practice Questions"
    ]
},

# ================= OOPS =================
"oops": {
    "explanation": """
# 📘 OOPs (Object Oriented Programming)

OOP is a programming paradigm based on *objects* and *classes*.

---

## 🧱 4 Pillars of OOP

1. *Encapsulation* : Wrapping data & methods together  
2. *Abstraction* : Hiding implementation details  
3. *Inheritance* : Reusing properties of parent class  
4. *Polymorphism* : Same function, different behavior  

---

## 🚀 Benefits

1. Code Reuse  
2. Security  
3. Modularity  
4. Easy Maintenance  

---

## 🎯 Example

Class : Blueprint  
Object : Instance  

Example:  
Car : Class  
BMW : Object
""",

    "questions": [
        {"id":0,"q":"OOP stands for?","opt":{"A":"Object Oriented Programming","B":"Only One Program","C":"Object Oriented Process","D":"None"},"ans":"A"},
        {"id":1,"q":"Which is NOT OOP principle?","opt":{"A":"Encapsulation","B":"Inheritance","C":"Compilation","D":"Polymorphism"},"ans":"C"},
        {"id":2,"q":"Inheritance means?","opt":{"A":"Reuse code","B":"Delete code","C":"Compile","D":"Run"},"ans":"A"}
    ],

    "plan": [
        "Day 1: Basics",
        "Day 2: Classes",
        "Day 3: Inheritance",
        "Day 4: Polymorphism",
        "Day 5: Abstraction",
        "Day 6: Encapsulation",
        "Day 7: Projects"
    ]
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
