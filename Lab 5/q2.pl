% Write a predicate swap12(?List1, ?List2) which succeeds when
% List1 is identical to List2, except that the first two elements are exchanged. The predicate must fail on lists with fewer than two elements.
% Note that either of the arguments can be bound or unbound (input or output).









swap12([A,B|C],[B,A|C]).

% Per question one, this is just unification



test_answer :-
    swap12([a, b, c, d], L),
    writeln(L).

test_answer :-
    \+ swap12(L, [1]),
    writeln('OK').

test_answer :-
    swap12(L, [b, a]),
    writeln(L).

test_answer :-
    swap12(L1, L2),
    writeln('OK').
