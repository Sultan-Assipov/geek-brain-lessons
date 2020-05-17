import functools
import math


# task 1: see script

# # task 2
input_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
output_list = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
print(output_list)

# # task 3
result_list = [i for i in range(20, 240) if (i % 20 == 0 or i % 21 == 0)]
print(result_list)

# task 4 прошу прокомментировать решение. мое получилось слишком громоздкое
input_list_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
input_list_4_copy = input_list_4.copy()
input_list_4_copy.sort()
interim_list_4 = [item for num, item in enumerate(input_list_4_copy) if
                  input_list_4_copy[num] != input_list_4_copy[num - 1]
                  and input_list_4_copy[num] != input_list_4_copy[num + 1]]
output_list_4 = [item for item in input_list_4 if item in interim_list_4]
print(output_list_4)

# task 5
output_5 = functools.reduce(lambda a, b: a*b, [i for i in range(100,1001,2)])
print(output_5)

# task 6 see script

# task 7

def fact(n):
    yield list(map(math.factorial, [i for i in range(n)]))


for el in fact(5):
    print(el)
