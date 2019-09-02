% Write a predicate swap_ends(?List1, ?List2) which succeeds if List1 is identical to List2 ,
% except that the first and last elements are exchanged. The predicate should fail on lists with fewer than two elements.
%
% Hint: One way to solve this problem is to use append/3.
%  You can also write this predicate without using any other predicates.



%Note: ?- append([A|B],C,D).
          % B = [],
          % D = [A|C] .

%
% %per usual, define a base case for our recursive definition:
swap_ends([], []).
swap_ends(L1, L2) :-
	append([H1 | B1], [H2], L1),
	append([H2 | B1], [H1], L2).


%NOTE: This does allow input list < 2 in size. Need to fix,


% test_answer :-
%     swap_ends([a, b, c, d, e, f], L),
%     writeln(L).
%
% test_answer :-
%     swap_ends(L1, L2),
%     writeln('OK').
%
% test_answer :-
%     swap_ends(L, [term1, term2, term3, term4]),
%     writeln(L).
%
% test_answer :-
%     swap_ends([367], L),
%     writeln('Wrong answer!').
%
% test_answer :-
%     writeln('OK').
