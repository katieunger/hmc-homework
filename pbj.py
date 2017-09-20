# Variables
bread = 2
peanutButter = 2
jelly = 1
sandwiches = bread/2

# Goal 1
# Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
print "Goal 1"
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "You can make at least one peanut butter and jelly sandwich."
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches."

# Goal 2
# Create a program to tell you: if you can make a sandwich, how many you can make
print "Goal 2"
minIngredientQuantity = min(bread, peanutButter, jelly)
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} sandwich(es).".format(minIngredientQuantity)
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches."

# Goal 3
# Create a program to allow you to make open-face sandwiches if you have an odd number of slices of bread
print "Goal 3"
if sandwiches > 0 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} sandwich(es).".format(sandwiches)
	if bread%2 != 0:
		if peanutButter%2 != 0 and jelly%2 != 0:
			print "You have an odd number of bread slices, and an odd amount of peanut butter and jelly. You can also make an open-face sandwich."
		else:
			print "You have an odd number of bread slices, but not an odd amount of peanut butter and jelly. You can't make an additional open-face sandwich."
	else:
		print "You have an even number of bread slices."
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches."

# Goal 4
print "Goal 4"
if sandwiches > 0 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} peanut butter and jelly sandwich(es).".format(sandwiches)
	if bread%2 != 0:
		if peanutButter%2 != 0 and jelly%2 != 0:
			print "You have an odd number of bread slices, and an odd amount of peanut butter and jelly. You can also make an open-face sandwich."
		else:
			print "You have an odd number of bread slices, but not an odd amount of peanut butter and jelly. You can't make an additional open-face sandwich."
	else:
		print "You have an even number of bread slices."
elif sandwiches > 0 and peanutButter >= 1 and jelly < 1:
	print "You can make {0} peanut butter sandwich(es).".format(sandwiches)
else:
	print "You don't have sufficient ingredients to make any sandwiches."

# Goal 5
print "Goal 5"
if sandwiches > 0 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} peanut butter and jelly sandwich(es).".format(sandwiches)
	if bread%2 != 0:
		if peanutButter%2 != 0 and jelly%2 != 0:
			print "You have an odd number of bread slices, and an odd amount of peanut butter and jelly. You can also make an open-face sandwich."
		else:
			print "You have an odd number of bread slices, but not an odd amount of peanut butter and jelly. You can't make an additional open-face sandwich."
	else:
		print "You have an even number of bread slices."
elif sandwiches > 0 and peanutButter >= 1 and jelly < 1:
	print "You can make {0} peanut butter sandwich(es).".format(sandwiches)
else:
	print "You don't have sufficient ingredients to make any sandwiches."

# Goal 6
print "Goal 6"
if sandwiches > 0 and peanutButter >= 1 and jelly >= 1:
	print "You can make at least one sandwich!"
	if peanutButter == jelly:
		print "There's an equal amount of peanut butter and jelly."
		if peanutButter or jelly <= sandwiches:
			print "There's more peanut butter or jelly than slices of bread to make sandwiches."
			print "The maximum number of sandwiches you can make is {0}.".format(sandwiches)
		else:
			print "There's more bread than there is peanut butter and jelly."
			print "The maximum number of sandwiches you can make is {0}.".format(jelly)
	else:
		print "Uh oh, there isn't an equal amount of peanut butter and jelly."
		if peanutButter > jelly:
			extraPB = peanutButter - jelly
			print "There's {0} more peanut butters than jellies.".format(extraPB)
		else:
			extraJelly = jelly - peanutButter
			print "There's {0} more jellies than peanut butters.".format(extraJelly)
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches."