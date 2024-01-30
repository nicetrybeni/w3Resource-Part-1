#tuples 

list_of_numbers = input("Input comma separated numbers: ")

list = list_of_numbers.split(",")

tuple = tuple(list)

print("List: ", list)

print("Tuple: ", tuple)