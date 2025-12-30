import streamlit as st
import random
import string

# ------------------------
# Password generation logic
# ------------------------
def generate_password(limit_letter, limit_num, limit_symbol):
    alpha_random = random.choices(string.ascii_letters, k=limit_letter)
    num_random = random.choices(string.digits, k=limit_num)
    symbol_random = random.choices(string.punctuation, k=limit_symbol)

    password = alpha_random + num_random + symbol_random
    random.shuffle(password)

    return "".join(password)

# ------------------------
# Streamlit UI
# ------------------------
st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("🔐 Password Generator")
st.write("Welcome to the Password Generator! Customize your password below:")

# Dropdown options
options = list(range(0, 21))  # 0 to 20

limit_letter = st.selectbox("How many letters?", options, index=6)
limit_num = st.selectbox("How many numbers?", options, index=2)
limit_symbol = st.selectbox("How many symbols?", options, index=1)

# Generate button
if st.button("Generate Password"):
    if limit_letter == 0 and limit_num == 0 and limit_symbol == 0:
        st.error("Please select at least one character type!")
    else:
        new_password = generate_password(
            limit_letter, limit_num, limit_symbol
        )
        st.success("Password Generated Successfully!")
        st.code(new_password, language="text")
