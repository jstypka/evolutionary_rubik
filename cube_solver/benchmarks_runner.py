import time

from cube_solver.algorithm import run
from cube_solver.cube import Cube


REPETITIONS = 10
PARENTS = [10, 20, 50]
OFFSPRING = [100, 200, 500]
USING_TOURNAMENT_SELECTION = [False, True]


def init_results_dict():
    results = {
        is_tournament: {
            parents: {
                offspring: {
                } for offspring in OFFSPRING
            } for parents in PARENTS
        }
        for is_tournament in USING_TOURNAMENT_SELECTION
    }
    return results


def avg(array):
    return sum(array) / len(array)


def main():
    problem = Cube()
    problem.scramble()

    results = init_results_dict()
    for is_tournament in USING_TOURNAMENT_SELECTION:
        for parents in PARENTS:
            for offspring in OFFSPRING:
                times = []
                generations = []
                rotations_count = []
                for i in range(REPETITIONS):
                    start = time.process_time()
                    _generations, _rotations_count = run(problem, parents, offspring, use_tournament_selection=is_tournament)
                    end = time.process_time()
                    times.append(end - start)
                    generations.append(_generations)
                    rotations_count.append(_rotations_count)
                results[is_tournament][parents][offspring] = (avg(times), avg(generations), avg(rotations_count))
                print(str(parents) + "," + str(offspring) + ": " + str(avg(times)))

    print('#' * 80 + '\n' * 2)
    print("is_tournament parents offspring time[s] generations rotations_count\n")
    for is_tournament, v1 in results.items():
        for parents, v2 in v1.items():
            for offspring, v3 in v2.items():
                print("%s\t%d\t%d\t%f\t%d\t%d" % (str(is_tournament), parents, offspring, v3[0], v3[1], v3[2]))


if __name__ == "__main__":
    main()
