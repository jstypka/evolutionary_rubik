from cube_solver.cube import Cube


def test_recalculate_fitness_fresh_cube():
    c = Cube()
    c.recalculate_fitness()

    assert c.fitness == 0