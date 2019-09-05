import nltk
#from nltk.stem.porter import *
from nltk.stem import PorterStemmer

#nltk.download()
class preprocessing:
    def __init__(self):
        print("Preprocessing class")

    def stemmer(self, type=''):
        stemmer = None
        if type == 'porter':
            stemmer = PorterStemmer()
        return stemmer

    def stem(self, stem='', word=''):
        return stem.stem(word)