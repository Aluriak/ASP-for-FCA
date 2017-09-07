"""Routines to compute the lattice from the context.

"""

import solving


def compute_concepts_for_lattice(context:str) -> str:
    all_obj, all_att = set(), set()
    for idx, model in enumerate(solving.concept_generation(context).first_arg_only, start=1):
        for obj in model['ext']:
            all_obj.add(obj)
            yield 'concept_ext({},{}).'.format(idx, obj)
        for att in model['int']:
            all_att.add(att)
            yield 'concept_int({},{}).'.format(idx, att)

    # infinum and supremum
    for att in all_att:
        yield 'concept_int({},{}).'.format('#sup', att)
    for obj in all_obj:
        yield 'concept_ext({},{}).'.format('#inf', obj)


def run(context:str) -> str:
    concepts = ''.join(compute_concepts_for_lattice(context))
    print('CONCEPTS:', concepts)

    lattice_gen = solving.lattice_generation(concepts)
    edges = tuple(next(lattice_gen)['under'])
    print('COMMAND:', lattice_gen.command)
    print('LATTICE:', edges)


if __name__ == "__main__":
    CONTEXT = 'rel((a;b;c),(d;e;f)).  rel((g;h),(i;j)).'
    # CONTEXT = """
# rel(a,(f;g)).      % a × ×
# rel(b,(g;h;j;k)).  % b   × ×   × ×
# rel(c,(i;j;k)).    % c       × × ×
# rel(d,(g;i)).      % d   ×   ×
# rel(e,(f;g;h;i)).  % e × × × ×
# """
    run(CONTEXT)
