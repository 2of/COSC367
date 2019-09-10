% DNA is a really big molecule that encodes all the information about an organism. It has four bases: cytosine (c), guanine (g), adenine (a), and thymine (t). Base c always pairs with g, and a always pairs with t, meaning that from a single half of a DNA strand you can always build the other:
% this is exactly what your body does when cells are splitting! Write a predicate dna(?Left, ?Right) that makes sure the left and right halves of a DNA strand match.






match(A,B) :- A = 'c', B = 'g'.
match(A,B) :- A = 'g', B = 'c'.
match(A,B) :- A = 't', B = 'a'.
match(A,B) :- A = 'a', B = 't'.


dna([],[]).
dna([HL|BL],[HR|BR]) :- match(HL,HR),dna(BL,BR).









test_answer :- dna([a, t, c, g], X),
               writeln(X).
test_answer :- dna(X, [t, a, g, c]),
               writeln(X).
