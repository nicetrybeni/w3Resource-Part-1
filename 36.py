# add 2 integers if they are both int 

def add_numbers(x,y):

    if not(isinstance(x, int) and isinstance(y, int)):
        return "Input must be INT"
    else:
        return x + y

print(add_numbers(5,5))
print(add_numbers(5,5.003))
