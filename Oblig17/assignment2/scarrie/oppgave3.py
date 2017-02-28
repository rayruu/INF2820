from read_lexicon_py3 import *

sclex = ScaryLexicon()

def analyze3a(ids, words, word):
    a = []
    for id in ids:
        wf = words[id]
        morf = wf.morf_feat.split(",")
        syn = wf.syn_feat.split("_")
        a.append(" %s \n id: %s \n Morfologi: %s \n Syntaks: %s" 
                 %(word, id, wf.morf_feat, wf.syn_feat))
    return a

def analyze3c(ids, words, word):
    a = []
    for id in ids:
        wf = words[id]
        morf = wf.morf_feat.split(",")
        syn = wf.syn_feat.split("_")
        
        if syn[0] == "N":
            s1, s2, s3, s4 = syn
            # cat_gen_num_def
            a.append(" %s \n cat: %s \n gen: %s \n num: %s \n def: %s \n"
                     %(word, s1, s2, s3, s4))
        elif syn[0] == "V":
            s1, s2, s3, s4, s5, s6 = syn
            s6 = s6.split("!")
            s6 = " eller ".join(s6)
            # cat_form_modus_group_type_subCat
            a.append(" %s \n cat: %s \n form: %s \n modus: %s \n group: %s \n type: %s \n subCat: %s \n"
                     %(word, s1, s2, s3, s4, s5, s6))
        elif syn[0] == "Det":
            s1, s2, s3, s4, s5 = syn
            # cat_gen_num_def_type
            a.append(" %s \n cat: %s \n gen: %s \n num: %s \n def %s \n type: %s \n"
                     %(word, s1, s2, s3, s4, s5))
    return a
   

#oppgave 3a:
wordsToAnalysea = ["kastet", "øyer"]
wordsToAnalysec = ["kaster", "kastet", "noen", "et"]

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
for word in wordsToAnalysea:
    ids = form_to_ids[word]
    print("\nskriver ut identifikatorene til %s" %ids) 
    analyse = analyze3a(ids, words, word)
    [print(string) for string in analyse] 

""" run log:
$ python3 oppgave3.py

skriver ut identifikatorene til ['w140110', 'w140109', 'w140111', 'w140079', 'w140108']
 kastet 
 id: w140110 
 Morfologi: V 
 Syntaks: V_pastpart_indic_active_main_ditrans!intrans!trans
 kastet 
 id: w140109 
 Morfologi: V 
 Syntaks: V_pastpart_indic_passive_main_dummysubj!intrans!trans
 kastet 
 id: w140111 
 Morfologi: V,pret 
 Syntaks: V_pret_indic_active_main_ditrans!intrans!trans
 kastet 
 id: w140079 
 Morfologi: N,sg 
 Syntaks: N_n_sg_def
 kastet 
 id: w140108 
 Morfologi: Adj,pos,indef,sg,part 
 Syntaks: Adj_mfn_pos_indef_sg

skriver ut identifikatorene til ['w341585', 'w341659', 'w341664']
 øyer 
 id: w341585 
 Morfologi: N,pl,indef 
 Syntaks: N_f_pl_indef
 øyer 
 id: w341659 
 Morfologi: V,pres 
 Syntaks: V_pres_indic_active_main_trans
 øyer 
 id: w341664 
 Morfologi: N,pl,indef 
 Syntaks: N_n_pl_indef

"""
#oppgave 3b:

"""
kaster:
V,pres V_pres_indic_active_main_ditrans!intrans!trans
- Beskriver: V, pres beskriver de morfologiske egenskapene: Verb og presens
- V_pres_indic_active_main_ditrans!intrans!trans breskriver syntaksen:
  kaster er av indiktiv modus og et aktivt hovedverb i presens. 
  Det er også et ditransitiv eller intransitiv eller transitiv verb
  som betyr at det kan brukes alene eller med ett eller flere objekter

kaster:
N,pl,indef N_m_pl_indef
  - N, pl, indef beskriver de morfologiske egenskapene: 
    Noun-substantiv, pl-flertall, indef-ubestemt
  - N_m_pl_indef beskriver syntaksen:
    Beskriver da at ordet er subjektiv med mengde: flertall og ubestemt

kaster
N,sg,indef N_m_sg_indef
  - N, sg, indef beskriver de morforlogiske egenskapene:
    Substantiv, entall, ubestemt
  - N_m_sg_indef beskriver syntaksen:
    Beskriver da at ordet er subjektiv med mengde: entall og ubestemt.

V - verb
pres - presens
indic - indikativ - betyr verbet brukes i utsagn om det faktiske
def - bestemt
indef - ubestemt
pl - flertall (plural)
sg - entall   (singular)
"""
#oppgave 3c:
print("############################################################")
print("##################### oppgave 3c ###########################")
print("############################################################")

for word in wordsToAnalysec:
    ids = form_to_ids[word]
    analyse = analyze3c(ids, words, word)
    [print(string) for string in analyse] 

"""
$ python3 oppgave3.py
   ....
   ....
 Syntaks: N_f_pl_indef
############################################################
##################### oppgave 3c ###########################
############################################################
kaster 
 cat: N 
 gen: m 
 num: sg 
 def: indef 

 kaster 
 cat: V 
 form: pres 
 modus: indic 
 group: active 
 type: main 
 subCat: ditrans eller intrans eller trans 

 kaster 
 cat: N 
 gen: m 
 num: pl 
 def: indef 

 kastet 
 cat: N 
 gen: n 
 num: sg 
 def: def 

 kastet 
 cat: V 
 form: pastpart 
 modus: indic 
 group: active 
 type: main 
 subCat: ditrans eller intrans eller trans 

 kastet 
 cat: V 
 form: pastpart 
 modus: indic 
 group: passive 
 type: main 
 subCat: dummysubj eller intrans eller trans 

 kastet 
 cat: V 
 form: pret 
 modus: indic 
 group: active 
 type: main 
 subCat: ditrans eller intrans eller trans 

 noen 
 cat: Det 
 gen: mfn 
 num: pl 
 def indef 
 type: quant 

 et 
 cat: V 
 form: pres 
 modus: imp 
 group: active 
 type: main 
 subCat: accinf eller intrans eller objacomp eller ref eller trans 

 et 
 cat: Det 
 gen: n 
 num: sg 
 def indef 
 type: quant 
"""
