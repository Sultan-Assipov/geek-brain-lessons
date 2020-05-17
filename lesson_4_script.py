from sys import argv
import itertools

# task 1
# script_name, script_hours, script_rate, script_reward = argv
# print("salary is: ", int(script_hours) * int(script_rate) + int(script_reward))

# task 6
script_name, script_start, script_iterations = argv
list_6 =["a", "repeating", "cycle"]
for i in itertools.count(int(script_start)):
    if i > int(script_start) + 10:
        break
    else:
        print("values for 6a: ", i)
cycle_count = 0
for i in itertools.cycle(list_6):
    if cycle_count > 3 * len(list_6):
        break
    else:
        print(i)
        cycle_count += 1

