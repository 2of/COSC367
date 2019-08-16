from search import * 
import math



import collections  


class LocationGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, nodes,locations,edges,starting_nodes,goal_nodes):
        self.nodes = nodes
        self.locations = locations
        self.edges = edges
        self.starting_nodes_ = starting_nodes
        self.goal_nodes = goal_nodes
        self.adj_list = self.make_pretty_datastructure(self.edges)
        
        
    def make_pretty_datastructure(self,edges):
        '''makes the data structure a lil nicer'''
        adj_list = {node : [] for node in self.nodes }
        for edge in edges: 
            x_dif = (self.locations[edge[0]][0] - self.locations[edge[1]][0])
            y_dif = (self.locations[edge[0]][1] - self.locations[edge[1]][1])            
            dist = math.sqrt(x_dif**2 + y_dif **2) 
            if ((edge[1],dist)) not in adj_list[edge[0]]:
                adj_list[edge[0]].append((edge[1],dist))
                adj_list[edge[1]].append((edge[0],dist))
        return adj_list
        
        
        
        

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        connections = []
        for arc in self.adj_list[tail_node]:
            connections.append(Arc(tail_node,arc[0],action = f"{tail_node}->{arc[0]}", cost = arc[1]))
        connections.sort(key = lambda x: x[1])
        return connections
   
    
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the seqence always has one element."""
        return [self.starting_nodes_] #abstract requires this exists!
 
    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        if node in self.goal_nodes:
            return True
        
        







# answers: 

graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})


for arc in graph.outgoing_arcs('A'):
    print(arc)

for arc in graph.outgoing_arcs('B'):
    print(arc)

for arc in graph.outgoing_arcs('C'):
    print(arc)
    
    
print('\n\n')
pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    starting_nodes=['a'],
    goal_nodes={'c'})

for arc in pythagorean_graph.outgoing_arcs('a'):
    print(arc)
    
    
    
print('\n\n')
graph = LocationGraph(nodes=set('ABC'),
                      locations={'A': (0, 0),
                                 'B': (3, 0),
                                 'C': (3, 4)},
                      edges={('A', 'B'), ('B','C'),
                             ('B', 'A'), ('C', 'A')},
                      starting_nodes=['A'],
                      goal_nodes={'C'})


for arc in graph.outgoing_arcs('A'):
    print(arc)

for arc in graph.outgoing_arcs('B'):
    print(arc)

for arc in graph.outgoing_arcs('C'):
    print(arc)