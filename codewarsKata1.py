# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b

import random

# Using the 'random module' and the 'range' function to generates lists in the variables
list_1 = random.sample(range(1, 15), 8)
list_2 = random.sample(range(1, 15), 8)

# list_1 = [1,2]
# list_2 = [1]

print('List 1:', list_1)
print('List 2:', list_2)

def array_diff(a,b):
    # Putting intersecting values in one list and storing it in a variable called 'intersect_'
    intersect_ = ([i for i in a if i in b])
    
    # looping through 'intersect_' and removing values/elements found in list 'b' from list 'a'
    for item in intersect_:
        a.remove(item)
    return(a)

# calling new list with intersecting values removed
print('\narrar_diff:')
print(array_diff(list_1, list_2))



# list_1 = random.sample(range(1, 15), 7)
# list_2 = random.sample(range(1, 15), 7)

# print('list 1:', list_1)
# print('list 2:', list_2)

# diff_ = []

# intersect_ = ([i for i in list_1 if i in list_2])


# for item in intersect_:
#     list_1.remove(item)

# print(list_1)