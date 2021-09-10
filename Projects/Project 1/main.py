# Project 1 - Knapsack problem
# Ally Smith
# Sept. 9, 2021
# CSCI 406
from operator import attrgetter
from random import randint

# basic item class that stores the weight, value, and their ratio
class Item:
    def __init__(self, w, v):
        self.weight = w
        self.value = v
        self.ratio = w/v

    def __repr__(self) -> str:
        string = "(weight=" + str(self.weight) + ", value=" + str(self.value) + ", ratio=" + str(self.ratio) + ")"
        return string


# function to get the powerset of a given set 
# source for this elegant solution: https://simonhessner.de/calculate-power-set-set-of-all-subsets-in-python-without-recursion/
def get_powerset(list):
    n = len(list)
    return [[list[k] for k in range(n) if i&1<<k] for i in range(2**n)]

# exhaustive approach, from provided pseudocode
def exhaustive(W, n, items):
    knapsack = []
    best_value = 0
    
    powerset = get_powerset(items)
    for subset in powerset:
        subset_value = 0
        subset_weight = 0
        for item in subset:
            subset_value += item.value
            subset_weight += item.weight
        if subset_weight <= W and subset_value > best_value:
            best_value = subset_value
            knapsack = subset
    return knapsack


# uses a built-in sorting function comparing the weight to value ratio primarily
# and the value as a secondary comparison in the event of a tie
def get_sorted_ratios(list):
    return sorted(list, key=attrgetter('ratio', 'value'))

# heuristic approach from pseudocode
def heuristic(W, n, items):
    knapsack = []
    currentW = W

    items_list = get_sorted_ratios(items)

    for item in items_list:
        if item.weight <= currentW:
            knapsack.append(item)
            currentW -= item.weight

    return knapsack

# main of program
if __name__=="__main__":
    # parameters for random item generation
    MIN_COUNT, MAX_COUNT = 3, 10
    MIN_WEIGHT, MAX_WEIGHT = 1, 10
    MIN_VALUE, MAX_VALUE = 2, 50

    NUM_LOOPS = 1000
    for _ in range(NUM_LOOPS):
        # generate some items to be in the store
        items = []
        num_items = randint(MIN_COUNT, MAX_COUNT)
        for _ in range(num_items):
            item_weight = randint(MIN_WEIGHT, MAX_WEIGHT)
            item_value = randint(MIN_VALUE, MAX_VALUE)
            item = Item(w=item_weight, v=item_value)
            items.append(item)

        # print generated items for manual calculations
        should_print = True
        if should_print:
            for item in items:
                print(item)

        # constants for testing with
        WEIGHT = 20
        heuristic_knapsack = heuristic(W=WEIGHT, n=len(items), items=items)
        heuristic_weight = heuristic_value = 0
        for item in heuristic_knapsack:
            heuristic_weight += item.weight
            heuristic_value += item.value
        print("Heuristic result:")
        print("Weight:", heuristic_weight)
        print("Value:", heuristic_value)
        exhaustive_knapsack = exhaustive(W=WEIGHT, n=len(items), items=items)
        exhaustive_weight = exhaustive_value = 0
        for item in exhaustive_knapsack:
            exhaustive_weight += item.weight
            exhaustive_value += item.value
        print("Exhaustive result:")
        print("Weight:", exhaustive_weight)
        print("Value:", exhaustive_value)

        if heuristic_value > exhaustive_value:
            break

