#parse of input
with open('day6input.txt') as txtfile:
    input_values = [[]]
    group_counter = 0
    for line in txtfile:
        if line != "\n":
            input_values[group_counter].append(line.strip("\n"))
        elif line == "\n":
            group_counter += 1
            input_values.append([])
        else:
            print("You missed something")
            break

#part 1 solution
    def countAnswers(list):
        total_count = []
        total_sum = 0
        letters = "abcdefghijklmnopqrstuvwxyz"
        alphabet = [char for char in letters]


        for input in list:
            temp_count = 0
            used_letters = []
            for word in input:
                for letter in word:
                    if letter in alphabet and letter not in used_letters:
                        temp_count += 1
                        used_letters.append(letter)
            total_count.append(temp_count)
        for amount in total_count:
            total_sum += amount
        return total_count, total_sum
    print(countAnswers(input_values))

#part 2 solution
    def allAgree(list):

        length = 0
        total_agreed = []
        total_agree = 0

        for group in list:
            agreed = {}
            length = len(group)
            for member in group:             
                for letter in member:
                    if letter in agreed:
                        agreed[letter] += 1
                    else:
                        agreed[letter] = 1
            amount = 0
            for k, v in agreed.items():
                if agreed[k] == length:
                    amount += 1
            total_agreed.append(amount)
        for amount in total_agreed:
            total_agree += amount
        return total_agreed, total_agree
# the result should be [3, 0, 1, 1, 1] and sum 6 for devvalues. 
    print(allAgree(input_values))
