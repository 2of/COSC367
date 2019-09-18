import itertools, copy 
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in csp.var_domains}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()
        for xval in csp.var_domains.get(x):
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                   for z in scope(cprime):
                       if x != z:
                           tda.add((z, cprime))
    return csp




simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

csp = arc_consistent(simple_csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))






csp = CSP(var_domains={x:set(range(10)) for x in 'abc'},
          constraints={lambda a,b,c: 2*a+b+2*c==10}) 

csp = arc_consistent(csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))







var_domains={
    'a1': {'has', 'bus'}, 
    'a3': {'lane', 'year'}, 
    'a4': {'car', 'ant'}, 
    'd1': {'buys', 'hold'}, 
    'd2': {'syntax', 'search'}}

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': set("has bus".split()),
        'a3': set(" lane year".split()),
        'a4': set("ant car".split()),
        # read down:
        'd1': set("buys hold".split()),
        'd2': set("search syntax".split()),
        },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
        })


print(sorted(crossword_puzzle.var_domains['a1']))
