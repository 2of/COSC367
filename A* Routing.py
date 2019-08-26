'''
Noah King 2019, Also Pinchy Pinchy Template from UC
A* routing algorithm(s) for COSC367 2019.
-Requires search.py module for abstract definitions, for generic search algorithm
-Therefore this file is simply the frontier for A*, with pruning and a graph class, which provides methods for
heuristic generation, setup.


-Example cases provided in __main__ for the 'draw_map' function only,
also handles things like below,  however print_map does not handle these:

    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """
    ->  Actions:
                N,
                N,
                E,
                Fuel up,
                W,
                S,
                S,
                E,
                E,
                E,
                E,
                E,
                N.
                Total cost: 75
    NOTE: the supporting code for this in __main__


-Directly; This is A* on a graph generated from a map_string (See further examples down),
An agent from an 'S' or Numeric start point must reach the 'G' node; Each move costs 5 units, A numbered agent
has that amount of moves available, lest it reaches an 'F' and refuels to 9 at a cost of 15 units.
- Manhattan distance is used for the heuristic
- Pruning is used (note this implementation is a little memory heavy, there is only removal pruning, everything goes back into
the heap!)
'''


from search import *
import heapq
import math
from collections import namedtuple
LETTERNODECOST = math.inf
BORDERCHARS = ['|','-','+','X']
FUEL_UP_NAME = 'Fuel up'
TRANSLATECOST = 5




class RoutingGraph(Graph):
    def __init__(self,map_str):
        self.matrix, self.starting_nodes_, self.goal_nodes = self.decompose_graph(map_str)
        self.deleteme = []

    def decompose_graph(self, graph_str):
        a = [b.strip() for b in graph_str.splitlines()]
        matrix = [[r for r in c] for c in a]
        sn,gn = [],[]
        location = namedtuple('location','x,y,cost')
        for c in range(len(matrix)):
            for r in range(len(matrix[c])):
                if matrix[c][r] == 'S':
                    sn.append(location(c,r,LETTERNODECOST))
                elif matrix[c][r] == 'G':
                    gn.append(location(c,r,0))
                elif matrix[c][r].isdigit():
                    sn.append(location(c,r,int(matrix[c][r])))
        return matrix, sn, gn

    def is_goal(self,node):
        for cand in self.goal_nodes:
            if node[0] == cand.x and node[1] == cand.y:
                return True
        return False

    def strip_tuple(self, _tuple):
        return (_tuple.x,_tuple.y,_tuple.cost)

    def starting_nodes(self):
        return [self.strip_tuple(a) for a in self.starting_nodes_]

    def outgoing_arcs(self,tail_node):
        arcs = []
        valid_actions = ['S','G',' ','F']
        moves =  [('N' , -1, 0),
                  ('E' ,  0, 1),
                  ('S' ,  1, 0),
                  ('W' ,  0, -1)]
        y,x = tail_node[0],tail_node[1]
        for action,dy,dx in moves:
            candidate = self.matrix[y+dy][x+dx]
            if (candidate in valid_actions or candidate.isdigit()) and tail_node[2]-1 >= 0:
                arcs.append(Arc(tail_node,(y+dy,x+dx,tail_node[2] - 1),action,TRANSLATECOST))
        if self.matrix[y][x] == 'F' and tail_node[2] < 9:
            arcs.append(Arc(tail_node,(y,x,9),FUEL_UP_NAME,15))
        return arcs

    def estimated_cost_to_goal(self, node):
        """Return the estimated cost to a goal node from the given
        state. This function is usually implemented when there is a
        single goal state. The function is used as a heuristic in
        search. The implementation should make sure that the heuristic
        meets the required criteria for heuristics."""
        if node in self.goal_nodes:
            return 0
        if node is None:
            return 0
        heuristic = lambda x1,x2,y1,y2 : abs(x1-x2) + abs(y1-y2) #manhattan distance
        pool = []
        nrow = node[0]
        ncol = node[1]
        for grow,gcol,_ in self.goal_nodes:
            pool.append(heuristic(ncol,gcol,nrow,grow))
        return min(pool)*5




