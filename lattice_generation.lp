% Generate the concept lattice of an input context.
%
% INPUT:
%   - concept_ext(N,X):- object X is in extent of concept N.
%   - concept_int(N,Y):- attribute X is in intent of concept N.
% OUTPUT (one model == one concept):
%   - ext(X):- X is an object of the concept (extent)
%   - int(Y):- Y is an attribute of the concept (intent)


% Concepts.
concept(N):- concept_ext(N,_).
concept(N):- concept_int(N,_).

% Ordering of two concepts.
smaller(C1,C2):- concept(C1) ; concept(C2) ; C1!=C2 ; concept_ext(C1,X): concept_ext(C2,X) ; concept_int(C2,Y): concept_int(C1,Y).

% C1 is under C2 if there is no concepts between them.
under(C1,C3):- smaller(C1,C3) ; not concept(C2): smaller(C1,C2) , smaller(C2,C3).


#show.
#show under/2.
#show smaller/2.
