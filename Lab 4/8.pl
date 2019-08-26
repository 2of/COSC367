/*Binary trees are trees where all internal nodes have exactly two children. The mirror of a binary tree is obtained by exchange all the left and right children. For example the following two trees are the mirror of each other:

     .                   .
    / \	                / \
   1   .               .   1
      / \             / \
     2   3           3   2
The smallest binary trees consist of only one leaf node. We will represent leaf nodes as leaf(Label) . For instance, leaf(1) and leaf(3) are leaf nodes, and therefore small binary trees. Given two binary trees B1 and B2 we combine them into one binary tree by tree(B1,B2).So, from the leaves leaf(2) and leaf(3) we can build the binary tree tree(leaf(2),leaf(3)) . And from the binary trees leaf(1) and tree(leaf(2),leaf(3)) we can build the binary tree tree(leaf(4), tree(leaf(1), leaf(2))).

Define a predicate mirror/2 that succeeds when the two arguments are binary trees and are the mirror of each other.
*/





mirror(leaf(X),leaf(X)).
% The case that the two next nodes are identical
mirror(tree(L,R), tree(A,B)) :- mirror(R,A), mirror(L,B).
% Mirror is definied recursively ; Mirror R,A & mirror(L,B) are defined by
% picking off from each side, then recursing until the two are indentical leaves.



test_answer :-
    mirror(leaf(foo), leaf(foo)),
    write('OK'),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.


test_answer :-
    mirror(tree(leaf(foo), leaf(bar)), tree(leaf(bar), leaf(foo))),
    write('OK'),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.


test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  leaf(4)), T),
    write(T),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.


test_answer :-
    mirror(tree(tree(leaf(1),  leaf(2)),  tree(leaf(3), leaf(4))), T),
    write(T),
    halt.

test_answer :-
    write('Wrong answer!'),
    halt.
