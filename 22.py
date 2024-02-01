# count a certain number in array list

def list_counter(nums):

    count = 0 

    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(list_counter([1,4,4,3,4]))