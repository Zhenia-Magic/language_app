import streamlit as st
import SpellCheck as sc
from PIL import Image
from topic_recognition import predict_topic

st.title('Typewriter')
img = Image.open("typewriter.png")
st.image(img)
st.subheader('This tool can help enhance your writing.')
option = st.selectbox(
    'What do you want to do with your text?',
    ['Spell checking and correction', 'Find Theme'])
my_slot = st.empty()
st.write("Please, fill in the text field with your great writing.")
text = st.text_area(label='writing', value="Type here...")

if option == 'Spell checking and correction':
    answer = my_slot.radio(
    'Which SpellChecker you want to use?',
    ['Simple', 'Norvig','Jam'])
    if answer == 'Simple':
        sc.SpellCheck(text)
    elif answer == 'Norvig':
        sc.Spell_Check2(text)
    else:
        sc.Spell_Check_js(text)
elif option == 'Find Theme':
    st.write(predict_topic(text))