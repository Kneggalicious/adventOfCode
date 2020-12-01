#first sum to 2020

from day1input import input_values

for sum1 in input_values:
    for sum2 in input_values:
        if (sum1 + sum2) == 2020:
            summed = sum1 * sum2
            print(summed)

for sum1 in input_values:
    for sum2 in input_values:
        for sum3 in input_values:
            if (sum1+sum2+sum3) == 2020:
                summed = sum1 * sum2 * sum3
                print(summed)