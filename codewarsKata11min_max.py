# Ben has a very simple idea to make some profit: he buys something and sells it again. 
# Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. 
# Instead, he's going to buy it for the lowest possible price and sell it at the highest.

# Task
# Write a function that returns both the minimum and maximum number of the given list/array.

# solution
lst = [1,2,3,4,5]

def min_max(lst):
    new_list = []
    
    new_list.append(min(lst))
    new_list.append(max(lst))

    return new_list

print(min_max(lst)) 

# or 
def min_max(lst):
  return [min(lst), max(lst)]