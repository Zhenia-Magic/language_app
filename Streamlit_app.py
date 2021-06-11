import streamlit as st
import SpellCheck as sc
from PIL import Image
import topic_recognition as tr
import grammar_check as grch

st.title('Typewriter')
img = Image.open("typewriter.png")
st.image(img)
st.subheader('This tool can help enhance your writing.')
option = st.selectbox(
    'What do you want to do with your text?',
    ['Spell check and correction', 'Find Theme', 'Grammar check and correction'])
my_slot = st.empty()
st.write("Please, fill in the text field with your great writing.")
text = st.text_area(label='writing', value="Type here...")

if option == 'Spell check and correction':
    answer = my_slot.radio(
    'Which SpellChecker you want to use?',
    ['Simple', 'Norvig','Jam', "Enchant"])
    if answer == 'Simple':
        sc.SpellCheck(text)
    elif answer == 'Norvig':
        sc.Spell_Check2(text)
    elif answer == 'Enchant':
        sc.spell_check_enchant(text)
    else:
        sc.Spell_Check_js(text)
elif option == 'Find Theme':
    st.write( "Predicted topic: ",tr.predict_topic(text))
elif option == 'Grammar check and correction':
    answer = my_slot.radio(
        'Which Grammar Checker you want to use?',
        ['Language Tool', 'Ginger'] )
    if answer == 'Language Tool':
        grch.grammar_check(text)
    elif answer == 'Ginger':
        grch.grammar_check_ginger( text )

