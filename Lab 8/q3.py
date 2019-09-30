

network = {
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 0.00001
            }},
            
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 0.99,
            (False,): 0.01,
            }},
    }
 