"""
An implementation of nondeterministic finite automata.

It processes NFAs with abreviations and epsilon transitions.

An NFA can be read in from the Python shell by:

>>> nfa1 = NFA(
start=0,
finals=[4],
edges=[
(0,'b',1),
(1,'a',2),
(2,'a',3),
(3,'a',3),
(3,'!',4)
]) 

There is a subclass of NFA which lets one read the NFA from file.
The file should be of the same form as  'template.nfa'
>>> nfa = NFAFromFile('template.nfa')

"""


class NFA:
    """Non-deterministic Finite Automaton

    Class for reprsenting and constructing and NFA.
    Common superclass for reading the automaton from file or entering
    it manually.
    By default it reads from terminal.
    Reading from terminal does not include abreviations.
    Use NFAFromFile class to read from file.
    """
    
    def __init__(self,start=None, finals=None, edges=None):
        """Read in an automaton from python shell"""
        self.start = start
        self.edges = edges
        self.finals = finals
        self.abrs = {}


def add_states(nfa):
    """Adds a set nfa.states to nfa of all the states of the nfa"""
    nfa.states = set([nfa.start]+
                     nfa.finals +
                     [e[0] for e in nfa.edges] +
                     [e[2] for e in nfa.edges ])


def add_epsilon_closure(nfa):
    """Adds ec to nfa where nfa.ec[state] is the epsilon closure of state.
    """
    add_states(nfa)
    nfa.ec = {}
    for state in nfa.states:
        nfa.ec[state] = []
        agenda = [state]
        # The agenda is introduced to make sure that
        # - all states that should be entered to epsilon closure are entered
        # - no states are entered twice. Secures termination.
        # The states that are to be added to epsilon closure
        # is first put into the agenda.
        while len(agenda) > 0:
            next = agenda.pop()
            if next not in nfa.ec[state]:
                #Add it to epsilon closure
                nfa.ec[state].append(next)
                # If there is a jump arc from next to a state
                # put this state in the agenda
                agenda = agenda + [edge[2] for edge in nfa.edges
                                   if edge[0] == next and edge[1] == '#']
                    
        
def nrec(tape, nfa, trace=0):
    """Recognize with epsilon transitions"""
    index = 0
    add_epsilon_closure(nfa)
    states = nfa.ec[nfa.start]
    while True:
        if trace > 0:
            print(" Tape: {}\t States: {}".format(tape[index:], list(states)))
        if index == len(tape): # End of input reached
            successtates = [s for s in states
                              if s in nfa.finals]
            # If this is nonempty return True, otherwise False.
            # This suffices since states is already epsilon closed
            return len(successtates)> 0
        elif len(states) == 0:
            # Not reached end of string, but no states.
            return False
        else:
            # Calculate the new states using epsilon closure.
            edges = set([e for e in nfa.edges
                               if e[0] in states and
                                  (tape[index] == e[1] or
                                     e[1] in nfa.abrs.keys() and
                                     tape[index] in nfa.abrs[e[1]])
                          ])
            states = set([s for e in edges
                            for s in nfa.ec[e[2]]
                          ])
            # Move one step in the string
            index += 1 


class NFAFromFile(NFA):
    """Non-deterministic Finite Automaton

    Read a NFA description from file.
    Build the automaton
    """
    
    def __init__(self, fsa_file):
        """Read in an automaton on the format shown in template.nfa"""
        self.start = None
        self.edges = []
        self.finals = []
        self.abrs = {}
        infile = open(fsa_file, 'r')
        line = infile.readline()
        # self.abrs = {}
        while line:
            if line[0:5] == 'START':
                line = infile.readline()
                self.start = line.split()[0]
                # The first word on the line
                line = infile.readline()
            if line[0:5] == 'FINAL':
                line = infile.readline()
                while len(line)>1:
                    # The final states may be at more than one line
                    # If the next line isn't blank there are more final states
                    symbols = line.split()
                    for word in symbols:
                        self.finals.append(word.strip(','))
                    # The finals may (or may not) be separated by commas.
                    line = infile.readline()
            if line[0:5] == 'EDGES':
                line = infile.readline()
                while len(line)>1:
                    # Each nonblank line contains one edge.
                    triple = line.split()
                    triple[1] = triple[1].strip("'")
                    # Stripping off quotes from the edge symbol.
                    edge = tuple(triple)
                    # Each edge is represented as a triple.
                    self.edges.append(edge)
                    # The edges are stored in the list 'edges'.
                    line = infile.readline()
            if line[0:4] == 'ABRS':
                line = infile.readline()
                while len(line)>1:
                    words = line.split()
                    if words[0][-1]== ':':
                        # First word ends with :
                        # New abreviation
                        abr = words[0][:-1]
                        # Strip the :
                        self.abrs[abr] = []
                        words = words[1:]
                    for word in words:
                        self.abrs[abr].append(word.strip(",'"))
                    line = infile.readline()
            while line and len(line) == 1:
                line = infile.readline()
                # Ignore blank lines.
        infile.close()
        # Always close the file!
        

if(__name__ == "__main__"):
    # test sekvenser:
    words_true = [['tre'],
                  ['halv', 'fem'],
                  ['ti','på','sju'],
                  ['tre', 'over', 'halv', 'åtte'],
                  ['kvart','over','ni'],
                  ['kvart','på','ti']]
    
    words_false = [['halv'],
                   ['kvart', 'på', 'halv','ni'],
                   ['fem','over','kvart','på','ti'],
                   ['ti','på','halv'],
                   ['halv','over','to'],
                   ['halv','på','tolv']]

    nfa = NFAFromFile('oppgave1.nfa')

    print("Tester eksempler fra oppgave 1:")
    print("Skal være med:")
    for sentence in words_true:
        trueOrFalse = nrec(sentence, nfa)
        print('Input is %s' %(trueOrFalse))
        
    print("Skal ikke være med:")
    for sentence in words_false:
        trueOrFalse = nrec(sentence, nfa)
        print('Input is %s' %(trueOrFalse))


""" Run log:

$ python nfa_smart.py 
Tester eksempler fra oppgave 1:
Skal være med:
Input is: True
Input is: True
Input is: True
Input is: True
Input is: True
Input is: True
Skal ikke være med:
Input is: False
Input is: False
Input is: False
Input is: False
Input is: False
Input is: False
"""






