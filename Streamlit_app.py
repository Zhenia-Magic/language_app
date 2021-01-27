import streamlit as st
import SpellCheck as sc
import keras

st.title('Writing Aid')
option = st.selectbox(
    'What do you want to do with your text?',
    ['SpellCheck', 'Find Theme'])
st.write("Please, fill in the text field with your great writing.")
text = st.text_area(label='writing', value="Write here...")

if option == 'SpellCheck':
    sc.SpellCheck(text)
elif option == 'Find Theme':