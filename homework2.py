from preprocesing import *

pre = preprocessing()
stem = pre.stemmer(type='porter')
res=pre.stem(stem=stem, word='Abandon')
print(res)
res=pre.stem(stem=stem, word='abandonment')
print(res)