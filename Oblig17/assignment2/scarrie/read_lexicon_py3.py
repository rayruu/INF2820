# -*- coding:utf-8 -*-

## Jan Tore Loenning, V2017
##
## This is a program for reading the prepare scary Lexicon into Python 3.
## It assumes that the original ScaryLexicon is already tranformed to the
## form defined by the program scarrie-lexicon, and that it is contained in
## the same folder as the lexicon. The command ScaryLexicon() returns
## the lexicon.
##


class Word:
    """Simple class collecting the different features of a word (form)"""
    
    def __init__(self,ident,form,morf_feat,syn_feat='no_syn_feat'):
        self.ident = ident
        self.form = form
        self.morf_feat = morf_feat
        self.syn_feat = syn_feat  

        
class Lexeme:
    """Class collecting the word identifiers belonging to the same lexeme"""
    
    def __init__(self,ident,word_ids):
        self.ident = ident
        self.word_ids = word_ids
  

class ScaryLexicon(dict):
    """Read in the Scarrie Lexicon in enclosed format.

    First construct a sublexicon corresponding to each file
    Then make a dicionary *words* containing all words from sublexica 
    except affixes and suffixes, and similarly for lexemes.
    """
    
    def __init__(self):
        for (lexicon, i) in zip(['main',
                        'gramwords',
                        'gramwords2x',
                        'idiomwords',
                        'abbrevwords',
                        'prefixes',
                        'suffixes'],
                        ['', 'gr', 'g2', 'idi', 'ab', 'pre', 'suf']):
            self[lexicon]= SubLexicon(lexicon, i)
        self.words =  {k: v for lex in ['main',
                        'gramwords',
                        'gramwords2x',
                        'idiomwords',
                        'abbrevwords']
                        for (k,v) in self[lex].words.items()}
        self.lexemes =  {k: v for lex in ['main',
                        'gramwords',
                        'gramwords2x',
                        'idiomwords',
                        'abbrevwords']
                        for (k,v) in self[lex].lexemes.items()}


class SubLexicon:
    """Read in a sublexicon file in the provided format.

    Store in 2 dictionaries: 
    *words*: a dictionary which maps word identifiers to words
    *lexemes*: a dictionary mapping lexeme ids to lexemes.
    """
    
    def __init__(self, lexicon, sort):
        words = {} 
        lexemes = {}
        lex_nr = -1
        wf_nr = -1
        with open(lexicon, 'r') as infile:
            for line in infile:
                posts = line.strip().split(';')
                if posts[0] == 'Lexeme':
                    # Start a new lexeme
                    lex_nr += 1
                    ident = sort+'x'+str(lex_nr)
                    forms = []   # Identifiers of word forms in this lexeme.
                    # To be filled.
                    this_lexeme = Lexeme(ident, forms)
                    lexemes[ident]=this_lexeme
                else:
                    # Start a new word
                    wf_nr += 1
                    ident = sort+'w'+str(wf_nr)
                    form = posts[0]
                    if len(posts) == 2:
                        posts.append('no_syn_feat')
                        # Some words lack syntactic feature.
                    this_word = Word(ident, form, posts[1], posts[2])
                    # Make new word form. Include current position in word.
                    words[ident]=this_word
                    forms.append(ident)
                    # Put word identifier into the list of its lexeme.
        self.words, self.lexemes = words, lexemes

