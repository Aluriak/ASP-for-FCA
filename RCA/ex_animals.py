"""Definition of the animals example data. See README and animals/"""


RELATIONS_OF_CONTEXT = {  # maps each context with the relations it share objects with
    'site': {'contains'},
}
CONTEXTS_TARGETED_BY_RELATION = {  # maps each relation with the context it share objects with
    'contains': 'animal',
}


# The process is iterative: lets redefine correctly CONTEXTS and RELATIONS.
CONTEXTS = {  # step -> (context name -> asp data)
    0: {
        'site': open('animals/context-sites.lp').read(),
        'animal': open('animals/context-animals.lp').read(),
    },
}
RELATIONS = {
    'contains': open('animals/relation-contains.lp').read(),
}



def test_function(eso_from_data:callable):
    """A small function ran at start, allowing one to test its data"""
    print('Testing of eso_from_data with hardcoded data')
    # for context, relation, concepts_source in SEQUENCE:
    eso_from_data(0, 'site', 'contains', 'animal')
