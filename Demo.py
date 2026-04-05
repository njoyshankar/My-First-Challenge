import streamlit as st

st.set_page_config(page_title="Quiz App", page_icon="🧠")

st.title("🧠 Simple Quiz App")

# ------------------ QUESTIONS ------------------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "Java", "HTML", "All of the above"],
        "answer": "All of the above"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "6"],
        "answer": "8"
    }
]

# ------------------ SESSION STATE ------------------
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0

# ------------------ QUIZ LOGIC ------------------
if st.session_state.current_q < len(questions):

    q = questions[st.session_state.current_q]

    st.subheader(f"Question {st.session_state.current_q + 1}")
    st.write(q["question"])

    selected = st.radio("Choose your answer:", q["options"], key=st.session_state.current_q)

    if st.button("Submit Answer"):
        if selected == q["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")

        st.session_state.current_q += 1
        st.rerun()

# ------------------ RESULT ------------------
else:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your Score: {st.session_state.score} / {len(questions)}")

    if st.button("Restart Quiz"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()