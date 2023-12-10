
# ids : possible games
# red, green, blue

games = []
with open("Day2/test.txt",'r') as puzzle_inp:
    for game in puzzle_inp.readlines():
        games.append(game[:-1])


sum = 0
for game in games:
    game = game[5:]
    gid = game.split(":")[0]
    subgames = game.split(":")[1].replace(" ","").split(";")
    red = blue = green = 0
    for cubes in subgames:
        for cube in cubes.split(","):
            if "red" in cube:
                curr_red = int(cube.split("red")[0])
                red =  curr_red if curr_red > red else red
            elif "blue" in cube:
                curr_blue = int(cube.split("blue")[0])
                blue = curr_blue if curr_blue > blue else blue
            elif "green" in cube:
                curr_green = int(cube.split("green")[0])
                green = curr_green if curr_green > green else green
    if red <= 12 and green <= 13 and blue <= 14:
        sum += int(gid)

print(sum)