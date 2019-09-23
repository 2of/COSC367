import itertools

def n_queens_cost(state):
    ''' Y is position in list, x is x'''
    if type(state) == int:
        state = [state]
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
    
    
def n_queens_neighbours(state):
    if type(state) == int:
        state = [state]
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


def get_min(state, neighbours, cost):
    ''' why yes, this is very nasty nasty code'''
    min_ = 1000000000
    active = state
    for each in neighbours(state):
        statecost = cost(each)
        if statecost < min_:
            active = each
            min_ = statecost

    return (active,min_)





def greedy_descent(initial_state, neighbours, cost):
    #print(f"call on initial:{initial_state}")
    flag = 0
    statelist = []
    costlist = []
    new_cost = cost(initial_state)
    last_encountered = -10000
    current = initial_state
    while not flag:
        if new_cost in costlist:
            flag = 1
            break
        if current in statelist:
            flag = 1
            break
        costlist.append(new_cost)
        statelist.append(current)
        new,new_cost = get_min(current, neighbours,cost)
        if last_encountered == new:
            flag = 1
            break
        last_encountered = current
        current = new
    return statelist,cost(last_encountered)




def greedy_descent_with_random_restart(random_state, neighbours, cost):
    '''
    Greedy descent :- the nasty, works for the quiz
    edition, featuring hardcoded stops! Duplicate code and
    an asymptotic nightmare!
    
    
    '''
    a = random_state()
    final = -1
    prev = 100000
    while final:
        prev = 100000000
        sol,final = list(greedy_descent(a,neighbours,cost ))
        for each in sol:
            c_ = cost(each)
            if not(c_ > prev):
                print(each)
            if c_ == 0:
                final = 0
                break
            prev = c_            
        if final:
            print("RESTART")
            a = random_state()
             