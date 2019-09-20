"""Implementation of RCA"""

import clyngor
from collections import defaultdict
from fca import concepts_from_name, render_lattice
from ex_animals import CONTEXTS, RELATIONS, RELATIONS_OF_CONTEXT, CONTEXTS_TARGETED_BY_RELATION, test_function as animals_test_function


CONCEPTS = {  # step -> (context name -> asp data describing the formal concepts)
    0: {
        'site': '\n'.join(concepts_from_name(CONTEXTS, 0, 'site')),
        'animal': '\n'.join(concepts_from_name(CONTEXTS, 0, 'animal')),
    },
}


def eso_from_data(step:int, context, relation, concepts_source, show=False):
    files = 'solve-existential-scaling-operator.lp',
    concepts = CONCEPTS[step][concepts_source]
    # print('CONCEPTS:', concepts)
    eso = defaultdict(set)
    maps_predicate = f"\nrel(X,Y) :- {relation}(X,Y).  has(X,Y) :- {context}(X,Y).\n"
    data = CONTEXTS[step][context] + RELATIONS[relation] + maps_predicate + concepts
    models = clyngor.solve(files, inline=data, delete_tempfile=False).by_arity
    # print('ESO command:', models.command)
    for model in models:
        for obj, att in model.get('eso/2', ()):
            eso[obj].add(att)
    if show:
        # print('ESO:', dict(eso))
        rel_attributes = sorted(tuple(set.union(*eso.values())))
        print(' ' * max(map(len, eso)) + ''.join(str(attr).rjust(2) for attr in rel_attributes))
        for obj in sorted(tuple(eso)):
            print(obj, end='')
            for attr in rel_attributes:
                print(' X' if attr in eso[obj] else '  ', end='')
            print()
    return eso


def extend_context(step, context_name):
    new_context = CONTEXTS[step][context_name]
    for relation in RELATIONS_OF_CONTEXT.get(context_name, ()):
        concepts_source = CONTEXTS_TARGETED_BY_RELATION[relation]
        eso = eso_from_data(step, context_name, relation, concepts_source)
        for obj, attrs in eso.items():
            for att in attrs:
                # create the new attribute
                new_context += f'{context_name}({obj},{relation[0]}_c{att}).'
    return new_context

def equivalent_asp(enc1, enc2) -> bool:
    "True if given encoding yields the very same models"
    models1 = frozenset(clyngor.solve(inline=enc1))
    models2 = frozenset(clyngor.solve(inline=enc2))
    return models1 == models2

animals_test_function(eso_from_data)  # allow the example to test something, for debug

step = 0
while True:
    step += 1
    print(f'\n\n  STEP {step}\n')
    CONTEXTS[step] = {}
    CONCEPTS[step] = {}
    for context in CONTEXTS[step-1]:
        CONTEXTS[step][context] = extend_context(step-1, context)
        CONCEPTS[step][context] = '\n'.join(concepts_from_name(CONTEXTS, step, context))
        # print(f'\tNew context {context}:', CONTEXTS[step][context])
    assert set(CONTEXTS[step]) == set(CONTEXTS[step-1]), (set(CONTEXTS[step]), set(CONTEXTS[step-1]))  # same contexts are available
    if all(equivalent_asp(CONTEXTS[step-1][context_name], CONTEXTS[step][context_name])
            for context_name in CONTEXTS[step]):
        break
for context in CONTEXTS[step]:
    render_lattice(CONCEPTS[step][context], predicate=context)
