class Algorithm:
    def init_table(self):
        self.table = [[None] * self.targets for _ in range(self.pumpkins)]

    def __init__(self, pumpkins: int, targets: int):
        self.recursive_counter = 0
        self.dynamic_counter = 0
        self.pumpkins = pumpkins
        self.targets = targets
        self.init_table()

    def print_table(self):
        for r in range(self.pumpkins):
            for c in range(self.targets):
                print(self.table[r][c], end="\t")
                # print("(",r, c, self.table[r][c], ")", end="\t")
            print()

    def fill_table(self) -> None:
        for r in range(self.pumpkins):
            for c in range(self.targets):
                self.dynamic(p=r + 1, t=c + 1)

    def recursive(self, p: int, t: int) -> int:
        self.recursive_counter += 1
        if (t == 0 or t == 1):
            return t
        if (p == 1):
            return t

        results = []  # list to hold calculated costs, used to choose minimum
        for x in range(1, t + 1):
            breaksCase = self.recursive(p=p - 1, t=x - 1)
            intactCase = self.recursive(p=p, t=t - x)
            maxThrows = max(breaksCase, intactCase)
            results.append(maxThrows)
        results.sort()
        return 1 + results[0]

    def dynamic(self, p: int, t: int):
        self.dynamic_counter += 1
        if (t == 0 or t == 1):
            self.table[p - 1][t - 1] = t
            return
        if (p == 1):
            self.table[p - 1][t - 1] = t
            return

        results = []
        for x in range(1, t + 1):
            breaks_case = 5
            intact_case = 4
            try:
                if self.table[p - 2][x - 2] == None:
                    self.dynamic(p=p - 1, t=x - 1)
                breaks_case = self.table[p - 2][x - 2]

                if self.table[p - 1][t - x - 1] == None:
                    self.dynamic(p=p, t=t - x)
                intact_case = self.table[p - 1][t - x - 1]
            except IndexError as e:
                print(p, x)
                exit(-5)

            max_throws = max(breaks_case, intact_case)
            results.append(max_throws)
        results.sort()

        self.table[p - 1][t - 1] = 1 + results[0]


if __name__ == "__main__":
    # setup parameters
    p = 3
    t = 16
    algo = Algorithm(pumpkins=p, targets=t)

    RECURSIVE = False
    if RECURSIVE:
        print("Recursive Implementation")
        algo.recursive_counter = 0  # reset counter
        num_throws = algo.recursive(algo.pumpkins, algo.targets)
        print("Worst-Case Minimum Throws:", num_throws)
        print("Recursive Calls:", algo.recursive_counter)

    DYNAMIC = True
    if DYNAMIC:
        print("Dynamic Implementation")
        algo.dynamic_counter = 0  # reset counter
        algo.init_table()  # reset table
        algo.fill_table()
        # algo.dynamic(p=algo.pumpkins, t=algo.targets)
        algo.print_table()
        print("Worst-Case Minimum Throws:", algo.table[p - 1][t - 1])
        print("Dynamic Calls:", algo.dynamic_counter)