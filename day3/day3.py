with open('day3input.txt') as f:
    input_values = list(f.readlines())
    stripped_values = []
    for line in input_values:
        stripped_values.append(line.strip("\n"))

# part 1
    def slope_calc(stepx):
        trees = 0
        x = 0
        for y in range(0,len(stripped_values)):
            if y == 0:
                pass
            else:
                if x + stepx > len(stripped_values[y])-1:
                    x = (x + stepx) - (len(stripped_values[y])) 
                    if stripped_values[y][x] == "#":
                        trees += 1                
                else: 
                    x += stepx
                    if stripped_values[y][x] == "#":
                        trees += 1
        return trees

# part 2
    def slope_calc_y(stepx, stepy):
        trees = 0
        x = 0
        for y in range(0,len(stripped_values), stepy):
            if y == 0:
                pass
            else:
                if x + stepx > len(stripped_values[y])-1:
                    x = (x + stepx) - (len(stripped_values[y])) 
                    if stripped_values[y][x] == "#":
                        trees += 1                
                else: 
                    x += stepx
                    if stripped_values[y][x] == "#":
                        trees += 1
        return trees

    print(slope_calc(1))
    print(slope_calc(3))
    print(slope_calc(5))
    print(slope_calc(7))
    print(slope_calc_y(1, 2))

