/*Let point(X,Y) represent a point in a 2D Euclidean space. Define a predicate reflection/2 that
 takes two points and is true when the two points are the reflection of each other across the line y=x. */


 reflection(point(X,Y), point(Y,X)).


 test_answer :-
	reflection(point(3, 6), point(6, 3)),
        writeln('OK').

test_answer :-
	reflection(point(-5, 8), point(X, Y)),
        writeln(point(X, Y)).
