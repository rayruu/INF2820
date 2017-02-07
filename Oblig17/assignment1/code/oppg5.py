# -*- coding: utf-8 -*-
#Dette er oppgave fem.
#############################################

import nltk

# kaller og leser fila:
# oppgave a
filename =("Python_INF2820_v2017.txt")
pyt_raw = open(filename).read()

pyt_words1 = pyt_raw.split()
pyt_words2 = nltk.word_tokenize(pyt_raw)
pyt_low = [w.lower() for w in pyt_words2]

print("Oppgave 5a:")
print(pyt_raw[:102])
print("Oppgave 5b:")
print(pyt_words1[:10])
print(pyt_words2[:10])
print("Oppgave 5c: ")
print(pyt_low[:10])


