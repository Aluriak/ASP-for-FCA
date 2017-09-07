% Algebraic notions on formal concepts.
% Implementation of weak negation, weak opposition


% Object and attributes.
obj(X):- concept_ext(_,X).
att(Y):- concept_int(_,Y).

% Concepts.
concept(N):- concept_ext(N,_).
concept(N):- concept_int(N,_).

% Derivation operator on single elements.
derobj(X,A):- rel(X,A).
deratt(Y,O):- rel(O,Y).


% ????
toname_ext(N,O):- concept_ext(N,O) ; not att(A): derobj(O,A), concept_int(N,A).
toname_int(N,A):- concept_int(N,A) ; not obj(O): deratt(A,O), concept_ext(N,O).

% Property oriented concept lattice.
propor_ext(N,O):- concept_ext(N,O) ; concept_int(N,A): derobj(O,A).
propor_int(N,A):- concept_int(N,A) ; concept_ext(N,O): deratt(A,O).

