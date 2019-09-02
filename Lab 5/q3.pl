% Suppose we are given a knowledge base with the following facts:
%
% tran(eins,one).
% tran(zwei,two).
% tran(drei,three).
% tran(vier,four).
% tran(fuenf,five).
% tran(sechs,six).
% tran(sieben,seven).
% tran(acht,eight).
% tran(neun,nine).
% Write a predicate listtran(?G, ?E) which translates a list of German number words to/from the corresponding list of English number words. For example:
%
% listtran([eins,neun,zwei],X).
% should give:
% X = [one, nine, two].
% Your program should also work in the other direction. For example, the query
%
% listtran(X, [one, seven, six, two]).
% should succeed with
% X = [eins, sieben, sechs, zwei].
% Hint: to answer this question, first ask yourself “How do I translate the empty list of number words?”. That’s the base case. For non-empty lists,
% first traslate the head of the list, then use recursion to translate the tail.






% To solve this question use some recursion; hence base case is :

listtran([],[]).
listtran([H1|T1], [H2|T2]) :- tran(H1,H2), listtran(T1,T2).

% Solution: recursively take the head from each list, ensuring there is a
% tran pred for each.
% We are unifying for H2|T2 in essence







Test	Result
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

test_answer :-
    listtran([eins, neun, zwei], X),
    writeln(X).

test_answer :-
    listtran([], []),
    writeln('OK').

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

test_answer :-
    listtran(X, [one, seven, six, two]),
    writeln(X).

test_answer :-
    listtran(L1, L2),
    writeln('OK').

tran(1, one).
tran(2, two).
tran(3, three).

test_answer :-
    listtran([1, 2, 3], X),
    writeln(X).
