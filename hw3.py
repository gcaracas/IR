import os
from utils.preprocessing import preprocessing
from utils.persist_index_memory import persist_index_memory
from utils.inverted_index import import inverted_index
from collections import Counter

path = 'data/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

alltext=''
count=0
for f in files:
    count=count+1
    if count == 10: break
    f = open(f, "r")
    txt=f.read()
    alltext=alltext+txt

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

storage