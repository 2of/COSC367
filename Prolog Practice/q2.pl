% Write a predicate reversed(?Forward, ?Backward) that asserts Backward is the reverse of Forward. It should behave identically to the built-in predicate reverse/2, but should not use this predicate.







reversed_(L,L1):-reversed_(L,[],L1).
reversed_([],ACC,ACC).
reversed_([X|L], ACC,L1):- reversed_(L,[X|ACC],L1).





reversed(A,B) :- reversed(A,[],B).
reversed([],BF,BF).
reversed([H|B],BF,R) :- reversed(B,[H|BF],R).
test_answer :-
    reversed([1, 2, 3, 4, 5], L),
    writeln(L).

test_answer :-
    reversed(L, [d, c, b, a]),
    writeln(L).
