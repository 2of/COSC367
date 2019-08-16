mirror(leaf(X), leaf(X)).
mirror(tree(L, R), tree(A, B)) :- mirror(R, A), mirror(L, B).
