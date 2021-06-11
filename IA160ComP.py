# Write a new Python Script to promt the user to input the radiuses of two cicles, calculate the areas for the circles, 
# and output the differences

# Input Prompt for collecting Radius data
radius_one = int(input('Enter Radius One: '))
radius_two = int(input('Enter Radius Two: '))

# Area: Circle One
area_one = 3.14 * radius_one**2
print('Area Of Circle One:', area_one)

# Area: Circle Two
area_two = 3.14 * radius_two**2
print('Area Of Circle Two:', area_two)

# Difference between the Areas
diff_inAreas = area_one - area_two
diff = abs(diff_inAreas)

print('Difference in Areas of Both circles:', diff)