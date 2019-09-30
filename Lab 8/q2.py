import itertools
'''
    Hello.
    There is a bug with this implementation 
    with A -> B, p(B|A) we yield a keyerror.
    


'''

def query(network, query_var, evidence):
    '''
    Slides 15/16 here! Woohoo it works
    '''
    def do_query(network, query_var, evidence_):
        pt = 0
        evidence = evidence_.copy()
        hidden_vars = network.keys() - evidence.keys() - {query_var}
        if len(hidden_vars) == 0:
            pt += joint_prob(network,evidence)
        else:
            hidden_vars = network.keys() - evidence.keys()
            for values in itertools.product((True, False), repeat=len(hidden_vars)):
                hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
                for consider in hidden_assignments:
                    evidence[consider] = hidden_assignments[consider]
                pt += joint_prob(network,evidence)
        return pt


    qbase = do_query(network,query_var,evidence)
    evidence[query_var] = True
    qT = do_query(network,query_var,evidence)
    evidence[query_var] = False
    qF = do_query(network,query_var,evidence)
    return[qF/qbase,qT/qbase]







def joint_prob(network,assignment):
    jp = 1
    for header in assignment.keys():
        this = network[header]
        consider_parents = tuple([assignment[a] for a in network[header]['Parents']])
        prob = this['CPT'].get(consider_parents)
        if assignment[header]:
            jp *= prob
        else:
            jp *= (1-prob)
    return jp

def joint_prob(network, assignment):
    total = 1
    for header in assignment:
        value = network[header]
        parents = tuple([assignment[a] for a in network[header]["Parents"]])
        if assignment[header]:
            total *= value['CPT'][parents] 
        else:
            total *= 1 - value['CPT'][parents]
    return total

        
        




network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {})
print("P(B=true) = {:.5f}".format(answer[True]))
print("P(B=false) = {:.5f}".format(answer[False]))

network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'Burglary', {'John': True, 'Mary': True})
print("Probability of a burglary when both\n"
      "John and Mary have called: {:.3f}".format(answer[True]))                        


network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

answer = query(network, 'John', {'Mary': True})
print("Probability of John calling if\n"
      "Mary has called: {:.5f}".format(answer[True]))           