from cube_solver.cube import Cube
from cube_solver.rotation import F, D, L, B, U, R, Di, Li, Bi, Ui, Ri, Fi


def test_recalculate_fitness_fresh_cube():
    c = Cube()
    c.recalculate_fitness()

    assert c.fitness == 0


def test_recalculate_fitness_rotations():
    rotations = [F, R, U, B, L, D,
                 Fi, Ri, Ui, Bi, Li, Di]
    for rotation in rotations:
        c = Cube()
        rotation(c)
        c.recalculate_fitness()
        assert c.fitness == 52