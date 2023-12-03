"""2023 Day 3: Gear Ratios"""
import math
import re
from collections import defaultdict
from itertools import islice

with open('2023/day3/input.txt', 'r') as f:
    data = f.read()

# Part 1
n = 0
line_len = len(data.split(maxsplit=1)[0])
data = data.replace("\n", "")
numbers = re.finditer(r"\d+", data)
pattern = re.compile(r"[^.\d]")
for match in numbers:
    span = match.span()
    adjacent_chars = (
        data[span[0]-1]
        + data[span[1]]
    )
    adjacent_chars += "".join(
        islice(
            data,
            max(span[0] - line_len - 1, 0),
            max(span[1] - line_len + 1, 0),
        )
    )
    adjacent_chars += "".join(
        islice(
            data,
            span[0] + line_len - 1,
            span[1] + line_len + 1
        )
    )
    if pattern.search(adjacent_chars):
        n += int(match.group())

print("Part 1: ", n)

# Part 2
n = 0

gears = re.finditer(r"\*", data)
numbers = re.finditer(r"\d+", data)
indices = defaultdict(list[int])

for match in numbers:
    number = int(match.group())
    span = match.span()
    indices[span[0] - 1] += [number]
    indices[span[1]] += [number]
    for i in range(span[0] - 1, span[1] + 1):
        indices[i + line_len] += [number]
        indices[i - line_len] += [number]

for gear in gears:
    nums = indices.get(gear.span()[0], "")
    if len(nums) == 2:
        n += math.prod(nums)

print("Part 2: ", n)
