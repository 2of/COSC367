% Here are six Italian words:
%
% astante , astoria , baratto , cobalto , pistola , statale .
%
% They have to be assigned to rows and columns (crossword puzzle fashion) in the following grid:
%
%
%
% The following knowledge base represents a lexicon containing these words:
%
% word(astante, a,s,t,a,n,t,e).
% word(astoria, a,s,t,o,r,i,a).
% word(baratto, b,a,r,a,t,t,o).
% word(cobalto, c,o,b,a,l,t,o).
% word(pistola, p,i,s,t,o,l,a).
% word(statale, s,t,a,t,a,l,e).
% Write a predicate solution/6 in the form of solution(V1,V2,V3,H1,H2,H3) that tells us how to fill in the grid.
%
% Notes
% In this question, the same word can appear in different rows or columns. [As an additional exercise for yourself, think what rule needs to be added in order to have each word used only once.]
% The rules you provide will be used with different sets of six-letter words.
% Prolog has some facilities that make it possible to solve this sort of problems in simpler ways but at this stage we have to solve it in a somewhat tedious way (you need some copy and paste).

%


solution(V1,V2,V3,H1,H2,H3) :-
 word(V1, _, V12, _, V14, _, V16, _),
 word(V2, _, V22, _, V24, _, V26, _),
 word(V3, _, V32, _, V34, _, V36, _),
 word(H1, _, V12, _, V22, _, V32, _),
 word(H2, _, V14, _, V24, _, V34, _),
 word(H3, _, V16, _, V26, _, V36, _).

%Note V1 V2, H1 .. ETC are all WORDS not letters.
%hence we have to manually figure out the overlapping blocks.
%In the above grid we can see the variables under H1, H2 mirror those in V1... 

word(astante, a,s,t,a,n,t,e).
word(astoria, a,s,t,o,r,i,a).
word(baratto, b,a,r,a,t,t,o).
word(cobalto, c,o,b,a,l,t,o).
word(pistola, p,i,s,t,o,l,a).
word(statale, s,t,a,t,a,l,e).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
    halt.


word(abalone,a,b,a,l,o,n,e).
word(abandon,a,b,a,n,d,o,n).
word(enhance,e,n,h,a,n,c,e).
word(anagram,a,n,a,g,r,a,m).
word(connect,c,o,n,n,e,c,t).
word(elegant,e,l,e,g,a,n,t).

test_answer :-
    findall((V1,V2,V3,H1,H2,H3), solution(V1,V2,V3,H1,H2,H3), L),
    sort(L,S),
    foreach(member(X,S), (write(X), nl)).

test_answer :- write('Wrong answer!'),
    halt.
