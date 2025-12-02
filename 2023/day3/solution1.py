import re


lines = []

with open("Day3/test.txt",'r') as puzzle_inp:
    for puzzle_lines in puzzle_inp.readlines():
        lines.append(puzzle_lines.strip())


pattern = re.compile(r'\d+')

TOP = 0
LEFT = 0
RIGHT = len(lines[0])-1
DOWN = len(lines)-1

SUM = 0
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
                    if lines[indices[0]][indices[1]] != '.':

                        print(match.group(),lines[indices[0]][indices[1]])

                        SUM += int(match.group())


print(SUM)