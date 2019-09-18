# csp = CSP(
#    var_domains = {var:{-1,0,1} for var in 'abcd'},
#    constraints = {
#       lambda a, b: a == abs(b),
#       lambda c, d: c > d,
#       lambda a, b, c: a * b > c + 1
#       }
#    )



# Note: if two tables do not join they are unique relations
from csp import Relation

relations = [
    Relation(
        header = ['a','b'],
        tuples = {(0,0),
                  (1,1),
                  (1,-1)}
    ),
    
    Relation(
        header = ['c','d'],
        tuples = {(0,-1),
                  (1,0),
                  (1,-1)}
            ),
    Relation(
        header = ['a','b','c'],
        tuples = {(1,1,-1),
                  (-1,-1,-1),
                  }
    )

      
      ### COMPLETE ###
      
      ] 

relations_after_elimination = [
    
    Relation(
        header = ['c','d'],
        tuples = {(0,-1),
                  (1,0),
                  (1,-1)}
            ),
    Relation(
        header = ['b','c'],
        tuples = {(1,-1)
                  }
    )

    
    ### COMPLETE ###
    
    ] 