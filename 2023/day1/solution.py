"""2023 Day 1: Trebuchet?!"""

with open('2023/day1/input.txt', 'r') as f:
    data = f.read()

# Part 1
cal_vals = []

for line in data.splitlines():
    digits = [char for char in line if char.isnumeric()]
    cal_vals.append(int(digits[0] + digits[-1]))

print("Part 1: ", sum(cal_vals))


# Part 2
def first_numeric(string: str, num_map: dict[str, int]) -> str:
    string_start = ""
    for char in string:
        if char.isnumeric():
            return char
        string_start += char
        for word, digit in num_map.items():
            if word in string_start:
                return str(digit)


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
numbers_r = {word[::-1]: digit for word, digit in numbers.items()}
for line in data.splitlines():
    cal_vals.append(
        int(
            first_numeric(line, numbers)
            + first_numeric(line[::-1], numbers_r)
        )
    )

print("Part 2: ", sum(cal_vals))
