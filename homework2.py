from preprocesing import *
from stats import *
import os
import sys
#from __future__ import division
from itertools import *
from pylab import *
from nltk.corpus import brown
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
    #if count == 10: break
    #print(f)
    f = open(f, "r")
    txt=f.read()
    #print(txt)
    alltext=alltext+txt
print(len(alltext))
pre = preprocessing()
t=pre.tokenizer(type='TweetTokenizer')
s=pre.tokenize(sentence=alltext, tokenizer=t)
print(type(s), len(s))
# The data: token counts from the Brown corpus
tokens_with_count = Counter(s)
counts = array(tokens_with_count.values())
counts = list(counts.tolist())
tokens = tokens_with_count.keys()
print(counts, type(counts))
#asys.exit()
# A Zipf plot
ranks = arange(1, len(counts)+1)
indices = argsort(counts)
print(counts)

#frequencies = counts[indices]
frequencies = sorted(counts, reverse=True)
loglog(ranks, frequencies, marker=".")
title("Zipf plot for Brown corpus tokens")
xlabel("Frequency rank of token")
ylabel("Absolute frequency of token")
grid(True)
#for n in list(logspace(-0.5, log10(len(counts)), 20).astype(int)):
#    dummy = text(ranks[n], frequencies[n], " " + tokens[indices[n]],
#                 verticalalignment="bottom",
#                 horizontalalignment="left")

show()
'''
t=pre.tokenizer(type='TreeBank')
sentence="Jack O'Niel wa"
sentence2="Yesterday's forecast is Today's it was @@@@##$@Great!"
s=pre.tokenize(sentence=sentence, tokenizer=t)
#print(s)
t=pre.tokenizer(type='TweetTokenizer')
s=pre.tokenize(sentence=sentence, tokenizer=t)
#print(s)
t=pre.tokenizer(type='TweetTokenizer2')
s=pre.tokenize(sentence=sentence, tokenizer=t)
#print(s)
t=pre.tokenizer(type='RegexpTokenizer')
print('Sentence 1 = {}'.format(sentence))
s=pre.tokenize(sentence=sentence, tokenizer=t)
print('Tokens = ',s)
print('Sentence 2 = {}'.format(sentence2))
s=pre.tokenize(sentence=sentence2, tokenizer=t)
print('Tokens = ',s)
'''