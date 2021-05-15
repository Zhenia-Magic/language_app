import pickle
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.corpus import stopwords

# nltk.download('stopwords')
#file = open("topic_recognition_model.pkl", "rb")
from sklearn.multiclass import OneVsRestClassifier

topic_classifier: OneVsRestClassifier = pickle.load(open("topic_recognition_model1.pkl", "rb"))
#file.close()
vocab = pickle.load(open("topics_vocabulary1.pkl", "rb"))

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
    prediction = topic_classifier.predict(r)
    mlb = pickle.load( open( "binarizer.pkl", "rb" ) )
    prediction = mlb.inverse_transform(prediction)
    prediction = list(set([i[0] for i in prediction if len(i) > 0]))
    return ', '.join(prediction)

print(predict_topic("Education is an important tool which is very useful in everybody’s life. Education is what differentiates us from other living beings on earth. It makes man the smartest creature on earth. It empowers humans and gets them ready to face challenges of life efficiently. With that being said, education still remains a luxury and not a necessity in our country. Educational awareness needs to be spread through the country to make education accessible. But, this remains incomplete without first analyzing the importance of education. Only when the people realize what significance it holds, can they consider it a necessity for a good life. In this essay on Education, we will see the importance of education and how it is a doorway to success."))