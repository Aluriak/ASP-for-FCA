"""Definition of FCA functions to be used by rca.py"""

import biseau
import clyngor

# Some ASP related declarations
COMPUTE_ONLY_AOC = """
:- not specext(_) ; not specint(_).
"""
COMPUTE_AOC = """
ext_outsider(X) :- ext(X) ; {relation}(X,Z) ; X!=Z ; not int(Z).
int_outsider(Y) :- int(Y) ; {relation}(Z,Y) ; Z!=Y ; not ext(Z).
specext(X) :- ext(X) ; not ext_outsider(X).
specint(Y) :- int(Y) ; not int_outsider(Y).
"""
COMPUTE_LATTICE = """
c(N):- ext(N,_).
c(N):- int(N,_).
% Ordering of two concepts: the first has all objects of the second.
contains(C1,C2):- c(C1) ; c(C2) ; C1!=C2 ; ext(C1,X): ext(C2,X).
% Concepts linked to another in the Galois Lattice.
link(C1,C3):- contains(C1,C3) ; not link(C1,C2): contains(C2,C3).
annot(lower,X,A) :- specext(X,A).
annot(upper,X,B) :- specint(X,B).
textwrap(10).
"""
COMPUTE_CONCEPTS = """
ext(X) :- {relation}(X,_) ; {relation}(X,Y): int(Y).
int(Y) :- {relation}(_,Y) ; {relation}(X,Y): ext(X).
"""


def concepts_from_name(contexts, step:int, predicate='rel', aoc=True):
    "Computation of formal concepts from the context name and step number"
    return concepts_from_lp(contexts[step][predicate], predicate, aoc=aoc)

def concepts_from_lp(lp, predicate='rel', aoc=False):
    """Yield ext/2 and int/2 atoms describing concepts"""
    if aoc:
         lp += '\n' + COMPUTE_AOC.format(relation=predicate)
    models = clyngor.solve(inline=lp + COMPUTE_CONCEPTS.format(relation=predicate), force_tempfile=True).by_arity
    # print('CONCEPTS command:', models.command)
    for idx, model in enumerate(models):
        yield f'concept({idx}).'
        yield ' '.join(f'ext({idx},{obj}).'.format(obj) for obj, in model.get('ext/1', ()))
        yield ' '.join(f'int({idx},{att}).'.format(att) for att, in model.get('int/1', ()))
        if aoc:
            yield ' '.join(f'specext({idx},{obj}).'.format(obj) for obj, in model.get('specext/1', ()))
            yield ' '.join(f'specint({idx},{att}).'.format(att) for att, in model.get('specint/1', ()))


def render_lattice(data, predicate='rel'):
    "Use biseau to render a lattice from ASP data"
    print(f'Rendering {predicate}…')
    return biseau.compile_to_single_image(data + COMPUTE_LATTICE, outfile=f'out/{predicate}.png')
