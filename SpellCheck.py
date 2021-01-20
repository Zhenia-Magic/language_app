import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk
nltk.download("punkt")

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
