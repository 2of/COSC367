from search import *
import heapq
import math
LETTERNODECOST = math.inf
BORDERCHARS = ['|','-','+','X']
FUEL_UP_NAME = 'Fuel up'
TRANSLATECOST = 5

#Note the inclusion of 'deleteme', It provides a nice graphical way to observe the heuristic costs


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
        self.cc = 0
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
        '''unnecessary, yes... But that is okay!'''
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
            print(self.cc)
            self.cc += 1
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
