% Write a predicate second(?List,?X) which succeeds when X is the second element of List.
%
% Note that as the notation implies, either of the arguments can be instantiated or unbound (input or output).
%
% In some test cases, you see the symbol \+ which means negation.





second([_,X|_],X).

% How does this work? We Decompose the 'head' as the left of the '|' operator
% i.e. head = _,X, tail = _. And we'd like to have the X's unify in the second spot.




% Test Cases:

test_answer :-
    second([cosc, 2, Var, beethoven], X),
    writeln(X).

test_answer :-
    \+ second([1], X),
    writeln('OK').

test_answer :-
    second([a, b, c, d], b),
    writeln('OK').

test_answer :-
    second(L, X),
    writeln('OK').
