import math
from functools import reduce

def euclidean_distance(a,b):
    # notice, this will definitely throw a IndexError if len(a) != len(b)
    return math.sqrt(reduce(lambda i,j: i + ((a[j] - b[j]) ** 2), range(len(a)), 0))
    
    
    
def majority_element(labels):
    ''' inefficient, I know, but it was lookups vs try catch block '''
    freq_t = {}
    for c in labels:
        try:
            freq_t[c] += 1 
        except:
            freq_t[c] = 1
   # print(freq_t)
    return max(freq_t, key=freq_t.get)
        
    
    
print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))


print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
print(majority_element("abcabcabcabc") in "abc")