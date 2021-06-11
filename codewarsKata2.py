# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

# solution

l = [1,2,'a','b']

def filter_list(l):
    # using list comprehension to remove string elements from list. 
    return [i for i in l if type(i) != str]

print(filter_list(l))

# checking what type each element is
for element in l:
    print(type(element), element)


# list comprehension
# return [i for i in l if type(i) != str]
# return i after looping through list
# for i in list 'l' if i is not a string, take element and put it in a new list