class AStarFrontier(Frontier):
    def __init__(self, map_g):
        self.priority_count = {}
        self.container = []
        self.map_g = map_g
        self.hedgeclippers = set()
        heapq.heapify((self.container))

    def make_heap_key(self,cost):
        if cost in self.priority_count: 
            self.priority_count[cost] += 1
            return (cost,self.priority_count[cost])
        self.priority_count[cost] = 0
        return (cost,self.priority_count[cost])
        

    def make_prune_key(self, arc_):
        '''This adds a little overhead, not much. Just a convenient way to 
            configure what goes into the heap!!!'''
        return ((arc_.head[0],arc_.head[1],arc_.head[2]))

    def add(self, path):
        cost = sum(arc.cost for arc in path) + self.map_g.estimated_cost_to_goal(path[-1].head);
        key = (self.make_heap_key(cost))
        heapq.heappush(self.container, (key, path))

    def add_to_clippings(self, arc_):
        self.hedgeclippers.add(self.make_prune_key(arc_))

    def clip_check(self, arc_):
        if arc_.tail is not None:
            return True if (self.make_prune_key(arc_)) in self.hedgeclippers else False
        return False
   
    
    def __iter__(self):
        return self

    def __next__(self):
        while len(self.container) > 0:
            candidate = heapq.heappop(self.container)[1]
            if not (self.clip_check(candidate[-1])):
                self.add_to_clippings(candidate[-1])
                return candidate
        raise StopIteration






def print_map(map_graph, frontier, solution):
    for x,y,_ in frontier.hedgeclippers:
        map_graph.matrix[x][y] = '.'
    if solution is not None:
        for a in solution:
            map_graph.matrix[a.head[0]][a.head[1]] = '*'
    for x in map_graph.starting_nodes_:
        map_graph.matrix[x.x][x.y] = 'S'
    for x in map_graph.goal_nodes:
        map_graph.matrix[x.x][x.y] = 'G'
    for row in map_graph.matrix: 
        print(''.join(row))

    

if __name__ == "__main__":
    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


    map_str = """\
    +----------------+
    |                |
    |                |
    |                |
    |                |
    |                |
    |                |
    |        S       |
    |                |
    |                |
    |     G          |
    |                |
    |                |
    |                |
    +----------------+
    """


    map_graph = RoutingGraph(map_str)
    # changing the heuristic so the search behaves like LCFS
    map_graph.estimated_cost_to_goal = lambda node: 0

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)



    map_str = """\
    +-------------+
    | G         G |
    |      S      |
    | G         G |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)




    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    |  S    |
    +-------+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


    map_str = """\
    +----+
    |    |
    | SX |
    | X G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +---------------+
    |    G          |
    |XXXXXXXXXXXX   |
    |           X   |
    |  XXXXXX   X   |
    |  X S  X   X   |
    |  X        X   |
    |  XXXXXXXXXX   |
    |               |
    +---------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)




    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)

    map_str = """\
    +-------------+
    |S            |
    |             |
    |   G      S  |
    |             |
    | G           |
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


    map_str = """\
    +-------------+
    |G           G|
    |     S       |
    |             |
    |          G  |
    |S           S|
    +-------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_map(map_graph, frontier, solution)


    map_str = """\
    +-------+
    |   G   |
    |       |
    |   S   |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)



    map_str = """\
    +-------+
    |  GG   |
    |S    G |
    |  S    |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


    map_str = """\
    +-------+
    |     XG|
    |X XXX  |
    | S     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)





    map_str = """\
    +-------+
    |  F  X |
    |X XXXXG|
    | 3     |
    +-------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


    map_str = """\
    +--+
    |GS|
    +--+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)



    map_str = """\
    +---+
    |GF2|
    +---+
    """
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)



    map_str = """\
    +----+
    | S  |
    | SX |
    |GX G|
    +----+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)



    map_str = """\
    +---------+
    |         |
    |    G    |
    |         |
    +---------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)



    map_str = """\
    +----------+
    |    X     |
    | S  X  G  |
    |    X     |
    +----------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)




    map_str = """\
    +----------------+
    |2              F|
    |XX     G 123    |
    |3XXXXXXXXXXXXXX |
    |  F             |
    |          F     |
    +----------------+
    """

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


    import math

    map_str = """\
    +-------+
    |  9  XG|
    |X XXX  |
    | S  0FG|
    +-------+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(s)
        for arc in graph.outgoing_arcs(s):
            print ("  " + str(arc))

    node = (1,1,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (1,7,2)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3, 7, 0)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3, 7, math.inf)
    print("\nIs {} goal?".format(node), graph.is_goal(node))

    node = (3,6,5)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))

    node = (3,6,9)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))
            
            
            
    map_str = """\
    +--+
    |GS|
    +--+
    """

    graph = RoutingGraph(map_str)

    print("Starting nodes:", sorted(graph.starting_nodes()))
    print("Outgoing arcs (available actions) at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print ("  " + str(arc))



    node = (1,1,1)
    print("\nIs {} goal?".format(node), graph.is_goal(node))
    print("Outgoing arcs (available actions) at {}:".format(node))
    for arc in graph.outgoing_arcs(node):
        print ("  " + str(arc))