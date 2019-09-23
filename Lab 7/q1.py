import itertools


        

def n_queens_neighbours(state):
    res = set()
    def format_back(state, template):
        result = []
        for candidate in template: 
            A,B = candidate[0],candidate[1]
            current = list(state[:])
            current[A],current[B] = current[B],current[A]
            result.append(tuple(current))
        return sorted(result)
            
        
    for candidate in range(len(state)): 
        for replace in range(len(state)):
            if candidate != replace:
                res.add(tuple(sorted((candidate,replace))))
  #  print(res)
    
    return(format_back(state,res))
    
    
    
        



print(n_queens_neighbours((1, 2)))


print(n_queens_neighbours((1, 3, 2)))


print(n_queens_neighbours((1, 2, 3)))


print(n_queens_neighbours((1,)))


        
for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
    print(neighbour)

for neighbour in n_queens_neighbours((2, 3, 1, 4)):
    print(neighbour)