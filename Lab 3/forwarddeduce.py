import re

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


def forward_deduce(map):
    def rules_to_thing(base,rels):
           # print(base)
            for head,clauses in rels: 
                if head not in base: 
                    flag = 0
                    for each in clauses:
                        if each not in base:    
                            flag = 1        #continue not going on ? 
                    if not flag:        
                        return rules_to_thing(base + [head], rels)
            return base

    a = list(clauses(map))
  #  print(a)
    base = []

    #1 get starty fellas

    for rule in a:
       if rule[1] == []:
           base.append(rule[0])
    return(rules_to_thing(base,a))





if __name__ == "__main__":
    

    kb = """
    a :- b.
    b.
    """

    print(", ".join(sorted(forward_deduce(kb))))


    kb = """
    good_programmer :- correct_code.
    correct_code :- good_programmer.
    """

    print(", ".join(sorted(forward_deduce(kb))))


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

    print(", ".join(sorted(forward_deduce(kb))))



