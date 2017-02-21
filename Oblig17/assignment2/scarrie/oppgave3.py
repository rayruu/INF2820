from read_lexicon_py3 import *

sclex = ScaryLexicon()

def analyze(ids, words):
    a = []
    for id in ids:
        wf = words[id]
        morf = wf.morf_feat.split(",")
        syn = wf.syn_feat.split("_")
        print(morf)
        print(syn)
        #a.append("id: %s \n Morfologi: %s \n Syntaks: %s" 
        #         %(id, wf.morf_feat, wf.syn_feat))
        a = ""
    return a
   

#oppgave 3a:
word = ["kaster", "kastet", "noen", "et"]

# sort out forms from id key
words = sclex.words
id_keys = words.keys()

form_to_ids = {}
#set up a new dictionary with format as key and append id
for id in id_keys:
    form = sclex.words[id].form
    form_to_ids.setdefault(form, [])
    form_to_ids[form].append(id)

# print out ids, morfologi and syntax:
for w in word:
    ids = form_to_ids[w]
    print("\nskriver ut identifickatorene til %s" %w) 
    print(ids)
    analyse = analyze(ids, words)
    [print(string) for string in analyse] 

""" run log:
$ python3 oppgave3.py

skriver ut identifickatorene til kastet
['w140111', 'w140108', 'w140109', 'w140079', 'w140110']
id: w140111 
 Morfologi: V,pret 
 Syntaks: V_pret_indic_active_main_ditrans!intrans!trans
id: w140108 
 Morfologi: Adj,pos,indef,sg,part 
 Syntaks: Adj_mfn_pos_indef_sg
id: w140109 
 Morfologi: V 
 Syntaks: V_pastpart_indic_passive_main_dummysubj!intrans!trans
id: w140079 
 Morfologi: N,sg 
 Syntaks: N_n_sg_def
id: w140110 
 Morfologi: V 
 Syntaks: V_pastpart_indic_active_main_ditrans!intrans!trans

skriver ut identifickatorene til øyne
['w341904', 'w341666']
id: w341904 
 Morfologi: V,inf 
 Syntaks: V_inf_indic_active_main_trans
id: w341666 
 Morfologi: N,pl,indef 
 Syntaks: N_n_pl_indef

"""

#oppgave 3b:

"""
V,pres V_pres_indic_active_main_ditrans!intrans!trans
- Beskriver: V, pres beskriver de morfologiske egenskapene: Verb og presens
- V_pres_indic_active_main_ditrans!intrans!trans breskriver syntaksen

N,pl,indef N_m_pl_indef
- N, pl, indef beskriver de morfologiske egenskapene: Noun-subjekt, pl-flertall, indef-udefinert
- N_m_pl_indef beskriver syntaksen

N,sg,indef N_m_sg_indef
- Beskriver at det er et subjekt, entall og udefinert.
- N_m_sg_indef og de andre oppsumerer id'n, altså syntaksen til ordet.
"""

#oppgave 3c:

"""

"""
