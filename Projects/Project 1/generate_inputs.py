from random import randint

MIN_ITEMS, MAX_ITEMS = 3000, 3200
MIN_CAP, MAX_CAP = 1500, 40000
MIN_WEIGHT, MAX_WEIGHT = 30, 150
MIN_VALUE, MAX_VALUE = 5, 400

if __name__ == "__main__":
    for file_name in {"auto1.txt", "auto2.txt", "auto3.txt", "auto4.txt"}:
        with open(file="./Projects/Project 1/" + file_name, mode="w") as file:
            n = randint(MIN_ITEMS, MAX_ITEMS)
            capacity = randint(MIN_CAP, MAX_CAP)
            file.write(str(capacity) + "\n")
            file.write(str(n) + "\n")

            for _ in range(n):
                weight = randint(MIN_WEIGHT, MAX_WEIGHT)
                value = randint(MIN_VALUE, MAX_VALUE)
                file.write(str(weight) + " " + str(value) + "\n")
                
    print("ran")                


