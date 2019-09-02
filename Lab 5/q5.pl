% Write a predicate remove(+X, +ListIn, ?ListOut) that succeeds if ListOut can be obtained by removing all instances
% of X from ListIn. Note that the first two arguments will always be bound (input argument).


%
% NOTE: we will require the 'append' operator here, append works as:
%     ?- append([a,b,c,d],[1,2,3,4,5], X).
%     X=[a,b,c,d,1,2,3,4,5]
%     yes
%     That is X is unified to the appending of ?1 and ?2 (first second args)


%Because this definition is recursive, let us select an appropriate base case
remove(X,[],ListOut,ListOut).
  % The base case is defined here where ListIn is exhausted and temp/ ListOut are identical

%note that we can 'return' to the 'three input' state in the next line:
remove(X,ListIn,ListOut) :- remove(X,ListIn,ListOut,[]).
remove(A,[A|T],ListOut,TempList) :- remove(A,T,ListOut,TempList).
remove(A,[B|T],ListOut,TempList) :- append(TempList,[B],L),remove(A,T,ListOut,L).

%'generate' a new list with values of B not matching A (line 4)
% Otherwise 'pop' (~) A from the list and continue (Line 3)







test_answer :-
    remove(a, [a, b, a, c, d, a, b], L),
    writeln(L).

test_answer :-
    remove(2, [2], L),
    writeln(L).

test_answer :-
    remove(d, [a, b, c], L),
    write(L).

test_answer :-
    remove(a, [], L),
    write(L).

test_answer :-
    remove(term2, [term1, term2, term3], [term1, term3]),
    write('OK').
