# reutnr true if 2 int = 5 

def n_diff(x,y):
    if x == y or abs (x - y) == 5 or (x+y) == 5:
        return True
    else:
        return False
    
print(n_diff(2,2))
print(n_diff(7,3))