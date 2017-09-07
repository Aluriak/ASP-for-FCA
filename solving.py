"""Routines to run solving on available asp files.

"""

import os
from functools import partial
import clyngor


AVAILABLE_ASP_ROUTINES = {
    'concept_generation',
    'lattice_generation'
}


def solve(input_data:str, asp_routine:str) -> dict:
    if os.path.exists(input_data):
        files = asp_routine, input_data
        inline = None
    else:
        files = asp_routine,
        inline = input_data
    return clyngor.solve(files, inline=input_data).by_predicate


for routine in AVAILABLE_ASP_ROUTINES:
    globals()[routine] = partial(solve, asp_routine=routine + '.lp')
