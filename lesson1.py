# task 1
name = input("enter your name: ")
print(f'your name is {name} ')
# age = input(f'{name} please enter your age: ')
# print(f'{name} your age is {age}')
input_friend_list = input(f'{name} please enter your friend list separated by coma: ')
friend_list = input_friend_list.split(",")
i = 0
for names in friend_list:
    print(f'your friend №{i+1} is {friend_list[i]}')
    i = i + 1

# task 2
time_in_seconds = int(input("enter time in seconds: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds - hours*3600) // 60
seconds = time_in_seconds - hours*3600 - minutes*60
print(f'Normal format of time is {hours}:{minutes}:{seconds}')

# task 3
number = int(input('enter your number: '))
print(f"result = {number+number**2+ number**3}")

# task 4 I have used different approach as I believe it is more effective and clean
number = list(input('enter the number: '))
print(f'maximum digit is: {max(number)}')

# task 5
sales = int(input("please enter your sales: "))
costs = int(input("please enter your costs: "))
if sales > costs:
    print(f"company works with profitability of {(sales / costs - 1) * 100}%")
    staff = int(input("enter the number of staff: "))
    print(f'profit per person of staff is: {(sales-costs)/staff}$')
else:
    print('company works at loss')

# task 6
current = int(input('enter the starting point: '))
goal = int(input('enter the goal: '))
n = 0
while current <= goal:
    current *= 1.1
    n += 1
    print(f'result for day {n} is {current: .2f}')
print(f'result of {goal} kilometers will be achieved in {n} days')

# task 7
