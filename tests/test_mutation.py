from cube_solver.cube import Cube
from cube_solver.mutation import add_3_other_orientations, mutations


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


MAX_ACCEPTED_FITNESS_CHANGE = 117


def _each_mutation_changes_fitness_only_slightly(cube_factory):
    for mutation in mutations:
        cube = cube_factory()
        fitness_before = cube.fitness
        for rotation in mutation:
            rotation(cube)
        cube.recalculate_fitness()
        fitness_after = cube.fitness

        assert abs(fitness_after - fitness_before) <= MAX_ACCEPTED_FITNESS_CHANGE


def test_each_mutation_changes_fitness_only_slightly_solved_cube():
    cube_factory = lambda: Cube()
    _each_mutation_changes_fitness_only_slightly(cube_factory)


def test_each_mutation_changes_fitness_only_slightly_scrambled_cube():
    def cube_factory():
        cube = Cube()
        cube.scramble()
        return cube

    _each_mutation_changes_fitness_only_slightly(cube_factory)
