import pandas as pd
import numpy as np
import streamlit as st
from textblob import TextBlob
import nltk
nltk.download("punkt")
from __init__ import annotated_text

def compare(text1, text2):
    l1 = text1.split()
    l2 = text2.split()
    correct = 0
    incorrect = 0
    dict_of_incorrect = {}
    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            incorrect += 1
            dict_of_incorrect[l1[i]] = {'correct': l2[i], 'position': i+1}
        else:
            correct += 1
    return (correct, incorrect), dict_of_incorrect

def percentage_of_incorrect(x):
    return (x[1] / (x[0] + x[1])) * 100

def correct_percentage_and_mistakes(text):
    words = nltk.word_tokenize(text)
    text = [word for word in words if word.isalnum()]
    text = " ".join(text)
    text_corrected = TextBlob(text).correct()
    tuple_of_words, dict_of_incorrect = compare(text, text_corrected)
    percentage = percentage_of_incorrect(tuple_of_words)
    return percentage, dict_of_incorrect

def SpellCheck(text):
    p, d= correct_percentage_and_mistakes(text)
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