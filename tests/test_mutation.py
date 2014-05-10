from cube_solver.mutation import add_3_other_orientations


def test_add_3_other_orientations():
    orientations = {
        'F': {'F': 1, 'B': 2, 'R': 3, 'U': 4, 'L': 5, 'D': 6}
    }
    expected = {
        'F': {'F': 1, 'B': 2, 'R': 3, 'U': 4, 'L': 5, 'D': 6},
        'F1': {'F': 1, 'B': 2, 'R': 4, 'U': 5, 'L': 6, 'D': 3},
        'F2': {'F': 1, 'B': 2, 'R': 5, 'U': 6, 'L': 3, 'D': 4},
        'F3': {'F': 1, 'B': 2, 'R': 6, 'U': 3, 'L': 4, 'D': 5},
    }

    add_3_other_orientations(orientations)
    assert orientations == expected