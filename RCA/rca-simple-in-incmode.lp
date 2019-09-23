% Trying an implementation of RCA's existential scale operator using clingo's incmode.
%  the process stops when no additional attributes can be added.
% The specific example is taken from the animal example (AOC-RCA paper).
% Animals context cannot move (no relation allowing it to),
%  so only the Site context is modified.
% Also, because Animals context does not change, the formal concepts on which
%  Site is working does not change either. So concepts only have to be computed once.
%  INPUT: contains(X,Y): object X of the site context is in relation with object Y of animal context C2.
%         site(S,X,Y): In Context Site at step S, object X is in relation with attribute Y.
%         animal(X,Y): In Context Animal, object X is in relation with attribute Y.

#include <incmode>.

#include "animals/context-animals.lp".
#include "animals/context-sites.lp".
#include "animals/relation-contains.lp".

% Site context at first step.
site(0,X,Y) :- site(X,Y).
rel(X,Y) :- contains(X,Y).

% Initial formal concepts derived from animal context.
% Since the animal context does not change, derived formal concepts remains the same,
%  hence does not depends on step k.
% If the animal context were to be changed at each step (because of a relation animal × something)
%  the concepts would have to be mined after each change.
ext(0,ath). ext(0,ant). ext(0,aph). ext(0,ano). int(0,a2).
ext(1,ath). ext(1,ase). ext(1,anc). ext(1,ano). ext(1,ani). ext(1,ant). ext(1,aph).
int(2,a4). int(2,a0). int(2,a2). int(2,a1). int(2,a3). int(2,a5).
ext(3,ath). ext(3,aph).  int(3,a4). int(3,a0). int(3,a2).
ext(4,ath).  int(4,a4). int(4,a0). int(4,a2). int(4,a3).
ext(5,ath). ext(5,ant). ext(5,aph).  int(5,a0). int(5,a2).
ext(6,ath). ext(6,ant).  int(6,a0). int(6,a2). int(6,a3).
ext(7,ase).  int(7,a4). int(7,a0). int(7,a5).
ext(8,ani). ext(8,ase). ext(8,anc).  int(8,a0). int(8,a5).
ext(9,ani).  int(9,a0). int(9,a1). int(9,a5).
ext(10,ath). ext(10,ase). ext(10,aph).  int(10,a4). int(10,a0).
ext(11,ath). ext(11,ase). ext(11,anc). ext(11,ani). ext(11,ant). ext(11,aph).  int(11,a0).

% Collect the objects from the different sources.
object(X) :- contains(X,_).
object(X) :- site(X,_).


#program step(k).

% Keep the existing attributes.
site(k,X,Y) :- site(k-1,X,Y).

% Collect the new relational attributes (corresponding to the concepts).
relattribute(N) :- ext(N,_).
relattribute(N) :- int(N,_).

% Compute the new incidence matrix of relation between object O and concept C.
% Existential scaling:
eso(k,X,C) :- object(X) ; relattribute(C) ; rel(X,V) ; ext(C,V).

% the new attributes are added to the site context.
site(k,X,C) :- eso(k,X,C).



#program check(k).
% Stops when no new attributes found with Scaling operator.
:- query(k) ; not eso(k,_,_).


% Outputs.
#show.
#show site0(C): site(k,site0,C), query(k).
#show site1(C): site(k,site1,C), query(k).
#show site2(C): site(k,site2,C), query(k).
#show site3(C): site(k,site3,C), query(k).
