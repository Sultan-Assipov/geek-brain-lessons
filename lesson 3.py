# task 1
def dev(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print("please enter numbers")


a = input("enter num1: ")
b = input("enter num2: ")
print(dev(a, b))


# task 2
def print_user(name, surname, date_of_birth, city, email, telephone):
    print(name, surname, date_of_birth, city, email, telephone)


print_user(name="Sultan", surname="Assipov", date_of_birth=1987, city="Almaty", email="sultan.assipov@gmail.com",
           telephone="+77014779753")


# task 3
def my_func(num1, num2, num3):
    return max(num1 + num2, num1 + num3, num2 + num3)


print(my_func(1, 2, 3))


# task 4
def power(x, y):
    try:
        if type(y) != int: raise ValueError
        float(x)
    except ValueError:
        print("please give correct values to the function")
        return None

    result = 1
    for i in range(y):
        result *= x
    return result


x = 2
y = 5
print(power(x, y))
power("a", "b")
power(5, 2.1)


# task 5
def list_sum(input_list, previous_result):
    result = previous_result
    for item in input_list:
        try:
            result += float(item)
        except ValueError:
            print(result)
            return None
    print(result)
    print("entered not a number")
    return result


previous_result = 0
while True:
    input_list = input("please enter the list via space: ").split(" ")
    trigger = list_sum(input_list, previous_result)
    if trigger == None:
        break
    else:
        previous_result += trigger


# task 6
def int_func(word):
    return word.capitalize()


input_list1 = input("please enter the word list via space: ").split(" ")
print(*(int_func(word) for word in input_list1))
