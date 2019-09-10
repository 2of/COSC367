%Write a predicate new_append(?A, ?B, ?AB) that behaves exactly the same as the built-in append/3, without using append/3.

% 
% new_append([], List, List).
% new_append([Head|Tail], List, [Head|Rest]) :-
%     new_append(Tail, List, Rest).
%


new_append([], L, L).
new_append([H1|B1], L1, [H1|Rest]) :- new_append(B1,L1,Rest).

test_answer :-
    new_append([1, 2, 3], [a, b, c], L),
    writeln(L).

test_answer :-
    new_append([1, 2, 3], L, [1, 2, 3, 4, 5]),
    writeln(L).
