% Write a predicate swap_ends(?List1, ?List2) which succeeds if List1 is identical to List2 ,
% except that the first and last elements are exchanged. The predicate should fail on lists with fewer than two elements.
%
% Hint: One way to solve this problem is to use append/3.
%  You can also write this predicate without using any other predicates.




%We need to ensure that the input list has at least two elements
%We shall use an auxiliary predicate to require this:
swap_ends([X1, X2| Xs], [Y1, Y2| Ys]) :-
												swap_ends_2plus([X1, X2| Xs], [Y1, Y2| Ys]).



% note that Xs may be blank, but we must unify with  the left of each pred arg


swap_ends_2plus([], []).
swap_ends_2plus(L1, L2) :-
												append([H1| B1], [H2], L1),
	    									append([H2| B1], [H1], L2).




test_answer :-
    swap_ends([a, b, c, d, e, f], L),
    writeln(L).

test_answer :-
    swap_ends(L1, L2),
    writeln('OK').

test_answer :-
    swap_ends(L, [term1, term2, term3, term4]),
    writeln(L).

test_answer :-
    swap_ends([367], L),
    writeln('Wrong answer!').

test_answer :-
    writeln('OK').
