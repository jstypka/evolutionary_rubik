# TODO(vucalur): move cube, rotations and stuff code to a separate package and leave off the alg
from copy import deepcopy
import random

from cube_solver.cube import Cube
from cube_solver.mutation import mutations


INDIVIDUALS_COUNT = 1000
LAMBDA = 50


def none_solved(individuals_and_applied_rotations):
    for pair in individuals_and_applied_rotations:
        if pair[0].is_solved():
            return False
    return True


def mutate(individuals_and_applied_rotations):
    for pair in individuals_and_applied_rotations:
        mutation = random.choice(mutations)
        for rotation in mutation:
            rotation(pair[0])
            pair[1].append(rotation)


def main():
    individuals_and_applied_rotations = [(Cube(), []) for i in range(INDIVIDUALS_COUNT)]

    for pair in individuals_and_applied_rotations:
        pair[0].scramble()
        pair[0].recalculate_fitness()

    generations = 0
    while none_solved(individuals_and_applied_rotations):
        mutate(individuals_and_applied_rotations)
        for pair in individuals_and_applied_rotations:
            pair[0].recalculate_fitness()

        individuals_and_applied_rotations = sorted(individuals_and_applied_rotations, key=lambda pair: pair[0].fitness)

        generations += 1

        # drop weakest LAMBDA
        individuals_and_applied_rotations = individuals_and_applied_rotations[:-LAMBDA]

        # duplicate strongest LAMBDA
        individuals_and_applied_rotations.extend(deepcopy(individuals_and_applied_rotations[:LAMBDA]))

        lowest_fitness = individuals_and_applied_rotations[0][0].fitness
        print("Generation %d ends. Lowest fitness so far: %d" % (generations, lowest_fitness))

    print("Solved in %d generations" % generations)


if __name__ == "__main__":
    main()