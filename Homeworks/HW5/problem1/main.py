# input
n = 20
cuts = [3, 8, 10]
# add fake cuts
cuts = [-1] + cuts + [n - 1]
cuts_num = len(cuts)
# init table with zeros
table = []
for i in range(cuts_num):
    table += [[0] * cuts_num]
# fill table


for offset in range(2, cuts_num):
    for start in range(0, cuts_num - offset):
        end = start + offset
        table[start][end] = 1000000000 # just a big value
        for middle in range(start + 1, end):
            table[start][end] = min(table[start][end], table[
                                    start][middle] + table[middle][end])
        table[start][end] += cuts[end] - cuts[start]



# print result: 38
for row in table:
    for element in row:
        print(element, end="\t")
    print(" ")