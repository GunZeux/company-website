import streamlit as st
import pandas as pd
from send_mail import send_mail

df = pd.read_csv("topics.csv")
st.title("Contact Us")
with st.form(key="send_message"):
    user_mail = st.text_input("E-Mail")
    option = st.selectbox("what topic do you want to discuss",
                          df["topic"])
    raw_text = st.text_area("Enter message")

    submit = st.form_submit_button("Submit")

    if submit:
        message = f"""\
        Subject = New {option} from {user_mail}

From {user_mail}
{raw_text}"""

        send_mail(message)

        st.info("e-mail sent successfully".title())

