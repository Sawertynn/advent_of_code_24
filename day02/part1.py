"""
how many reports are safe?
report (line) is safe if:
- values are all increasing or all decreasing
- changes in value is from 1 to 3
1 3 5 -> safe
1 5 7 -> unsafe
2 4 3 -> unsafe
"""

import numpy as np

def is_safe(record: list[int]) -> bool:
    if len(record) < 2:
        return True
    
    differences = np.array([right - left for left, right in zip(record[:-1], record[1:])])
    
    if np.any(differences < 0) and np.any(differences > 0):
        return False
    
    if np.any(np.abs(differences) < 1) or np.any(np.abs(differences) > 3):
        return False
    
    return True

def is_safe_with_tolerance(record: list[int]) -> bool:
    if is_safe(record):
        return True
    
    for ommited in range(len(record)):
        new_record = record[:ommited] + record[ommited+1:]
        if is_safe(new_record):
            return True
    
    return False


input_path = 'input.txt'
with open(input_path) as file:
    lines = file.readlines()

safe_counter = 0
tolerant_counter = 0
for line in lines:
    record = [int(x) for x in line.split()]
    safe_counter += int(is_safe(record))
    tolerant_counter += int(is_safe_with_tolerance(record))

print(f'No tolerance: {safe_counter}')
print(f'Single tolerance: {tolerant_counter}')