from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

class preprocessing:
    def __init__(self):
        self.stemer = PorterStemmer()
        self.tokenizer = TweetTokenizer()

    def stem(self, tokens=''):
        return [self.stemer.stem(w) for w in tokens]

    def tokenize(self, text=''):
        return self.tokenizer.tokenize(text)

    def remove_stopwords(self, tokens=[]):
        stop_words = set(stopwords.words('english'))
        return [w for w in tokens if not w in stop_words]

    def remove_capitalization(self, tokens=[]):
        return [w.lower() for w in tokens]