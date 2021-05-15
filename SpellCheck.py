import streamlit as st
from textblob import TextBlob
import nltk
from spellchecker import SpellChecker
import jamspell

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

def tokenize_input(text):
    words = nltk.word_tokenize(text)
    text = [word for word in words if word.isalnum()]
    return text

def correct_percentage_and_mistakes(text):
    text = tokenize_input(text)
    text = " ".join(text)
    text_corrected = TextBlob(text).correct()
    tuple_of_words, dict_of_incorrect = compare(text, text_corrected)
    percentage = percentage_of_incorrect(tuple_of_words)
    return percentage, dict_of_incorrect

def write_results(text, p, d):
    st.write("Percentage of mistakes: " + str(round(p, 2)) + "%")
    splitted_text = text.split()
    positions_of_incorrect = [i['position'] for i in d.values()]
    for i in range(1, len(splitted_text)+1):
        if not i in positions_of_incorrect:
            splitted_text[i-1] = " " + splitted_text[i-1] + " "
        if i in positions_of_incorrect:
            splitted_text[i-1] = (splitted_text[i-1], "", "#faa")
    l = len(splitted_text) / 13 * 28
    annotated_text(l, *splitted_text)
    st.write("Incorrect Words: ")
    for key, value in d.items():
        annotated_text(35, "The word ", (key, "", "#faa"), " must be written as ", (str(value['correct']), "", "#afa"))

def SpellCheck(text):
    p, d = correct_percentage_and_mistakes(text)
    write_results(text, p, d)

def correct_percentage_and_mistakes_js(text):
    text = tokenize_input(text)
    text = " ".join(text)
    corrector = jamspell.TSpellCorrector()
    corrector.LoadLangModel('en.bin')
    text_corrected = corrector.FixFragment(text)
    tuple_of_words, dict_of_incorrect = compare(text, text_corrected)
    percentage = percentage_of_incorrect(tuple_of_words)
    return percentage, dict_of_incorrect

def Spell_Check_js(text):
    p, d = correct_percentage_and_mistakes_js(text)
    write_results(text, p, d)

def Spell_Check2(text):
    spell = SpellChecker()
    splitted_text = tokenize_input(text)
    misspelled = spell.unknown(splitted_text)
    d = {}
    for word in misspelled:
        for i in range(len(splitted_text)):
            if splitted_text[i].lower() == word:
                index = i+1
        d[word] = {'correct': spell.correction(word),'position': index}
    p = percentage_of_incorrect((len(text.split())-len(misspelled),len(misspelled)))
    write_results(text, p, d)









