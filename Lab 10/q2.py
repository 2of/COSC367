import math
from functools import reduce

def euclidean_distance(a,b):
    # notice, this will definitely throw a IndexError if len(a) != len(b)
    return math.sqrt(reduce(lambda i,j: i + ((a[j] - b[j]) ** 2), range(len(a)), 0))
    
    
    
def majority_element(labels):
    ''' inefficient, I know, but it was lookups vs try catch block '''
    freq_t = {}
    #print("TERTE",labels)
    for c in labels:
        try:
            freq_t[c] += 1 
        except:
            freq_t[c] = 1
   # print(freq_t)
    

    a = [k for k, v in freq_t.items() if v == max(freq_t.values())]

    a.sort()
    return (a[0])
''' convert this to a list of tuples and use that!'''



def knn_predict(input, examples, distance, combine, k):
    ''' How efficient'''
    candidates = []
    consider = examples[:]
    consider.sort(key = lambda x: distance(input,x[0]))
    last_used = 0
    for i in range(k):
        t  = consider.pop(0)
        candidates.append(t[1])
        last_used = t[0]
    while(consider and distance(input,last_used)== distance(input,consider[0][0])):
        t  = consider.pop(0)
        candidates.append(t[1])
        last_used = t[0]
    return combine(candidates)
        
    

# examples = [
#     ([2], '-'),
#     ([3], '-'),
#     ([5], '+'),
#     ([8], '+'),
#     ([9], '+'),
# ]

# distance = euclidean_distance
# combine = majority_element

# for k in range(1, 6, 2):
#     print("k =", k)
#     print("x", "prediction")
#     for x in range(0,10):
#         print(x, knn_predict([x], examples, distance, combine, k))
#     print()
    
    
    

examples = [
    ([1], 5),
    ([2], -1),
    ([5], 1),
    ([7], 4),
    ([9], 8),
]

def average(values):
    return sum(values) / len(values)

distance = euclidean_distance
combine = average

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print("{} {:4.2f}".format(x, knn_predict([x], examples, distance, combine, k)))
    print()