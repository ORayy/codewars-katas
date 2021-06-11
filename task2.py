# Write a new Python Script to prompt the user to enter (n) and then computes the value of n+nn+nnn

# input number 1 (n)
n = int(input('Input n: '))

# input number 2 (nn)
nn = str(n) + str(n)
print('input nn:', int(nn))

# input number 3 (nnn)
nnn = str(n) + str(n) + str(n)
print('input nnn:', int(nnn))

# n+nn+nnn
n_sum = int(n) + int(nn) + int(nnn)
print(f'value of n({n}) + nn({nn}) + nnn({nnn}) =', n_sum)