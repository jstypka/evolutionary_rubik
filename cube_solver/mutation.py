from copy import deepcopy
import re

import cube_solver.rotation
from cube_solver.rotation import *


_orientations = {
    'F': {'F': F, 'B': B, 'R': R, 'U': U, 'L': L, 'D': D},
    'R': {'F': R, 'B': L, 'R': B, 'U': U, 'L': F, 'D': D},
    'U': {'F': U, 'B': D, 'R': R, 'U': B, 'L': L, 'D': F},
    'B': {'F': B, 'B': F, 'R': L, 'U': U, 'L': R, 'D': D},
    'L': {'F': L, 'B': R, 'R': F, 'U': U, 'L': B, 'D': D},
    'D': {'F': D, 'B': U, 'R': R, 'U': F, 'L': B, 'D': B}
}


def add_3_other_orientations(orientations):
    ruld = ['R', 'U', 'L', 'D']
    for original_name, original_mapping in deepcopy(orientations).items():
        for shift in range(1, 4):
            shifted_ruld = ruld[shift:] + ruld[:shift]
            shifted_mapping = {r: original_mapping[s_r] for r, s_r in zip(ruld, shifted_ruld)}
            shifted_mapping['F'] = original_mapping['F']
            shifted_mapping['B'] = original_mapping['B']
            orientations[original_name + str(shift)] = shifted_mapping


add_3_other_orientations(_orientations)


def add_inverted_rotations(orientations):
    name_by_function = {F: 'F', B: 'B', R: 'R', U: 'U', L: 'L', D: 'D'}

    for k, rotations_mapping in deepcopy(orientations).items():
        for k_inner, v_inner in rotations_mapping.items():
            # FIXME: warning - reflection. Dragons be here:
            inverted_k = k_inner + 'i'
            inverted_v_name = name_by_function[v_inner] + 'i'
            inverted_v = cube_solver.rotation.__dict__[inverted_v_name]
            orientations[k][inverted_k] = inverted_v


add_inverted_rotations(_orientations)

_magic_moves = [
    'FRBLULiUBiRiFiLiUiLUi',
    'FiLiBiRiUiRUiBLFRURiU',
    'LDiLiFiDiFUFiDFLDLiUi',
    'RiDRFDFiUiFDiFiRiDiRU',
    'UFFUiRiDiLiFFLDR',
    'UiFFULDRFFRiDiLi',
    'RiURUiRiUFRBiRBRFiRR',
    'LUiLiULUiFiLiBLiBiLiFLL',
    'FiUBUiFUBiUi',
    'FUiBiUFiUiBU',
    'RLiUURiLFF',
    'LiRUULRiFF'
]

# translate "magic moves" them to a sequence (tuple) of rotate functions to apply.
# Also take into account symmetrical reflections of these moves:
def add_symmetrical_sequences(magic_moves, orientations):
    mutations = []
    for move in magic_moves:
        rotations_of_a_magic_move = re.findall("[A-Z][a-z]?", move)  # split to singe rotations (split on capital letters)
        for rotations_mapping in orientations.values():
            mutation = tuple(rotations_mapping[r] for r in rotations_of_a_magic_move)
            mutations.append(mutation)
    return mutations


all_mutations = add_symmetrical_sequences(_magic_moves, _orientations)

rotate_functions = [F, B, R, U, L, D]






























