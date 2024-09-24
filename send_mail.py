import os
import streamlit as st
import smtplib
import ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    app_mail = "gunzeuxapp@gmail.com"

    try:
        password = os.getenv("GA_GEN_PASS")
    except Exception as ex:
        password = st.secrets["GA_GEN_PASS"]

    company_mail = "gunzeux71+app3@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(app_mail, password)
        server.sendmail(app_mail, company_mail, message)
