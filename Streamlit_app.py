import streamlit as st
import SpellCheck as sc
from __init__ import annotated_text

st.title('Writing Aid')
option = st.selectbox(
    'What do you want to do with your text?',
    ['SpellCheck', 'Find Theme'])
st.write("Please, fill in the text field with your great writing.")

text = st.text_area(label='writing', value="Write here...")
p, d= sc.correct_percentage_and_mistakes(text)
st.write("Percentage of mistakes: " + str(round(p, 2)) + "%")
splitted_text=text.split()
positions_of_incorrect = [i['position'] for i in d.values()]
for i in range(1, len(splitted_text)+1):
    if not i in positions_of_incorrect:
        splitted_text[i-1] = " " + splitted_text[i-1] + " "
    if i in positions_of_incorrect:
        splitted_text[i-1] = (splitted_text[i-1], "", "#faa")

annotated_text(*splitted_text)
st.write("Incorrect Words: ")
for key, value in d.items():
    annotated_text("The word ", (key, "", "#faa"), " must be written as ", (str(value['correct']), "", "#afa"))
    #st.markdown("The word "+ key + " must be written as " + str(value['correct']))
