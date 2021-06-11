# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# "helloWorld"   =>  "hello World"
# "camelCase"   =>  "camel Case"

# solution
import re

camSplit = 'camelCasing'

# re.sub to split string at start of camelcase[uppercase letter] -- uses regular expressions
def solution(camSplit):
    spl = []
    # Splitting on UpperCase using re.sub and regex references
    spl = re.sub(r'([A-Z])', r' \1', camSplit)
    return str(spl)

print(solution(camSplit))


