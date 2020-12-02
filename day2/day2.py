input_values = []

with open('day2input.txt') as f:
    input_values = list(f.readlines())

# Debug values ---> values = ["9-12 q: qqqxhnhdmqqqqjz", "13-14 g: ggggghggccgqfjgggg", "11-13 j: jjjjsjdjnzglfjnjjjj"]

valid_password_counter = 0
# Debug valued ---> for line in values:
for line in input_values:
    split_line = line.split(" ")
    low_value, high_value = split_line[0].split("-")
    counted_value = split_line[2].count(split_line[1].strip(":"))
    if counted_value >= int(low_value) and counted_value <= int(high_value):
        valid_password_counter += 1
print(valid_password_counter)