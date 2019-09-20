% Translation in ASP of the constraint on I+ for operator on relational scaling,
%  shown in Table 7 of RCA paper.

% Universal scaling:
eso(X,C) :- object(X) ; attribute(C) ; ext(C,V): rel(X,V).
% Strict Universal scaling:
eso(X,C) :- object(X) ; attribute(C) ; ext(C,V): rel(X,V) ; rel(X,_).
% Existential scaling:
eso(X,C) :- object(X) ; attribute(C) ; rel(X,V) ; ext(C,V).
% Cardinality restriction (min) scaling:
eso(X,C) :- object(X) ; attribute(C) ; 3 { rel(X,_) }.
% Cardinality restriction (max) scaling:
eso(X,C) :- object(X) ; attribute(C) ; { rel(X,_) } 4.
% Cardinality restriction (min & max) scaling:
eso(X,C) :- object(X) ; attribute(C) ; 3 { rel(X,_) } 4.
% Qualified Cardinality restriction (min) scaling:
eso(X,C) :- object(X) ; attribute(C) ; ext(C,V): rel(X,V) ; 3 { rel(X,_) }.
% Qualified Cardinality restriction (max) scaling:
eso(X,C) :- object(X) ; attribute(C) ; ext(C,V): rel(X,V) ; 3 { rel(X,_) } 4.
