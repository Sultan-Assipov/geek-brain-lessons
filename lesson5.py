# task 1
result1 = ''
while True:
    line = input("please enter the line or press enter to exit: ")
    if line == '':
        break
    else:
        result1 += line+'\n'
with open("task1_file.txt", "w") as t1_file:
    t1_file.write(result1)


# task 2
with open('task2_file.txt') as t2_file:
    t2_list = list(t2_file)
print(f'number of lines is {len(t2_list)}')
for i, line in enumerate(list(t2_list)):
    print(f'the number of words in line {i+1} is {len(line.split(" "))}')

# task 3
with open('task3_file.txt') as t3_file:
    t3_list = list(t3_file)
result3 = {}
for line in t3_list:
    line = line.strip()
    list3 = line.split(' ')
    result3.update({list3[0]: list3[1]})
print(result3)
#
# list3 = []
for name, pay in result3.items():
    if int(pay) < 20000:
        print(name)
    list3.append(int(pay))
print(f'average salary is : {sum(list3) / len(list3)}')

# task 4 вывод сделал в виде словаря
from googletrans import Translator
translator = Translator()
with open('task4_input.txt') as t4_file:
    t4_list = list(t4_file)
dict4 = {}
for line in t4_list:
    line = line.strip()
    list4 = line.split(' ')
    dict4.update({translator.translate(list4[0], "ru").text: list4[2]})
print(dict4)
with open("task4_output.txt", 'w') as t4_file:
    t4_file.write(str(dict4))

# task 5
list5 = [1, 2, 3, 4]
string5 = " ".join(str(el) for el in list5)
with open('task5_file.txt', 'w') as t5_file:
    t5_file.write(string5)
with open('task5_file.txt', 'r') as t5_file:
    new_string5 = list(t5_file)[0]
print(new_string5)
new_list5 = map(int, new_string5.split(" "))
print(sum(new_list5))

# task 6
clear_symbols = ["(", ")", "-", ":"]
with open('task6_input.txt', 'r') as t6_file:
    list6 = list(t6_file)
result6 = {}
for line in list6:
    for symbol in clear_symbols:
        line = line.replace(symbol, " ")

    name = line.split(' ')[0]
    hours = sum([int(s) for s in line.split() if s.isdigit()])
    result6[name] = hours
print(result6)

# task 7
from numpy import mean
import json
with open('task7_input.txt', 'r') as t7_file:
    list7 = list(t7_file)
profit_list = []
name_list = []
for line in list7:
    line_list = line.split()
    name_list.append(line_list[0])
    profit_list.append(int(line_list[2]) - int(line_list[3]))
print(name_list, '\n', profit_list)
company_dict = dict(zip(name_list, profit_list))
profit_dict = {"average_profit": mean(list(i for i in profit_list if i > 0))}
print(profit_dict)
result7 = [company_dict, profit_dict]
print(result7)
with open('task7_output.txt', 'w') as t7_file:
    json.dump(result7, t7_file)
