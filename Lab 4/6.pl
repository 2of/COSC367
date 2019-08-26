

/*Do you know these wooden Russian dolls (Matryoshka dolls) where the smaller ones are contained in bigger ones? Here is a schematic picture:



First, write a knowledge base using the predicate directlyIn/2 where directlyIn(X,Y) means that X is directly in Y.
Then, define a recursive predicate contains/2 , that tells us which doll (directly or indirectly) contains which other doll.
For example, the query contains(katarina,natasha) should succeed (be true), while contains(olga, katarina) should fail.
*/





directlyIn(irina,natasha).
directlyIn(natasha,olga).
directlyIn(olga,katarina).

% contains(X,Y) :- directlyIn(X,Y).
% contains(X,Z) :- directlyIn(X,Y), contains(Y,Z).

%Note the test_answers are looking for 'contains' NOT 'is contained by'
% the above solution should yield appropriate results for that. The below includes a
% rule to swap

switch(A,B) :- directlyIn(A,B).
%Base case for recursion
switch(A,B) :- directlyIn(A,C), switch(C,B).
% The search backend will recurse until switch c,b is defined by base case
% Please do not consider alphabetical order
contains(B,A) :- switch(A,B).
%The former definitions are for 'is contained by', we can just switch with This rule

test_answer :-
    directlyIn(irina, natasha),
    writeln('OK').

test_answer :-
    \+ directlyIn(irina, olga),
    writeln('OK').

test_answer :-
    contains(katarina, irina),
    writeln('OK').

test_answer :-
    contains(katarina, natasha),
    writeln('OK').

% Here we look for all of the dolls which contain irina.

test_answer :-
    findall(P, contains(P, irina), Output),
    sort(Output, SortedOutput),
    foreach(member(X,SortedOutput), (write(X), nl)).
