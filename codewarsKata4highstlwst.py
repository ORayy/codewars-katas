# In this little assignment you are given a string of space separated numbers, 
# and have to return the highest and lowest number.

# solution

numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"

def high_and_low(numbers):
    # taking string attribute of the function, putting it into a list and spliting them with the spaces represted by an empty string " "
    new = [int(i) for i in numbers.split(" ")]
    
    # returning the mininum and maximum and concatinating the two string results to remove it from a tuple
    return str(max(new)) + " " + str(min(new))

print(high_and_low(numbers))

