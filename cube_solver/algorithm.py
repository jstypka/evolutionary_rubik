# TODO(vucalur): move cube, rotations and stuff code to a separate package and leave off the alg
from copy import deepcopy
from time import sleep
import random

from cube_solver.cube import Cube
from cube_solver.mutation import mutations


PARENTS = 10
OFFSPRING = 50


def none_solved(population):
    return not population[0][0].is_solved()  # first element is the best element


def mutate(individuals_and_applied_rotations):
    for cube, mutation_list in individuals_and_applied_rotations:
        print("Before:", len(mutation_list))
        mutation = random.choice(mutations)
        for rotation in mutation:
            rotation(cube)
            mutation_list.append(rotation.__name__)
        print("After:", len(mutation_list))
        cube.recalculate_fitness()



def average_mutation_length(population):
    length_sum = 0
    for cube, mutation_list in population:
        length_sum += len(mutation_list)
    return length_sum / len(population)


def main():
    problem = Cube()
    problem.scramble()

    population = [(deepcopy(problem), []) for i in range(PARENTS)]

    print("Original problem fitness: " + str(problem.fitness))

    generations = 0
    while none_solved(population) and generations < 50:

        # reproduction
        while len(population) < OFFSPRING:
            population.extend(deepcopy(population))

        # mutation
        #print("Before: " + str(average_mutation_length(population)))
        mutate(population)
        #print("After: " + str(average_mutation_length(population)))

        # sort
        population = sorted(population, key=lambda pair: pair[0].fitness)

        # selection
        population = population[:PARENTS]

        best_guy = population[0]
        print("Generation: %d\tFitness: %d\tMutations: [%s]"
              % (generations, best_guy[0].fitness, ', '.join(map(str, best_guy[1]))))
        #print("Generation: %d\tPopulation: %s\tFitness: %d\tAv_mutation: %s"
        #      % (generations, len(population), lowest_fitness, average_mutation_length(population)))

        generations += 1

        sleep(1)

    print("Solved in %d generations" % generations)


if __name__ == "__main__":
    main()