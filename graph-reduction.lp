% ASP programs that filters out equivalences in input graph.
% INPUT:
%   - rel(X,Y):- object X is related to attribute Y.
% OUTPUT:
%   - rel(X,Y):- object X is related to attribute Y.
%   - equiv(obj,A,B):- object B is equivalent to object A (A is in the outputed graph)
%   - equiv(att,A,B):- same for attributes.

% A and B are equivalent (same neighborood).
equiv(obj,A,B):- rel(A,Y): rel(B,Y) ; rel(B,Y): rel(A,Y) ; A < B ; rel(A,_) ; rel(B,_).
equiv(att,A,B):- rel(X,A): rel(X,B) ; rel(X,B): rel(X,A) ; A < B ; rel(_,A) ; rel(_,B).

% The smaller node represent its equivalence class.
repr(E,A):- equiv(E,A,_) ; not equiv(E,_,A).

% Node in no equivalence classes represent itself.
repr(obj,X):- rel(X,_) ; not equiv(obj,X,_) ; not equiv(obj,_,X).
repr(att,Y):- rel(_,Y) ; not equiv(att,Y,_) ; not equiv(att,_,Y).

% Build the new graph.
#show.
#show rel(X,Y): rel(X,Y) ; repr(obj,X) ; repr(att,Y).
#show equiv(E,A,B): equiv(E,A,B) ; repr(E,A).
