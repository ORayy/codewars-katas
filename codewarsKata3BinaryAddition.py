# Implement a function that adds two numbers together and returns their sum in binary. 
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.

# solution

def add_binary(a,b):
    #adding values and converting to binary, removing '0b' bianary prefix with '[2:]'
    binary = bin(a + b)[2:]
    return str(binary) 
