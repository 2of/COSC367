import itertools

def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    trueProb = 0
    falseProb = 0
    for values in itertools.product((True, False), repeat=len(hidden_vars)):
        hidden_assignments = {var:val for var,val in zip(hidden_vars, values)}
        hidden_assignments.update(evidence)
        hidden_assignments.update({query_var: True})
        trueProb += joint_prob(network, hidden_assignments)
        hidden_assignments[query_var] = False
        falseProb += joint_prob(network, hidden_assignments)
    normalizer = trueProb + falseProb
    result = {True: trueProb / normalizer, False: falseProb / normalizer}
    return result



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
network = {
    'Virus' : {
        "Parents" : [],
        "CPT" : {
            (): 0.01
        },
    },
    'A' : {
        'Parents' : ["Virus"],
        "CPT" : {
            (True,): 0.95,
            (False,): 0.1
        }
    },
    'B' : {
        'Parents' : ["Virus"],
        "CPT" : {
            (True,): 0.9,
            (False,): 0.05
        }
    }
}



 
answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))


answer = query(network, 'Virus', {'B': True})
print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))