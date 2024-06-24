

import streamlit as st
import pandas as pd

st.title("This is My Special Testing APP!!!")

## session state allows us to keep variables - otherwise the script is reset and run from top to bottom each time
## session state is a special dictionary for persistant variables

if 'counter' not in st.session_state.keys():
    st.session_state['counter'] = 0

if st.button("Click me for balloons"):
    st.balloons()
    st.session_state['counter'] += 1

if st.button("Click me for snow"):
    st.snow()
    st.session_state['counter'] += 1

st.write(f"You've hit a button {st.session_state['counter']} times")

#################################################################################################
#################################################################################################

##  Playing with user inputs

# we can control the title retrospectively
my_title = st.empty()

user_choice = st.radio("Which is best?", options = ['Cats', 'Dogs'])
st.write(f"You have chosen:  {user_choice}")

my_title.title(f"You've picked {user_choice}")

# -----------------------------------------------------------------------------

sweets = st.slider("Please pick best bumber of sweets to eat a day",
        0, 100, step = 10)

if sweets <10:
    st.write("Correct")
elif sweets < 50:
    st.write("Too many")
else:
    st.write("You need help")


# --------------------------------------------------------------------------------------

col1, col2, col3 = st.columns(3)
col1.write("COL1")
col2.write("COL2")
col3.write("COL3")

with col1:
    col1.write("hello")

# -----------------------------------------------------------------------------------------------





