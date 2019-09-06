import nltk
#from nltk.stem.porter import *
from nltk.stem import PorterStemmer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import RegexpTokenizer

#Taken from nltk tweetertokenizer
# Source: https://www.nltk.org/_modules/nltk/tokenize/casual.html
pattern = r'''(?x)          # set flag to allow verbose regexps
        (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
      | [a-zA-Z]+\'+s       # ap
      | \w+(?:-\w+)*        # words with optional internal hyphens
      | \$?\d+(?:\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
      | \.\.\.              # ellipsis
      | [][.,;"'?():_`-]    # these are separate tokens; includes ], [
    '''

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

    def tokenizer(self, type=''):
        if type == 'TreeBank':
            tokenizer=TreebankWordTokenizer()
        elif type == 'TweetTokenizer':
            tokenizer=TweetTokenizer()
        elif type == 'TweetTokenizer2':
            tokenizer=TweetTokenizer(strip_handles=False, reduce_len=False, preserve_case=False)
        elif type == 'RegexpTokenizer':
            tokenizer=RegexpTokenizer(pattern=pattern)

        return tokenizer

    def tokenize(self, sentence='', tokenizer=None):
        return tokenizer.tokenize(sentence)