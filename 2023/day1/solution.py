"""2023 Day 1: Trebuchet?!"""

with open('2023/day1/input.txt', 'r') as f:
    data = f.read()

cal_vals = []

for line in data.splitlines():
    digits = [char for char in line if char.isnumeric()]
    cal_vals.append(int(digits[0] + digits[-1]))

print("Part 1: ", sum(cal_vals))
