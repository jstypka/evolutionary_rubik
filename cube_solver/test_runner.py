from cube_solver.algorithm import run
from time import clock

REPETITIONS = 10
PARENTS = [10, 20, 50]
OFFSPRING = [100, 200, 500]

def main():
    results = dict()
    for parents in PARENTS:
        for offspring in OFFSPRING:
            times = []
            for i in range(REPETITIONS):
                start = clock()
                run(parents, offspring)
                end = clock()
                times.append(end - start)
            avg = sum(times) / len(times)
            results[(parents, offspring)] = avg
            print(str(parents) + "," + str(offspring) + ": " + str(avg))

    for parents, offspring in results:
        print(str(parents) + "," + str(offspring) + ": " + str(results[(parents, offspring)]))


if __name__ == "__main__":
    main()
