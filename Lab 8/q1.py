

def joint_prob(network,assignment):
    ''' 
    Perhaps On^2, likely  a lil less
    '''
    jp = 1
    for header in assignment.keys():
        this = network[header]
        c onsider_parents = tuple([assignment[a] for a in network[header]['Parents']])
        prob = this['CPT'].get(consider_parents)
        # Consider parents used for false,false requirements etc
        if assignment[header]:
            jp *= prob
        else:
            jp *= (1-prob)
    return jp
        
        
        
        







# network = {
#     'A': {
#         'Parents': [],
#         'CPT': {
#             (): 0.2
#             }},
# }

# p = joint_prob(network, {'A': True})
# print("{:.5f}".format(p))

# network = {
#     'A': {
#         'Parents': [],
#         'CPT': {
#             (): 0.2
#             }},
# }

# p = joint_prob(network, {'A': False})
# print("{:.5f}".format(p))


# network = {
#     'A': {
#         'Parents': [],
#         'CPT': {
#             (): 0.1
#             }},
            
#     'B': {
#         'Parents': ['A'],
#         'CPT': {
#             (True,): 0.8,
#             (False,): 0.7,
#             }},
#     }
 
# p = joint_prob(network, {'A': False, 'B':False})
# print("{:.5f}".format(p)) 


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

p = joint_prob(network, {'John': True, 'Mary': True,
                         'Alarm': True, 'Burglary': False,
                         'Earthquake': False})
print("{:.8f}".format(p))                 