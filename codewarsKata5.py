# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development 
# and functioning of living organisms.

# If you want to know more http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. 
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here
# http://rosalind.info/problems/list-view/ (source)

# Test Outcomes
# DNA_strand ("ATTGC") # return "TAACG"
# DNA_strand ("GTAT") # return "CATA"

# solution

import string
# table = string.maketrans('CGAT', 'GCTA')
# print 'GCTTAA'.translate(table)

def DNA_strand(dna):
    # spliting string input 'dna' into a list 'table
    table = [char for char in dna]

    # maps each char in the intabstring into the character at the same position in the outtab string. Table is passed to the translate() function
    # intab replaces chara in outtab as compliments of each other
    table = str.maketrans('CGAT', 'GCTA')
    return dna.translate(table)


print(DNA_strand("ATATkcGC"))


# str.maketrans(intab, outtab])

# intab − This is the string having actual characters.
# outtab − This is the string having corresponding mapping character.
