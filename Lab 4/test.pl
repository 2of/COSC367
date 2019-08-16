% directlyIn(katarina,olga).
% directlyIn(olga,natasha).
% directlyIn(natasha,irina).
% contains(X,Y) :- directlyIn(X,Y).
% contains(X,Y) :- directlyIn(X,Z), contains(Z,Y).


directlyIn(irina,natasha).
directlyIn(natasha,olga).
directlyIn(olga,katarina).

flub(A,B) :- directlyIn(A,B).
flub(A,B) :- directlyIn(A,C), flub(C,B).
contains(B,A) :- flub(A,B).
