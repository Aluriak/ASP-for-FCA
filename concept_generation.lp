% Generate formal concepts mined in an input context.
%
% This is one method. For more methods,
%  reach https://github.com/aluriak/concept-generation
%
% INPUT:
%   - rel(X,Y):- object X is in relation with attribute Y.
% OUTPUT (one model == one concept):
%   - ext(X):- X is an object of the concept (extent)
%   - int(Y):- Y is an attribute of the concept (intent)


% Generate the concept.
ext(X):- rel(X,_) ; rel(X,Y): int(Y).
int(Y):- rel(_,Y) ; rel(X,Y): ext(X).

% Avoid non-concept (no object or no attribute)
:- not ext(_).
:- not int(_).

% clingo 5.2.0 or less
% :- not ext(X):ext(X).
% :- not int(Y):int(Y).


#show.
#show ext/1.
#show int/1.
