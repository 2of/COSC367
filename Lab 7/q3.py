# def greedy_des3cent(initial_state, neighbours, cost):
#     flag = 0
#     prev_cost = -1000000 #just a negative because 
#     active = initial_state
#     prev_point = 0
#     statelist = []
#     while not flag:
#         #big ugly mess because i cant figure out how to zip this up nicely
#         statelist.append(active)
#         min_ = 10000
#       #  print(active,prev_point)
#         for each in neighbours(active):
            


    
#         if prev_point >= active:
#             break;
#             flag = 1
#         prev_point = active


#     return statelist


def get_min1(state, neighbours,cost):
     active = min(neighbours(state), key = abs)
     return active

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
       # print(new,new_cost,costlist)
        if last_encountered == new:
            flag = 1
            break
        last_encountered = current
        current = new
    return statelist





import time
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(4, neighbours, cost):
    print(state)
def cost(x):
    return x**2

def neighbours(x):
    return [x - 1, x + 1]

for state in greedy_descent(-6.75, neighbours, cost):
    print(state)

def cost(x):
  #  print ("HERE",x)
    return -x**2

def neighbours(x):
    return [x - 1, x + 1] if abs(x) < 5 else []

for state in greedy_descent(0, neighbours, cost):
    print(state)



def cost(state):
    x, y = state
    return abs(x) + abs(y)

def neighbours(state):
    x, y = state
    return [(x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1),]

for state in greedy_descent((3,4), neighbours, cost):
    print(state)


def cost(state):
    x, y = state
    return abs(x) + abs(y)

def neighbours(state):
    x, y = state
    return [(x - 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x + 1, y + 1),]

for state in greedy_descent((0,8), neighbours, cost):
    print(state)