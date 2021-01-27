import keras
import tensorflow

def Find_Theme(text):

    model = keras.models.load_model('path/to/location')

    dict_of_words = keras.datasets.reuters.get_word_index()
    print(dict_of_words)
    model.predict()

Find_Theme("")