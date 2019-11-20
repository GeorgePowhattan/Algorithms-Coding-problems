# Fixed Point

'''A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same. Find a fixed point (there can be many, just return 1) in a sorted list of <b>distinct elements</b>, or return None if it doesn't exist.'''

def find_fixed_point_sublinear(nums):
    
    for i, number in enumerate(nums):
        
        if i == number:
            return True
        elif i > number:
            continue
        else:
            return None
    
    return None

lst = [-5, 0, 3, 4]
lst2 = [-1, 0, 1, 2, 4]

print(find_fixed_point_sublinear(lst))
print(find_fixed_point_sublinear(lst2))