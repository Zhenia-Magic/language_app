import streamlit as st
from PIL import Image
import topic_recognition as tr
import grammar_spell as spell_with_grammar_checker

st.title('Typewriter')
img = Image.open("typewriter.png")
st.image(img)
st.subheader('This tool can help assess your English based on your writing. It will also give recommendations on how to improve it.')
option = st.selectbox(
    'Write using the prompt and choose the criterion for evaluation.',
    ['1. Grammar, spelling, and style checker', '2. Lexical complexity ', '3. Level of English'])
my_slot = st.empty()
st.write("Please, fill in the text field with your great writing.")
text = st.text_area(label='writing', value="Type here...")

if option == '1. Grammar, spelling, and style checker':
    spell_with_grammar_checker.example_check(text)
elif option == '2. Lexical complexity':
    st.write('Predicted topic: ', tr.predict_topic(text))
elif option == '3. Level of English':
    pass
