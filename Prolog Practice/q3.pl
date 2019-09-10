% Write a predicate max(+List, ?Max) that is true when List is a list of numbers and Max is the largest number in the list. The predicate should be false for empty lists.
% Note: this predicate is defined in the lecture notes. Try to implement it without getting much help from the notes. You can also first define a predicate max/3 that finds the maximum of two numbers and then use it to define the max/2 predicate specified here to find the maximum element in a list.
%


max([],M,M).
max([H|B],M) :- max(B,H,M).
max([H|B],C,M) :- H > C, max(B,H,M).
max([H|B],C,M) :- H =< C, max(B,C,M).





test_answer :-
    max([1, 2, 3, 4, 5], M),
    writeln(M).

test_answer :-
    max([], M),
    writeln("Max of an empty list is undefined!").
