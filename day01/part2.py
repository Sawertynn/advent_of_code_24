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


similarity_score = 0

for left in left_list:
    right = right_list.count(left)
    similarity_score += left * right

print(similarity_score)