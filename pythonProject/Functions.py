# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(x, y):
    """

    :rtype: object
    """
    sum = x + y
    print(sum)


add_two_numbers(2, 10)


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    pi = 2.14
    area = pi * r * r
    print(area)


area_of_circle(10)


# Write a function called add_all_nums which takes arbitrary number of arguments
# and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            total += num
            print(total)
        else:
            print("The number is not integer")


add_all_nums(2, 3, 'a')


## Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius(celsius):
    Faren = (celsius * 9 / 5) + 32
    print(Faren)


convert_celsius(24)


## Write a function called check-season,
## it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(month):
    if month == "December" or " Jan" or "Feb":
        print("Autumn")
    elif month == "March" or "April" or "May":
        print("Summer")


check_season('Jan')


## Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(m, x, b):
    y = (m * x) + b
    print(y)


calculate_slope(3, 4, 6)


## Declare a function named print_list.
# It takes a list as a parameter and it prints out each element of the list.

def print_list(nums):
    for i in nums:
        print(i)


print_list([1, 2, 3, 4])

## Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
'''
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
'''


def reverse_list(num):
    reverse = []
    for i in num:
        reverse = [i] + reverse
    print(reverse)


reverse_list(["A", "B", "C"])

'''Declare a function named capitalize_list_items. 
It takes a list as a parameter and it returns a capitalized list of items'''


def capital_list(items):
    var = []
    for i in items:
        var.append(i.capitalize())
    print(var)


capital_list(['a', 'b', 'c', 'd'])

''' Declare a function named add_item.
 It takes a list and an item parameters. It returns a list with the item added at the end.'''


def add_item(num, *item):
    num.extend(item)
    print(num)


add_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Meat')

'''
Declare a function named remove_item. 
It takes a list and an item parameters.
 It returns a list with the item removed from it.
'''


def remove_item(num, item):
    num.remove(item)
    print(num)


remove_item([1, 2, 3, 4], 3)

'''
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
'''


def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i

    print(sum)


sum_of_numbers(100)

'''
Declare a function named sum_of_odds. 
It takes a number parameter and it adds all the odd numbers in that range.
'''


def sum_of_odds(num):
    sum = 0
    for i in range(num):
        if i % 2 != 0:
            sum = sum + i
            print(sum)


sum_of_odds(5)

""" 
Declare a function named sum_of_even. 
It takes a number parameter and it adds all the even numbers in that - range.
"""


def sum_of_evens(num):
    sum = 0
    for i in range(num):
        if i % 2 == 0:
            sum = sum + i
            print(sum)


sum_of_evens(5)

## Level 2

""" Declare a function named evens_and_odds . It takes a positive integer as parameter
 and it counts number of evens and odds in the number.
"""


def evens_odds(num):
    count = 0
    for i in range(num):
        if i % 2 == 0:
            count = count + 1
            print(count)
        elif i % 2 != 0:
            count = count + 1
            print(count)


evens_odds(100)

## Call your function factorial,
# it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    fact = 1
    if num<0:
        print("Will not work")
    elif num == 0:
        print("0 factorial is 1")
    else:
        for i in range(1,num+1):
            fact = fact * i
        print(fact)

factorial(5)
5

