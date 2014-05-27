# TODO(vucalur): move cube, rotations and stuff code to a separate package and leave off the alg
from copy import deepcopy
from time import sleep
import random

from cube_solver.cube import Cube
from cube_solver.mutation import mutations


PARENTS = 100
OFFSPRING = 5000


def none_solved(population):
    return not population[0][0].is_solved()  # first element is the best element


def mutate(individuals_and_applied_rotations):
    for cube, mutation_list in individuals_and_applied_rotations:
        mutation = random.choice(mutations)
        before = len(mutation_list)
        for rotation in mutation:
            rotation(cube)
            mutation_list.append(rotation.__name__)
        if before == len(mutation_list):
            print("Mutation has not taken place!")
        cube.recalculate_fitness()


def truncation_selection(population):
    population = sorted(population, key=lambda pair: (pair[0].fitness,  len(pair[1])))
    population = population[:PARENTS]
    best_guy = population[0]
    return population, best_guy


def average_mutation_length(population):
    length_sum = 0
    for cube, mutation_list in population:
        length_sum += len(mutation_list)
    return length_sum / len(population)


def best_mutation_length(population):
    best = 99999
    for cube, mutation_list in population:
        if best > len(mutation_list):
            best = len(mutation_list)
    return best


def main():
    random.seed()
    problem = Cube()
    problem.scramble()

    population = [(deepcopy(problem), []) for i in range(PARENTS)]

    print("Original problem fitness: " + str(problem.fitness))

    generations = 0
    while none_solved(population) and generations < 20:

        parents = deepcopy(population)

        # reproduction
        while len(population) < OFFSPRING:
            population.extend(deepcopy(parents))

        # mutation
        mutate(population)

        #population.extend(parents)

        # selection
        population, best_guy = truncation_selection(population)

        print("Generation: %d\tPopulation: %s\tFitness: %d\tBest_guys_mutation: %s"
              % (generations, len(population), best_guy[0].fitness, len(best_guy[1])))

        generations += 1

    print("Solved in %d generations" % generations)


if __name__ == "__main__":
    main()