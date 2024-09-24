import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")
st.set_page_config(layout="wide")

st.title("The Best Company")
content = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut porta sem eget sagittis maximus. 
Nullam sed felis a erat vestibulum maximus. Vivamus id diam leo. Vestibulum id libero accumsan, vulputate 
sapien quis, porta mauris. Sed a egestas urna, vitae venenatis ipsum. Nullam suscipit nibh non enim posuere 
malesuada. Mauris a semper ex, porttitor vulputate ex. Nunc luctus eget justo et vestibulum. Aenean augue 
lacus, tincidunt vel vulputate sed, convallis ac lacus. Ut in diam eu arcu tincidunt vulputate. Suspendisse 
eget nibh vel magna dapibus tincidunt ac convallis neque. Etiam pretium in dolor nec vestibulum.

Sed non nisi leo. Proin et feugiat augue, non tempus enim. Integer ut cursus lectus. 
Sed maximus diam tempus luctus semper. Aliquam vulputate eleifend sapien. Cras non odio in urna malesuada 
aliquet. Morbi nec libero sed quam laoreet bibendum. Proin id interdum eros, non bibendum nisl. Interdum et 
malesuada fames ac ante ipsum primis in faucibus. Vestibulum mi magna, congue sit amet hendrerit pellentesque, 
pulvinar et felis. Etiam non fringilla nisl, et tempor turpis. Duis velit enim, volutpat ut ante sed, efficitur 
pretium nisl. Fusce dapibus tincidunt nunc. Sed et iaculis est. Suspendisse nec fringilla velit, sed aliquet risus.

Sed a posuere risus. Duis efficitur, odio vel rutrum bibendum, dui nisi lacinia est, at efficitur mi leo 
at libero. Duis convallis sapien diam, ut rhoncus arcu finibus sit amet. Nulla tempor dictum mi, et sodales 
risus laoreet vel. Morbi consequat erat ligula. Donec lobortis lacus eleifend purus fringilla molestie. 
Nam nec orci maximus turpis ornare ornare non a dolor."""

st.write(content)
st.header("Our Team", )

col1, col2, col3 = st.columns([1,1,1])

with col1:
    for index, row in df[:4].iterrows():
        st.header(F"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(F"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.header(F"{row['first name']} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/"+row["image"])

