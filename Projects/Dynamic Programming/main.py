from algorithm import Algorithm

if __name__ == "__main__":
    # setup parameters
    p = 3
    t = 15
    algo = Algorithm(pumpkins = p, targets = t)

    print("Recursive Implementation")
    algo.recursive_counter = 0      # reset counter
    num_throws = algo.recursive(algo.pumpkins, algo.targets)
    print("Worst-Case Minimum Throws:", num_throws)
    print("Recursive Calls:", algo.recursive_counter)

    print("Dynamic Implementation")
    algo.dynamic_counter = 0        # reset counter
    algo.init_table()               # & table
    algo.dynamic(p = algo.pumpkins, t = algo.targets)
    algo.print_table()
    print("Worst-Case Minimum Throws:", algo.table[p][t])
    print("Dynamic Calls:", algo.dynamic_counter)