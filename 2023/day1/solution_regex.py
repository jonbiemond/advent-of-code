"""2023 Day 1: Trebuchet?!"""
import re

with open('2023/day1/input.txt', 'r') as f:
    data = f.read()

# Part 1
cal_vals = []

for line in data.splitlines():
    digits = [char for char in line if char.isnumeric()]
    cal_vals.append(int(digits[0] + digits[-1]))

print("Part 1: ", sum(cal_vals))


# Part 2
cal_vals = []
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

pattern = re.compile("(?=("+"|".join([r"\d"] + list(numbers.keys()))+"))")
for line in data.splitlines():
    matches = pattern.findall(line)
    cal_vals.append(
        int(
            str(numbers.get(matches[0], matches[0]))
            + str(numbers.get(matches[-1], matches[-1]))
        )
    )

print("Part 2: ", sum(cal_vals))
