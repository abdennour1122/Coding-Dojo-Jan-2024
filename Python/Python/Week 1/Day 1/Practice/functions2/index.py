#  Create a function that accepts a number as an input. Return a new list
def countdown_list(num):
    new_list = []
    for i in range(num, -1, -1):
        new_list.append(i)
    return new_list
result = countdown_list(5)
print(result)
#  Create a function that will receive a list with two numbers. Print the first value and return the second.
def process_list(lst):
    if len(lst) < 2:
        print("Error: List must have at least two elements")
        return None
    print("First value:", lst[0])
    return lst[1]
my_list = [10, 20]
second_value = process_list(my_list)
print("Second value returned:", second_value)
# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def sum_first_plus_length(input_list):
    if not input_list:
        print("Error: List is empty")
        return None
    result = input_list[0] + len(input_list)
    return result
my_list = [1, 2, 3, 4, 5]
result = sum_first_plus_length(my_list)
print("Result:", result)
#  Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def filter_values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    second_value = lst[1]
    
    new_list = [x for x in lst if x > second_value]
    
    print("Number of values greater than the second value:", len(new_list))
    
    return new_list

my_list = [5, 3, 7, 2, 8]
result = filter_values_greater_than_second(my_list)
print("New list:", result)
# Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def create_list(size, value):
    return [value] * size

size = 5
value = 10
result = create_list(size, value)
print("New list:", result)
