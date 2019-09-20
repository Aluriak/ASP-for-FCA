% AOC poset generation ; to be grounded with formal concept search.

% An outsider is any object or attribute linked to an attribute or object not in the concept.
ext_outsider(X):- ext(X) ; rel(X,Z) ; X!=Z ; not int(Z).
int_outsider(Y):- int(Y) ; rel(Z,Y) ; Z!=Y ; not ext(Z).
% The specific part of each concept contains no outsider.
specext(X):- ext(X) ; not ext_outsider(X).
specint(Y):- int(Y) ; not int_outsider(Y).
