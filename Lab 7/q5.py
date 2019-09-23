
    
def roulette_wheel_select(population, fitness, r): 
    '''It's not really worth it ot normalise here. We just carry along until we hit the 'section' 
    of the wheel that this r falls within; r * total stops us from running off the edge '''
    total = float(sum(fitness(x) for x in population))
    c = 0
    for each in population:
        if r * total < c + fitness(each):
            return each
        c += fitness(each)
    
    
    
    
population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))
    
    
print("--")
    
population = [0, 1, 2]

def fitness(x):
    return x

for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))
print("--")
    
    
population = [0,1,2,3,4,5]

def fitness(x):
    return [8,2,17,7,4,11][x]
for r in range(0,49,4):
    print(roulette_wheel_select(population,fitness,r/49))