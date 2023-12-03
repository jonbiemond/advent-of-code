"""2023 Day 3: Gear Ratios"""
import re
from itertools import islice

with open('2023/day3/input.txt', 'r') as f:
    data = f.read()

i = 0
line_len = len(data.split(maxsplit=1)[0])
data = data.replace("\n", "")
digits = re.finditer(r"\d+", data)
pattern = re.compile(r"[^.\d]")
for match in digits:
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
        i += int(match.group())

print("Part 1: ", i)
