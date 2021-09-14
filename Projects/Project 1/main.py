# Project 1 - Knapsack problem
# Ally Smith
# Sept. 9, 2021
# CSCI 406
import time

# basic item class that stores the weight, value, and their ratio
class Item:
    def __init__(self, w, v):
        self.weight = w
        self.value = v
        self.ratio = v/w

    def __eq__(self, o):
        return (self.value == o.value and self.weight == o.weight)

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
def get_sorted_ratios(input_list):
    return sorted(input_list, key=lambda x: (x.ratio, x.value))

# heuristic approach from pseudocode
def heuristic(W, n, items):
    knapsack = []
    currentW = W

    items_list = get_sorted_ratios(items)
    # reverse the list (in place) so the highest ratios are encountered first
    items_list.reverse()

    for item in items_list:
        if item.weight <= currentW:
            knapsack.append(item)
            currentW -= item.weight

    return knapsack

# function to read in a file
# returns a tuple of (weight_capacity, num_items, items_list)
def generate_inputs(file_name):
    file_path = "./Projects/Project 1/" + file_name
    file = open(file=file_path, mode="r")
    weight_capacity = 0
    num_items = 0
    items = []

    for i, line in enumerate(file):
        if i == 0:
            weight_capacity = int(line)
        elif i == 1:
            num_items = int(line)
        else:
            values = line.split()
            weight = int(values[0])
            value = int(values[1])
            new_item = Item(w=weight, v=value)
            items.append(new_item)

    return (weight_capacity, num_items, items)

# main of program
EXHAUSTIVE = False
HEURISTIC = True
if __name__=="__main__":
    for file_name in {"auto1.txt", "auto2.txt", "auto3.txt", "auto4.txt"}:
    # for file_name in {"21.txt", "17.txt", "24.txt", "12.txt"}:
        print("\n\n", file_name)
        result = generate_inputs(file_name=file_name)
        weight = result[0]
        num_items = result[1]
        items = result[2]
        selected_indexes = []

        # print("\n")
        # print(weight)
        # print(num_items)
        # print(items)
        # print("\n")

        if HEURISTIC:
            print("Heuristic result:")
            start_time = time.time_ns()
            heuristic_knapsack = heuristic(W=weight, n=num_items, items=items)
            heuristic_time = time.time_ns() - start_time
            heuristic_value = 0
            for item in heuristic_knapsack:
                heuristic_value += item.value
                for i in range(len(items)):
                    if item == items[i]:
                        # print("\t" + str(item), str(i))
                        selected_indexes.append(i)
            selected_indexes.sort()
            print("Value:", heuristic_value)
            print("Selected:", selected_indexes)
            print("Time:", heuristic_time)
            selected_indexes.clear()
            print("\n")

        if EXHAUSTIVE:
            print("Exhaustive result:")
            start_time = time.time_ns()
            exhaustive_knapsack = exhaustive(W=weight, n=num_items, items=items)
            exhaustive_time = time.time_ns() - start_time
            exhaustive_value = 0
            for item in exhaustive_knapsack:
                exhaustive_value += item.value
                for i in range(len(items)):
                    if item == items[i]:
                        selected_indexes.append(i)
            print("Value:", exhaustive_value)
            selected_indexes.sort()
            print("selected:", selected_indexes)
            print("Time:", exhaustive_time)
            print("\n")

        if HEURISTIC and EXHAUSTIVE and heuristic_value > exhaustive_value:
            exit
    print("ran")
    

