# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

# solution
s = "abcd"

def accum(s):
    # setting counter i = 0
    i = 0

    # setting delimeter empty string
    result = ''
    
    # looping through string input s
    for letter in s:
        # adding letters iin str input to the result in .upper and .lower separated by '-'
        result += letter.upper() + letter.lower() * i + '-'
        # resetting counting adding 1 at the end of each iteration to be the number of times letter is printed
        i += 1
    return result[:len(result)-1]


print(accum(s))