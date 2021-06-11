import language_tool_python
import streamlit as st
from language_tool_python import Match
from textblob import TextBlob
import nltk
from gingerit.gingerit import GingerIt

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
    st.write("Incorrect: ")
    for key, value in d.items():
        annotated_text(35, (key, "", "#faa"), " must be written as ", (str(value['correct']), "", "#afa"))

s = "I was delighted to read you're letter last week. Its always a pleasure to recieve the latest news and to here that you and your family had a great summer. We spent last week at the beach and had so much fun on the sand and in the water exploring the coast we weren't prepared for the rains that came at the end of the vacation. The best parts of the trip was the opportunities to sightsee and relax. My kids are back in school to. I find their are less things to worry about now that the kids are at school all day. There is plenty of fun things to do in the summer, but by August, I've running out of ideas. I've excepted the fact that we'll have to think up brand-new activities next summer; hoping to round up some creative ideas soon."
# tool = language_tool_python.LanguageTool('en-US')
# is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and \
#                                rule.replacements[0][0].isupper()
# matches = tool.check(s)
# r = 8
# # matches = [rule for rule in matches if not is_bad_rule(rule)]
# print(len(matches))
# print(matches)





def grammar_check(text: str):
    tool = language_tool_python.LanguageTool('en-US')
    splitted_text = text.split() #tokenize_input(text)
    is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and \
                               rule.replacements[0][0].isupper()
    matches = tool.check(text)
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    # return matches
    print(matches)
    d = {}
    # index = -1
    for match in matches:

        mistake_word = text[match.offset:match.offset + match.errorLength]
        for i in range(len(splitted_text)):
            if splitted_text[i].lower() == mistake_word.lower():
                index = i+1

        d[mistake_word] = {'correct':  match.replacements[0],'position': index}
    # p = percentage_of_incorrect((len(text.split())-len(matches),len(matches)))

    print(d)
    p = 0
    write_results(text, p, d)


def grammar_check_ginger(text: str):
    splitted_text = text.split() #tokenize_input(text)
    #is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and \rule.replacements[0][0].isupper()
    parser = GingerIt()
    print(parser.parse(splitted_text))
""" 
    matches = [rule for rule in matches if not is_bad_rule(rule)]
    # return matches
    print(matches)
    d = {}
    # index = -1
    for match in matches:

        mistake_word = text[match.offset:match.offset + match.errorLength]
        for i in range(len(splitted_text)):
            if splitted_text[i].lower() == mistake_word.lower():
                index = i+1

        d[mistake_word] = {'correct':  match.replacements[0],'position': index}
    # p = percentage_of_incorrect((len(text.split())-len(matches),len(matches)))
"""
    #print(d)
    #p = 0
    #write_results(text, p, d)
