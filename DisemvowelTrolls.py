# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

# Solution
string_ = "This website is for losers LOL!"

def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]

    # taking individual letters in string and seperating them with an empty string('') and removing letters in vowel list
    vowels_check = [letter for letter in string_ if letter.lower() not in vowels]
    
    # joining string together to form words in a sentence, spaced by an empty string('')
    string_ = ''.join(vowels_check)
    return string_

print(disemvowel(string_))