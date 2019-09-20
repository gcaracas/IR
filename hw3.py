from utils.persist_index_memory import persist_index_memory
from utils.inverted_index import inverted_index

# Make an instance of the class that will hold the data in memory
# this will act as an abstraction layer, to be replaced when
# I need a database due to memory limitations.

memory_unit = persist_index_memory()

# Lets define now our texts.
txt1 = '''
Old-school musical numbers, feisty princesses, funny sidekicks and a mix of action, comedy
and romance come together in Frozen, a Disney animation that works hard to keep everyone
happy.
'''
txt2 = '''
Anyone with an appreciation for old-school musical numbers will find something pleasantly
familiar and cozy about Frozen.
'''
txt3 = '''
Frozen, the new animated film by Disney earns its charms the honest way: with smart
writing and heartfelt performances.
'''
txt4 = '''
 The animation is simply superb. Ice has never looked so good, except as the real thing.
Technical precision and innovation are expected nowadays in computer animation but Frozen
combines that with a gorgeously rich design.
'''
txt5 = '''
 An enjoyable fairy tale romp with some clever plot twists thrown in and positive messages
for young girls that subvert those usually provided by traditional Disney princesses.
'''

# Now let's define our documents with a json structure to facilitate the index creation
doc1 = {'id': 1, 'text': txt1}
doc2 = {'id': 2, 'text': txt2}
doc3 = {'id': 3, 'text': txt3}
doc4 = {'id': 4, 'text': txt4}
doc5 = {'id': 5, 'text': txt5}

# Now let's form our document collection
collection = [doc1, doc2, doc3, doc4, doc5]

inverted_index = inverted_index(memory_unit)

# Now let's process the documents
[inverted_index.index_document(doc) for doc in collection]

inverted_index.show_inverted_index()

inverted_index.create_term_document_matrix()
inverted_index.print_term_document_matrix()

'''
pre = preprocessing()
tokens = pre.tokenize(text=alltext)
print('Tokens = ',len(tokens))
print('Unique words = ',len(list(set(tokens))))
count = Counter(tokens)
print("After tokenizing",count.most_common(10))
tokens = pre.remove_stopwords(tokens=tokens)
count = Counter(tokens)
print('Without stop words, tokens = ',len(tokens))
print('Unique words = ',len(list(set(tokens))))
print("After remove stop words",count.most_common(10))
tokens = pre.remove_capitalization(tokens=tokens)
count = Counter(tokens)
print('After capitalization, tokens = ',len(tokens))
print('Unique words = ',len(list(set(tokens))))
print("After capitalization",count.most_common(10))
tokens = pre.stem(tokens=tokens)
count = Counter(tokens)
print('After lemmatizing, tokens = ',len(tokens))
print('Unique words = ',len(list(set(tokens))))
print("After lemmatizing",count.most_common(10))

'''