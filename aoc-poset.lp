% AOC poset generation ; to be grounded with formal concept search.
ext_outsider(X) :- ext(X) ; {relation}(X,Z) ; X!=Z ; not int(Z).
int_outsider(Y) :- int(Y) ; {relation}(Z,Y) ; Z!=Y ; not ext(Z).
specext(X) :- ext(X) ; not ext_outsider(X).
specint(Y) :- int(Y) ; not int_outsider(Y).
