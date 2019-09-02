% Write a predicate twice(?In, ?Out) whose left argument is a list, and whose right argument is a list consisting of every element in the left list repeated twice. For example, the query
%
% twice([a,4,buggle],X).
% gives
% X = [a,a,4,4,buggle,buggle].
% and the query
% twice(X, [1, 1, 2, 2]).
% gives
% X = [1,2].
% and the query
% twice(X, [a, a, b, b, c]).
% fails.
% Hint: to answer this question, first ask yourself
% “What should happen when the first argument is the empty list?”. That’s the base case. For non-empty lists, think about what you should do with the head, and use recursion to handle the tail.
%
%


%Because the definition will be recursive: Define a base case, here blank -> blank
twice([],[]).
twice([H1|T1],[H1,H1|T2]) :- twice(T1,T2).

%Define the second rule as (unify head to head * 2) if there is a way to do this for the next. Until base case


test_answer :-
    twice([a, b, c, d], L),
    writeln(L).
[a,a,b,b,c,c,d,d]
test_answer :-
    twice(L, [1, 1, 2, 2, 3, 3]),
    writeln(L).

test_answer :-
    twice([], []),
    writeln('OK').

test_answer :-
    twice(L1, L2),
    writeln('OK').

test_answer :-
    \+ twice(L, [a, a, b]),
    writeln('OK').
