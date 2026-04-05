import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

# --- STATE ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- FUNCTIONS ---
def press(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# --- FORCE DARK BACKGROUND ---
st.markdown("""
    <style>
    .stApp {
        background-color: black;
    }

    /* DISPLAY */
    .display {
        color: white;
        font-size: 70px;
        text-align: right;
        padding: 20px 10px;
    }

    /* BUTTON BASE */
    div.stButton > button {
        height: 80px;
        font-size: 28px;
        border-radius: 40px;
        border: none;
        width: 100%;
    }

    /* NUMBER BUTTONS */
    .num button {
        background-color: #333333;
        color: white;
    }

    /* FUNCTION BUTTONS (AC, %, +/-) */
    .func button {
        background-color: #a5a5a5;
        color: black;
    }

    /* OPERATOR BUTTONS */
    .op button {
        background-color: #ff9500;
        color: white;
    }

    /* REMOVE EXTRA SPACE */
    .block-container {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- DISPLAY ---
st.markdown(f"<div class='display'>{st.session_state.expression or 0}</div>", unsafe_allow_html=True)

# --- LAYOUT ---
layout = [
    [("AC","func"), ("+/-","func"), ("%","func"), ("/","op")],
    [("7","num"), ("8","num"), ("9","num"), ("*","op")],
    [("4","num"), ("5","num"), ("6","num"), ("-","op")],
    [("1","num"), ("2","num"), ("3","num"), ("+","op")],
    [("0","num"), (".","num"), ("=","op")]
]

# --- BUTTON GRID ---
for row in layout:
    cols = st.columns(len(row), gap="small")
    for i, (label, cls) in enumerate(row):
        with cols[i]:
            st.markdown(f"<div class='{cls}'>", unsafe_allow_html=True)

            if label == "AC":
                st.button(label, on_click=clear, use_container_width=True)
            elif label == "=":
                st.button(label, on_click=calculate, use_container_width=True)
            elif label == "+/-":
                if st.button(label, use_container_width=True):
                    if st.session_state.expression.startswith("-"):
                        st.session_state.expression = st.session_state.expression[1:]
                    else:
                        st.session_state.expression = "-" + st.session_state.expression
            else:
                st.button(label, on_click=press, args=(label,), use_container_width=True)

            st.markdown("</div>", unsafe_allow_html=True)