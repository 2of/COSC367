import re
from search import *


def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


class KBGraph(Graph):
    def __init__(self, kb, query):
  
    
        self.query = query
        
        ''' A little conversion just to make it ez'''
        self.clauses = {}
        self.final_nodes = []
        for each in list(clauses(kb)): 
            if each[0] in self.clauses: 
                self.clauses[each[0]].append(each[1])
                continue
            if each[1] == []: 
                self.final_nodes.append(each[1])
            self.clauses[each[0]] = [each[1]]
        '''Dictionary lookups amirite'''
            

        '''
            Arc(tail=(), head=(), action='-', cost=0)
        
        
        
        each 'node id ' is just a tuple with all perdicates ~
        
        
        for each arc, replace each of the predicates with their derivatives.
        
        
        
        end if node is nothing
        
        
        
        also cancel if iff node ! in set. 
        
        '''

    def starting_nodes(self):
 
        return [''.join(self.query)]
        
    def is_goal(self, node):
        " ** COMPLETE ** "
     #   print(f" is {node} a goal? ")
        if node == '':
            return True
        return False
        
        
        
    def slowdupscheck(self,x):
        '''Convert everything over and over. Great idea 10/10'''
        return ''.join((list(dict.fromkeys(list(x)))))
    
    def outgoing_arcs(self, tail_node):
        " ** COMPLETE ** "
        outgoing = []
       # print('tn',tail_node)
        for rule in tail_node: 
           # print(f"Replace {rule} in {tail_node}")
            if rule  in self.clauses:
               # print(f"looks like {rule}  in {self.clauses}")
                for b in self.clauses[rule]: 
                #print(f"\t {b}")
                    repl = (''.join(b))
                    candidate = tail_node.replace(rule, self.slowdupscheck((repl)))
                    outgoing.append(Arc(tail_node, candidate,action = '',cost = 0))
               
         #  outgoing = [tail_node.replace(rule, (b)) for b in self.clauses[rule]]
           # print(f"Yields: -> {outgoing}")
            
       
        return outgoing
            
        
        #[item for sublist in list_of_lists for item in sublist]
        
        
        
        
        
        
        
        
        
        



class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(-1)
        else:
            raise StopIteration   # don't change this one
        
        
        
if __name__ == "__main__":


    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
        g.
    """

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        
    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
        g.
    """

    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        


    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """

    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")
        
        
    kb = """
    a :- b.
    """

    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")