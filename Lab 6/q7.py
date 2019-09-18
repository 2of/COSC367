import itertools, copy 
from csp import *

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x:v for x, v in zip(names, values)}
        if all(satisfies(assignment,con) for con in csp.constraints):
            yield assignment



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




# two + two
# four
cryptic_puzzle = CSP(

        

    var_domains={x: set(range(1 if x == 'f' else 0, 10)) for x in 'twofur'},
    constraints={
       
        
        lambda t, w, o, f, u, r: len([t,w,o,f,u,r]) == len(set([t,w,o,f,u,r])),
        lambda o, w, u: ((0 if o < 5 else 1) + w + w) % 10 == u,
        lambda w, t, o: ((0 if w < 5 else 1) + t + t) % 10 == o,
        lambda t: t + t >= 10,
        lambda f: f == 1,
        #
        
        
         lambda o,r: (o + o) % 10 == r,
         #final char
                
        })



from csp import *
from collections import OrderedDict
#from student_answer import cryptic_puzzle, arc_consistent, generate_and_test

new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])