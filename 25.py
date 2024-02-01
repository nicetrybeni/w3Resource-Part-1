# check if number is in group

def is_group_member(group_list, n):

    for value in group_list:

        if n == value:
            return True
    return False
        
print(is_group_member([1,5,8,3], 4))