with open('day5input.txt') as txtfile:
    input_values = [item.strip("\n") for item in txtfile]

    def getSeat(boardingpass):
        FBvalue = boardingpass[:7]
        LRvalue = boardingpass[7:]
        rows = [[row] for row in range(128)]
        columns = [[col] for col in range(8)]

        while len(FBvalue) > 0:
            sliceIndex = len(rows) // 2
            if FBvalue[0] == "F":
                FBvalue = FBvalue[1:]
                rows = rows[:sliceIndex]

            elif FBvalue[0] == "B":
                FBvalue = FBvalue[1:]
                rows = rows[sliceIndex:]

            else:
                print("Wrong value! got {} from {}".format(FBvalue[0], boardingpass))

        while len(LRvalue) > 0:
            sliceIndex = len(columns) // 2
            if LRvalue[0] == "L":
                LRvalue = LRvalue[1:]
                columns = columns[:sliceIndex]

            elif LRvalue[0] == "R":
                LRvalue = LRvalue[1:]
                columns = columns[sliceIndex:]

            else:
                print("Wrong value! got {} from {}".format(LRvalue[0], boardingpass))
        return rows[0][0], columns[0][0], boardingpass

    def getHighestID(list):
        highestID = 0

        for item in list:
            r,c, boardingpass = getSeat(item)
            newHigh = r * 8 + c
            if newHigh > highestID:
                highestID = newHigh
        return highestID
    
    #part 1 solution under
    print(getHighestID(input_values))