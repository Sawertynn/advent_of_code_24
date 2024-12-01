import math

PATH = "input.txt"

left_list = []
right_list = []

with open(PATH, "r") as file:
    while line := file.readline():
        ids = line.split()
        values = [int(x) for x in ids]
        left_list.append(values[0])
        right_list.append(values[1])

left_list.sort()
right_list.sort()


total_diff = 0

for left, right in zip(left_list, right_list):
    diff = int(math.fabs(left - right))
    total_diff += diff

print(total_diff)