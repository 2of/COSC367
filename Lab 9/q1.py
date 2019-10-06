'''Use the spreadsheet bundled in this lab to calculate the weights en masse '''

'''This is just a little tool you can use to pretty up the format of the website'''
from numbers import Number

reference = "T  T	F	F   T	F	F	F   T	T	F	F   T	F	F	T   F	F	F	T   F	T	F	T   F	F	F	T".split()
tuples = []
# Put it all back together!
print(len(reference)/4)
for i in range(int(len(reference)/4)): 
    tuples.append(zip(*[reference[i::4] for i in range(4)]))
tuples = tuples[0]
for a in tuples:
    print(a)

network = {
    'Y': {
        'Parents': [],
        'CPT': {
            (): (6/11)
        }
    },

    'X1': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (3/8),
            (False,): (5/7)
        }
    },

    'X2': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (3/8),
            (False,): (4/7)
        }
    },

    'X3': {
        'Parents': ['Y'],
        'CPT': {
            (True,): (2/8),
            (False,): (2/7)
        }
    }
}


# ('T', 'T', 'F', 'F')
# ('T', 'F', 'F', 'F')
# ('T', 'T', 'F', 'F')
# ('T', 'F', 'F', 'T')
# ('F', 'F', 'F', 'T')
# ('F', 'T', 'F', 'T')
# ('F', 'F', 'F', 'T')





# Checking the overall type-correctness of the network
# without checking anything question-specific

assert type(network) is dict
for node_name, node_info in network.items():
    assert type(node_name) is str
    assert type(node_info) is dict
    assert set(node_info.keys()) == {'Parents', 'CPT'}
    assert type(node_info['Parents']) is list
    assert all(type(s) is str for s in node_info['Parents'])
    for assignment, prob in node_info['CPT'].items():
        assert type(assignment) is tuple
        assert isinstance(prob, Number)

print("OK")