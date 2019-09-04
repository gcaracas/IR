import nltk
from nltk.stem.porter import *
nltk.download()
class preprocessing:
    def __init__(self):
        print("hello")

    def stemmer(self, type=''):
        stemmer = None
        if type == 'porter':
            stemmer = PorterStemmer()

        return stemmer