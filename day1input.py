input_values = []

with open('day1file.txt') as f:
    lines = f.readlines()
    input_values = []
    for line in lines:
        input_values.append(int(line))