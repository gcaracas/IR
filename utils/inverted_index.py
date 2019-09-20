import re
from utils.preprocessing import preprocessing

class Appearance:
    """
    Represents the appearance of a term in a given document, along with the
    frequency of appearances in the same one.
    """

    def __init__(self, docId, frequency):
        self.docId = docId
        self.frequency = frequency


    def __repr__(self):
        """
        String representation of the Appearance object
        """
        return str(self.__dict__)


class inverted_index:

    def __init__(self, storage=''):
        self.index = {}
        self.storage = storage
        # Let's initialize our own preprocessing module
        self.preprocessing = preprocessing()
        self.preprocessing = preprocessing()

    def __repr__(self):
        """
        String representation of the Database object
        """
        return str(self.index)

    def index_document(self, document=''):
        """
        Process a given document, save it to the DB and update the index.
        """

        # Remove punctuation from the text.
        text = self.preprocessing.remove_punctuation(text=document['text'])

        # Tokenize
        tokens = self.preprocessing.tokenize(text=text)

        # Remove stop words
        tokens = self.preprocessing.remove_stopwords(tokens=tokens)

        # Remove capitalization
        tokens = self.preprocessing.remove_capitalization(tokens=tokens)

        # Stem terms
        tokens = self.preprocessing.stem(tokens=tokens)

        appearances_dict = dict()
        # Dictionary with each term and the frequency it appears in the text.
        for term in tokens:
            term_frequency = appearances_dict[term].frequency if term in appearances_dict else 0
            appearances_dict[term] = Appearance(document['id'], term_frequency + 1)

        # Update the inverted index
        update_dict = {key: [appearance]
        if key not in self.index
        else self.index[key] + [appearance]
                       for (key, appearance) in appearances_dict.items()}
        self.index.update(update_dict)
        # Add the document into the database
        self.storage.add(document)
        return document

    def show_inverted_index(self):
        print(self.index)
        words=list(self.index.keys())
        print("{: >10} {: >10} {: >10} {: >10}".format("Id", 'Term', 'Document', 'Frequency'))
        print('{}'.format('-'*43))
        for id, word in enumerate(words):
            docs = [str(a.docId) for a in self.index[word]]
            docs_str = (str(d) for d in docs)
            docs_flat_list=','.join(docs_str)

            freq = [a.frequency for a in self.index[word]]
            freq_str = (str(d) for d in freq)
            freq_flat_list = ','.join(freq_str)
            print("{: >10} {: >10} {: >10} {: >10}".format(id,word,docs_flat_list, freq_flat_list))
    def lookup_query(self, query):
        """
        Returns the dictionary of terms with their correspondent Appearances.
        This is a very naive search since it will just split the terms and show
        the documents where they appear.
        """
        return {term: self.index[term] for term in query.split(' ') if term in self.index}