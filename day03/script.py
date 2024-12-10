import re

path = "input.txt"
with open(path) as file:
    memory = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
pairs = re.findall(pattern, memory)

total = 0
for a, b in pairs:
    val = int(a) * int(b)
    total += val

print(total)


dd_total = 0
lines = memory.split('do()')
for line in lines:
    end = line.find("don't()")
    line = line[:end]
    pairs = re.findall(pattern, line)
    for a, b in pairs:
        val = int(a) * int(b)
        dd_total += val

print(f'{dd_total=}')
