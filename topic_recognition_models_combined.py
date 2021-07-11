import keras
import os
import re
import nltk
from nltk.corpus import stopwords
import pickle
from keras.preprocessing.sequence import pad_sequences

nltk.download('stopwords')

models = []
onlyfiles = [f for f in os.listdir('topic_recognition_models/')]

for entry in onlyfiles:
    model = keras.models.load_model('topic_recognition_models/' + entry)
    models.append(model)

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def predict_theme(text):
    text = prepare_text(text)
    sequences = tokenizer.texts_to_sequences( [text] )
    seq = pad_sequences(sequences, maxlen=200)
    theme_list = []
    for model in models:
        theme_list.append(model.predict_proba(seq))
    print(theme_list)

def prepare_text(text):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))

    text = text.lower()  # lowercase text
    text = text.replace( "\n", " " )
    text = REPLACE_BY_SPACE_RE.sub( ' ', text )  # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub( '', text )  # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join([word for word in text.split() if word not in STOPWORDS])  # delete stopwors from text
    text = text.strip()
    return text


predict_theme('Hello it is my mother and it is my father. we are family')