# Difficulty level: Beginner

# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.


# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Variables
bread = 8
peanutButter = 10
jelly = 3
sandwiches = bread/2
minIngredientQuantity = min(sandwiches, peanutButter, jelly)

# # Loop until I run out of an ingredient (minIngredientQuantity)
print("Goal 1")
for number in range(minIngredientQuantity):
	print("Making sandwich #{0}".format(number+1))
	# # Decrement the ingredients to account for what was just used to make a sandwich
	bread = bread-2
	peanutButter = peanutButter-1
	jelly = jelly-1
	sandwiches = bread/2
	# # Conditional block to determine which ingredient (if any) I've run out of
	if sandwiches == 0:
		print("All done; only had enough bread for {0} sandwiches.".format(number+1))
	elif peanutButter == 0:
		print("All done; only had enough peanut butter for {0} sandwiches.".format(number+1))
	elif jelly == 0:
		print("All done; only had enough jelly for {0} sandwiches.".format(number+1))
	else:
		print("I can make another sandwich...")

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Variables
bread = 10
peanutButter = 10
jelly = 4
sandwiches = bread/2
minIngredientQuantity = min(sandwiches, peanutButter, jelly)

print("\nGoal 2")
for number in range(minIngredientQuantity):
	bread = bread-2
	peanutButter -= 1
	jelly = jelly-1
	sandwiches = bread/2
	print("Making sandwich #{0}".format(number+1))
	if sandwiches == 0:
		print("All done; only had enough bread for {0} sandwiches.".format(number+1))
	elif peanutButter == 0:
		print("All done; only had enough peanut butter for {0} sandwiches.".format(number+1))
	elif jelly == 0:
		print("All done; only had enough jelly for {0} sandwiches.".format(number+1))
	else:
		print("I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(sandwiches, peanutButter, jelly))

