from time import time_ns
from typing import List


class Algorithm:
    # initializes all values in the table to None
    def init_table(self):
        self.table = [[None] * self.targets for _ in range(self.pumpkins)]

    def __init__(self, pumpkins: int, targets: int):
        self.recursive_counter = 0
        self.dynamic_counter = 0
        self.pumpkins = pumpkins
        self.targets = targets
        self.init_table()

    # prints out values in the table separated by a tab character
    def print_table(self):
        for r in range(self.pumpkins):
            for c in range(self.targets):
                print(self.table[r][c], end="\t")
            print()

    # runs the dynamic algorithm on each spot in the table
    def fill_table(self) -> None:
        for r in range(self.pumpkins):
            for c in range(self.targets):
                self.dynamic(p=r + 1, t=c + 1)

    # recursive algorithm
    def recursive(self, p: int, t: int) -> int:
        self.recursive_counter += 1  # increment counter for report
        # base cases
        if (t == 0 or t == 1):
            return t
        if (p == 1):
            return t

        # general cases for all values of x from 1 to t, inclusive
        results = []  # list to hold calculated costs, used to choose minimum
        for x in range(1, t + 1):
            breaksCase = self.recursive(p=p - 1, t=x - 1)
            intactCase = self.recursive(p=p, t=t - x)
            maxThrows = max(breaksCase,
                            intactCase)  # maximum of the two cases is chosen
            results.append(maxThrows)
        results.sort()  # sorts in place in ascending order
        return 1 + results[
            0]  # gets the minimum value from all values of x + 1

    # dynamic programming algorithm
    def dynamic(self, p: int, t: int):
        self.dynamic_counter += 1  # implement counter for report
        # base cases
        if (t == 0 or t == 1):
            self.table[p - 1][t - 1] = t
            return
        if (p == 1):
            self.table[p - 1][t - 1] = t
            return

        # general case for all values of x from 1 to t
        results = []
        for x in range(1, t + 1):
            # if the value is none, it is calculated by calling the dynamic function on that spot
            if self.table[p - 2][x - 2] == None:
                self.dynamic(p=p - 1, t=x - 1)
            # after that, the value is read for comparison
            breaks_case = self.table[p - 2][x - 2]

            # same as above but for the case where the pumpkin stays intact
            if self.table[p - 1][t - x - 1] == None:
                self.dynamic(p=p, t=t - x)
            intact_case = self.table[p - 1][t - x - 1]

            max_throws = max(breaks_case, intact_case)
            results.append(max_throws)
        results.sort()

        # assigns minimum value to the table slot corresponding to p and t
        self.table[p - 1][t - 1] = 1 + results[0]

    # input: num of pumpkins and targets to be traced
    # call after filling table for correct functionality
    def traceback(self, p: int , t: int):
        # base cases
        if (t == 0 or t == 1):
            return [t]
        if (p == 1):
            return list(range(1, t+1))        
        min_val = 1e9
        min_x = -1
        for x in range(1, t + 1):
            breaks_case = self.table[p - 2][x - 2]
            intact_case = self.table[p - 1][t - x - 1]
            max_val = max(breaks_case, intact_case)
            if max_val <= min_val:
                min_val = max_val
                min_x = x
                multiplier = -1 if breaks_case > intact_case else 1

        if multiplier == -1: # breaks case
            return self.traceback(p=p-1,t=min_x-1) + [multiplier*t]
        else: # intact
            return self.traceback(p=p, t=t-min_x) + [multiplier*t]

if __name__ == "__main__":
    # setup parameters
    p = 3
    t = 19
    algo = Algorithm(pumpkins=p, targets=t)

    RECURSIVE = False
    if RECURSIVE:
        print("Recursive Implementation")
        algo.recursive_counter = 0  # reset counter
        num_throws = algo.recursive(algo.pumpkins, algo.targets)
        print("Worst-Case Minimum Throws:", num_throws)
        print("Recursive Calls:", algo.recursive_counter)

    DYNAMIC = False
    if DYNAMIC:
        print("Dynamic Implementation")
        algo.dynamic_counter = 0  # reset counter
        algo.init_table()  # reset table
        algo.fill_table()
        print("Filled Table:")
        algo.print_table()
        print("Traceback:")
        print(algo.traceback(p=p, t=t))
        print("Worst-Case Minimum Throws:", algo.table[p - 1][t - 1])
        print("Dynamic Calls:", algo.dynamic_counter)