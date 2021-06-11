# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

# solution

text = "This is an example!"


def reverse_words(text):
    # splitting text into list
    spl = text.split(" ")
    
    # assigning empty string to variable 's' to be the delimeter joing reversed elements in the list 'spl'
    s = " "
    
    # reversing each element in its individual index assigning to variable t
    t = [x[::-1] for x in spl]
    
    # joining list using delimeter(empty string) assigned in variable s
    return s.join(t)

print(reverse_words(text))

# or 

# def reverse_words(text):
#     return ' '.join(s[::-1] for s in text.split(' '))
