# TODO(vucalur): move cube, rotations and stuff code to a separate package and leave off the alg
from copy import deepcopy
import random

from cube_solver.cube import Cube
from cube_solver.mutation import all_mutations


MAX_GENERATIONS = 300
MAX_ALLOWED_GENERATIONS_WITHOUT_IMPROVEMENT = 40

MIN_MUTATIONS_TO_APPLY_WHEN_NO_IMPROVEMENT = 2
MAX_MUTATIONS_TO_APPLY_WHEN_NO_IMPROVEMENT = 5

PARENTS = 10
OFFSPRING = 100


def compressed(solution_original):
    solution = deepcopy(solution_original)
    has_changed = True
    while has_changed:
        has_changed = False
        i = 0
        while i < len(solution) - 1:
            a = solution[i]
            b = solution[i + 1]
            if a + 'i' == b or a == b + 'i':
                solution.pop(i + 1)
                solution.pop(i)
                has_changed = True
                i -= 2
            i += 1
    return solution


def calc_compression(solution_original):
    solution = compressed(solution_original)

    return (len(solution_original) - len(solution)) / len(solution_original)


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def fitness(individual):
    return individual[0].fitness


def solved(best_guy):
    return fitness(best_guy) == 0


def mutate(individuals_and_applied_rotations, chain_mutations=False):
    for cube, rotations_list in individuals_and_applied_rotations:

        mutations_count = 1
        if chain_mutations:
            mutations_count = random.randint(MIN_MUTATIONS_TO_APPLY_WHEN_NO_IMPROVEMENT, MAX_MUTATIONS_TO_APPLY_WHEN_NO_IMPROVEMENT)

        before = len(rotations_list)
        mutations = random.sample(all_mutations, mutations_count)
        for mutation in mutations:
            for rotation in mutation:
                rotation(cube)
                rotations_list.append(rotation.__name__)
        if before == len(rotations_list):
            print("Mutation has not taken place!")
        cube.recalculate_fitness()


def truncation_selection(population, parents):
    population = sorted(population, key=lambda individual: (fitness(individual), len(individual[1])))
    population = population[:parents]
    best_guy = population[0]
    return population, best_guy


def tournament_selection(population, parents):
    random.shuffle(population)
    global_best = population[0]
    new_population = []
    chunk_length = parents

    for group in chunks(population, chunk_length):
        local_best = min(group, key=lambda x: fitness(x))
        if fitness(local_best) < fitness(global_best):
            global_best = local_best
        new_population.append(local_best)

    return new_population, global_best


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


def run(problem=None, parents=PARENTS, offspring=OFFSPRING, use_tournament_selection=False):
    random.seed()
    if problem is None:
        problem = Cube()
        problem.scramble()

    population = [(deepcopy(problem), []) for i in range(parents)]

    selection_fn = tournament_selection if use_tournament_selection else truncation_selection

    # print("Original problem fitness: " + str(problem.fitness))

    generations = 0
    generations_without_improvement = 0
    best_guy = population[0]
    while not solved(best_guy) and generations < MAX_GENERATIONS:

        old_population = deepcopy(population)
        old_best_buy = deepcopy(best_guy)

        # reproduction
        while len(population) < offspring:
            population.extend(deepcopy(old_population))

        # mutation
        if generations_without_improvement >= MAX_ALLOWED_GENERATIONS_WITHOUT_IMPROVEMENT:
            print("Chaining mutations !")
            mutate(population, chain_mutations=True)
            generations_without_improvement = 0
        else:
            mutate(population)

        population.extend(old_population)

        # selection
        population, best_guy = selection_fn(population, parents)

        print("Generation: %d\tPopulation: %s\tFitness: %d\tBest_guy's_rotations_count: %s"
              % (generations, len(population), fitness(best_guy), len(best_guy[1])))

        # measure improvement
        if fitness(best_guy) >= fitness(old_best_buy):
            generations_without_improvement += 1
        else:
            generations_without_improvement = 0

        generations += 1

    if generations == MAX_GENERATIONS:
        return None
    else:
        # print("Solved in %d generations" % generations)
        return generations, len(best_guy[1]), calc_compression(best_guy[1])


if __name__ == "__main__":
    run()