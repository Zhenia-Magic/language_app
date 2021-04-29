import pickle
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords

# nltk.download('stopwords')
#file = open("topic_recognition_model.pkl", "rb")
from sklearn.multiclass import OneVsRestClassifier

topic_classifier: OneVsRestClassifier = pickle.load(open("topic_recognition_model.pkl", "rb"))
#file.close()
vocab = pickle.load(open("topics_vocabulary.pkl", "rb"))

def predict_topic(text):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))

    text = text.lower() # lowercase text
    text = text.replace("\n", " ")
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = [word for word in text.split() if word not in STOPWORDS] # delete stopwors from text

    tfidf_vectorizer = TfidfVectorizer(token_pattern='(\S+)', vocabulary=vocab)
    r = tfidf_vectorizer.fit_transform(text)
    print(tfidf_vectorizer.get_feature_names())
    return topic_classifier.predict(r)

print(predict_topic("Football, also called association football or soccer, game in which two teams of 11 players, using any part of their bodies except their hands and arms, try to maneuver the ball into the opposing team’s goal. Only the goalkeeper is permitted to handle the ball and may do so only within the penalty area surrounding the goal. The team that scores more goals wins."))