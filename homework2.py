from preprocesing import *

pre = preprocessing()

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