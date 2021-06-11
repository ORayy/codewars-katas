# Given: an array containing hashes of names

# Return: a string formatted as a list of names separated by commas except for the last two names, 
# which should be separated by an ampersand.

# Example:
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

# namelist([ {'name': 'Bart'} ])
# returns 'Bart'

# namelist([])
# returns ''

# solution
names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

def namelist(names):
    names_lst = []
    for i in range(len(names)):
        names_lst.append(names[i]['name'])
    names_str = ''
    for i in range(len(names_lst)):
        names_str += names_lst[i]
        if i < len(names_lst) - 2:
            names_str += ', '
        elif i == len(names_lst) - 2:
            names_str += ' & '
    return names_str

print(namelist(names))
