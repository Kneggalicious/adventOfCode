with open('day2input.txt') as f:
    input_values = list(f.readlines())
    # part 1

    # values = ["9-12 q: qqqxhnhdmqqqqjz", "13-14 g: ggggghggccgqfjgggg", "11-13 j: jjjjsjdjnzglfjnjjjj"] <--- Debug values

    valid_password_counter1 = 0
    # for line in values: <--- Debug values
    for line in input_values:
        split_line = line.split(" ")
        low_value, high_value = split_line[0].split("-")
        counted_value = split_line[2].count(split_line[1].strip(":"))
        if counted_value >= int(low_value) and counted_value <= int(high_value):
            valid_password_counter1 += 1
    print(valid_password_counter1)

    #part 2 

    # first one: 12 is a hit, second one: no hits, third one: 11 is a hit, fourth one: has 2 hits <--- Debug values
    #values = ["9-12 q: qqqxhnhdmqqqqjz", "13-14 g: ggggghggccgqfjgggg", "11-13 j: jjjjsjdjnzjglfjnjjjj", "5-7 h: foilhnh"] <--- Debug values

    valid_password_counter2 = 0
    #for line in values: <--- Debug values
    for line in input_values:
        split_line = line.split(" ")
        pos_1, pos_2 = split_line[0].split("-")
        char_value = split_line[1].strip(":")
        check_pos_1 = split_line[2][int(pos_1)-1]
        check_pos_2 = split_line[2][int(pos_2)-1]
        if (check_pos_1 == char_value and not check_pos_2 == char_value) or (check_pos_2 == char_value and not check_pos_1 == char_value):
            valid_password_counter2 += 1
    print(valid_password_counter2)