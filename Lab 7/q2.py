import itertools

def n_queens_state(state):
    ''' Y is position in list, x is x'''
    candidate = (list(itertools.combinations(state,2)))
    count = 0
    for each in candidate:
        #aBsTrAcTiOn
        y1 = state.index(each[0])
        y2 = state.index(each[1])
        x1,x2 = each[0],each[1]
        dy = y2 - y1
        dx = x2 - x1
        if (abs(dx)==abs(dy)):
            count += 1 
    return count
    
  
print(cost((1, 2))) 
print(cost((1, 3, 2))) 
print(cost((1, 2, 3)))  
print(cost((1,)))
print(cost((1, 2, 3, 4, 5, 6, 7, 8)))
print(cost((2, 3, 1, 4)))