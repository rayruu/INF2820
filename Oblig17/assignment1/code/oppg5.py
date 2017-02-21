# -*- coding: utf-8 -*-
#Dette er oppgave fem.
#############################################

import nltk
import re

def beskriver(regeksp, ord):
	reg= "^("+regeksp+")$"
	if re.search(reg, ord):
		return True
	else: 
		return False


# kaller og leser fila:
# oppgave a
filename =("Python_INF2820_v2017.txt")
pyt_raw = open(filename).read()

pyt_words1 = pyt_raw.split()
pyt_words2 = nltk.word_tokenize(pyt_raw)
pyt_low = [w.lower() for w in pyt_words2]

print("Oppgave 5a:")
prin+t(pyt_raw[:102])
print("Oppgave 5b:")
print(pyt_words1[:10])
print(pyt_words2[:10])
print("Oppgave 5c: ")
print(pyt_low[:10])

print("Oppgave 5d: ")
pyt_special_words = [word for word in pyt_low if re.search("[æøå]", word)]
print("Bokstavene æøå forekommer %d ganger i pyt_low" %len(pyt_special_words))

print("Oppgave 5e: ")
sp = ["æ","ø","å"]
outfile = open("Norske.txt", "w")
for i in sp:
    teller = 0
    special_word = [word for word in pyt_special_words if re.search(i, word)]
    special_word = sorted(set(special_word))
    print("Bokstavene %s forekommer: %d" %(i, len(special_word)))
    for word in special_word:
        outfile.write("%s\n" %word)
print("Oppgave 5f:")
print("skriver ut til Norske.txt")        
outfile.close()


#oppgave 6 a og b:
reg_stinavn = "^(.*/)([^/]*)$"
reg_num = "^([0-9]+)"
path = "//www.uio.no/studier/emner/matnat/ifi/INF1100/h16/ressurser/installering.html"
        
test = beskriver(reg_stinavn, path)
test_ord = ["hei", "hade", "okei", "//www.uio.no/studier/emner/matnat/ifi/INF1100/h16/ressurser/installering.html", "hei", "0.9", "2", "44"]

pyt_words3 = []
for word in pyt_words2:
    if re.search(reg_stinavn, word):
        pyt_words3.append("<path>")
    elif re.search(reg_num, word):
        pyt_words3.append("<num>")
    else:
        pyt_words3.append(word)

print(pyt_words3)




        
        

    

