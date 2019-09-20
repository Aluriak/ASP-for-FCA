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
    print('CONCEPTS:', ''.join(concepts))
    return lattices_edges_from_concepts(concepts)


def lattices_edges_from_concepts(concepts:iter) -> frozenset:
    concepts = concepts if isinstance(concepts, str) else ''.join(concepts)
    lattice_gen = solving.lattice_generation(concepts)
    print('COMMAND:', lattice_gen.command)
    return frozenset(next(lattice_gen)['under'])




def test_simple():
    context = 'rel((a;b;c),(d;e;f)).  rel((g;h),(i;j)).'
    expected = {('#inf', 1), ('#inf', 2), (1, '#sup'), (2, '#sup')}
    assert run(context) == expected


def test_less_simple_lattice():
    concepts = """concept_ext(1,2).concept_ext(1,3).concept_int(1,c).concept_int(1,b).concept_ext(2,1).concept_int(2,d).concept_int(2,a).concept_ext(3,1).concept_ext(3,2).concept_int(3,a).concept_ext(4,2).concept_int(4,c).concept_int(4,b).concept_int(4,a).concept_ext(5,2).concept_ext(5,3).concept_ext(5,4).concept_int(5,b).concept_ext(6,4).concept_int(6,d).concept_int(6,b).concept_ext(7,1).concept_ext(7,4).concept_int(7,d).concept_int(#sup,c).concept_int(#sup,a).concept_int(#sup,b).concept_int(#sup,d).concept_ext(#inf,1).concept_ext(#inf,2).concept_ext(#inf,3).concept_ext(#inf,4)."""
    expected = {
        ('#inf', 3), ('#inf', 5), ('#inf', 7),
        (1, 4),
        (3, 2), (3, 4),
        (5, 1), (5, 6),
        (7, 2), (7, 6),
        (2, '#sup'), (4, '#sup'), (6, '#sup'),
    }
    found = lattices_edges_from_concepts(concepts)
    assert len(found) == 13
    assert len(expected) == 13
    assert found == expected


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
