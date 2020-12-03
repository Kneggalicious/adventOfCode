with open('day3input.txt') as f:
    input_values = list(f.readlines())
    stripped_values = []
    for line in input_values:
        stripped_values.append(line.strip("\n"))

    trees = 0
    x = 0
    for y in range(len(stripped_values)):
        if y == 0:
            pass
        else:
            if x + 3 > len(stripped_values[y])-1:
                x = (x + 3) - (len(stripped_values[y])) 
                if stripped_values[y][x] == "#":
                    trees += 1                
            else: 
                x += 3
                if stripped_values[y][x] == "#":
                    trees += 1
    
    print(trees)
