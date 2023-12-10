
import re
import numpy as np

lines = []

with open("Day3/input.txt",'r') as puzzle_inp:
    for puzzle_lines in puzzle_inp.readlines():
        lines.append(puzzle_lines.strip())


pattern = re.compile(r'\d+')

TOP = 0
LEFT = 0
RIGHT = len(lines[0])-1
DOWN = len(lines)-1
SUM = 0

gears = [[[0,0] for _ in range(len(lines))] for _ in range(len(lines[0]))]

for line_id, line in enumerate(lines):
    matches = pattern.finditer(line)
    for match in matches:
        start = match.start()
        end = match.end()
        adjacent_indices = [(line_id,start-1),(line_id,end),
                            (line_id+1,start-1),(line_id-1,start-1),
                            (line_id+1,end),(line_id-1,end)]
        for i in range(start,end):
            adjacent_indices.append((line_id+1,i))
            adjacent_indices.append((line_id-1,i))
        
        for indices in adjacent_indices:
            
            if indices[0] >= TOP and indices[0] <= DOWN:
                if indices[1] >= LEFT and indices[1] <= RIGHT:
                    if lines[indices[0]][indices[1]] == "*":
                        if gears[indices[0]][indices[1]][1] == 0:
                            gears[indices[0]][indices[1]] = [int(match.group()),1]
                        else:
                            gears[indices[0]][indices[1]] = [gears[indices[0]][indices[1]][0] * int(match.group()), gears[indices[0]][indices[1]][1]+1]
    


gears_np = np.array(gears)
for gear in gears_np:
    for g in gear:
        SUM += g[0] if g[1] == 2 else 0
print(SUM)