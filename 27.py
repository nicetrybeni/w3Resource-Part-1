# list of number to string

def concatenator(list_num):
    result = ""

    for element in list_num:
        result += str(element)

    return result

print(concatenator([1,5,212]))