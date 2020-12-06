import re

with open('day4input.txt') as txtfile:
    input_values = list(txtfile.readlines())

    stripped_values = []
    for line in input_values:
        stripped_values.append(line.strip('\n'))

    nested_values = [[]]
    x = 0
    for values in stripped_values:
        if len(values) > 0:
            if values.find(" ") != -1:
                values_splitted = values.split(" ")
                for line in values_splitted:
                    nested_values[x].append(line)
            else:
                nested_values[x].append(values)
        else:
            nested_values.append([])
            x += 1

#part 2 function that validates the passports

    def passportDataCheck(listvalue):
        eclRegex = re.compile(r'^ecl:(amb|blu|brn|gry|grn|hzl|oth)$')
        hclRegex = re.compile(r'^hcl:#(\w{5}[0-9a-f])$')
        returnValue = None
        for value in listvalue:
            if "ecl" in value:
                mo = eclRegex.search(value)
                if mo == None:
                    returnValue = False
                    break
                else:
                    returnValue = True
            elif "byr" in value:
                if int(value[4:]) >= 1920 and int(value[4:]) <= 2002:
                    returnValue = True
                else:
                    returnValue = False
                    break
            elif "eyr" in value:
                if int(value[4:]) >= 2020 and int(value[4:]) <= 2030:
                    returnValue = True
                else:
                    returnValue = False
                    break
            elif "iyr" in value:
                if int(value[4:]) >= 2010 and int(value[4:]) <= 2020:
                    returnValue = True
                else:
                    returnValue = False
                    break
            elif "pid" in value:
                if len(value[4:]) == 9 and type(int(value[4:])) == int:
                    returnValue = True
                else:
                    returnValue = False
                    break
            elif "cid" in value:
                continue
            elif "hcl" in value:
                mo = hclRegex.search(value)
                if mo == None:
                    returnValue = False
                    break
                else:
                    returnValue = True
            elif "hgt" in value:
                if "in" in value and len(value) == 8 and (int(value[4:6]) >= 59 and int(value[4:6]) <= 76):
                    returnValue = True
                elif "cm" in value and len(value) == 9 and (int(value[4:7]) >= 150 and int(value[4:7]) <= 193):
                    returnValue = True
                else:
                    returnValue = False
                    break
            else:
                print("uncaught value: {}".format(value))
                break
        return returnValue



# Part 1 function return valid passports and invalid
# containct part 2 function that validates the "valid" passports -> passportDataCheck

    def passportValidator(passport_list):
        validPassport = 0
        invalidPassport = 0
        for passport in passport_list:
            if len(passport) == 8 and passportDataCheck(passport):
                validPassport += 1
            elif len(passport) <= 6:
                invalidPassport += 1
            else:
                if any('cid' in s for s in passport):
                    invalidPassport += 1
                else:
                    if passportDataCheck(passport): 
                        validPassport += 1
                    else:
                        invalidPassport += 1
        return validPassport, invalidPassport


    print(passportValidator(nested_values))
