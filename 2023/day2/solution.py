"""2023 Day 2: Cube Conundrum"""
import math

with open('2023/day2/input.txt', 'r') as f:
    data = f.read()

# Part 1
avail_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

i = 0

for line in data.splitlines():
    game_id = line.split(" ")[1][:-1]
    line = line.replace(";", ",")
    for colour in [colour.split(" ") for colour in line.split(" ", 2)[-1].split(", ")]:
        if int(colour[0]) > avail_cubes[colour[1]]:
            break
    else:
        i += int(game_id)

print("Part 1: ", i)

# Part 2
i = 0

for line in data.splitlines():
    fewest_cubes = {}
    line = line.replace(";", ",")
    for colour in [colour.split(" ") for colour in line.split(" ", 2)[-1].split(", ")]:
        fewest_cubes[colour[1]] = max(fewest_cubes.get(colour[1], 0), int(colour[0]))
    i += math.prod(fewest_cubes.values())

print("Part 2: ", i)
