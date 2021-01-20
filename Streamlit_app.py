import streamlit as st
import SpellCheck as sc

st.title('Writing Aid')
option = st.selectbox(
    'What do you want to do with your text?',
    ['SpellCheck', 'Find Theme'])
st.write("Please, fill in the text field with your great writing.")

text = st.text_area(label='writing', value="Write here...")
p, d = sc.correct_percentage_and_mistakes(text)
st.write("Percentage of mistakes: " + str(p))
st.write("Incorrect Words: ")
for key, value in d.items():
    st.write("The word "+ key + " at the position " + str(value['position']) + " is incorrect.")
    st.write("Right spelling for this word is " + value['correct'])
st.write(d)