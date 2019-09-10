%
%
% Write a predicate binary_number(+ListOfAtoms)
% that only succeeds if the given list of atoms is a valid
% binary number.
% We consider a binary number valid if it matches the following regex: 0b(0|(1(0|1)*)).
%
%
%

%deep brackets
is_bin([]).
is_bin([H|B]) :- H = 1, is_bin(B).
is_bin([H|B]) :- H = 0, is_bin(B).



outter([H|B]) :- H = 0, B = [].
outter([H|B]) :- H = 1, is_bin(B).


binary_number([Z,A|B]) :- Z = 0, A = 'b', outter(B).


test_answer :- binary_number([0, b, 1, 0, 1]),
               writeln('OK').
test_answer :- binary_number([0, b, 0, 1]),
                              writeln('Wrong'), halt.
test_answer :- writeln('OK').
