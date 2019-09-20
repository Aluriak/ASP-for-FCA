% Implementation of the existential scaling operator.
% INPUT:  has(X,Y): object X holds attribute Y.
%         rel(X,Y): object X is in relation with object Y.
%         ext(N,X): object X belongs to the extent of the N-th concept.
%         int(N,Y): object Y belongs to the intent of the N-th concept.
%         relational_attr(N,A): N is the name of the relational attribute A.
% To implement the operator, extents must use the same objects found
%  in the first set/argument of relation ("Gir is the range of r").
% OUTPUT: eso(X,A): object X holds attribute A.

% Collect the objects from the different sources.
object(X) :- has(X,_).
object(X) :- rel(X,_).

range(A) :- rel(_,A).
range(A) :- ext(_,A).

% Collect the new relational attributes (corresponding to the concepts).
attribute(N) :- ext(N,_).
attribute(N) :- int(N,_).

% Compute the new incidence matrix of relation between object O and concept C.
% Existential scaling:
eso(X,C) :- object(X) ; attribute(C) ; rel(X,V) ; ext(C,V).



#show.
#show attribute/1.
#show eso/2.
