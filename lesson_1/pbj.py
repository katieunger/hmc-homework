# Variables
bread = 5
peanutButter = 4
jelly = 1
sandwiches = bread/2
minIngredientQuantity = min(sandwiches, peanutButter, jelly)

# Goal 1
# Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
print "Goal 1"
print "Can I make any peanut butter and jelly sandwiches?"
# If I have more than one bread slice, at least one serving of peanut butter, and at least one serving of jelly, I can make a PB&J sandwich.
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "Yes, you can make at least one peanut butter and jelly sandwich.\n"
else:
	print "No, you don't have sufficient ingredients to make any peanut butter and jelly sandwiches.\n"

# Goal 2
# Create a program to tell you: if you can make a sandwich, how many you can make
print "Goal 2"
print "How many peanut butter and jelly sandwiches can I make?"
# If I have more than one bread slice, at least one serving of peanut butter, and at least one serving of jelly, I can make as many PB&J sandwiches as the the number of servings of the ingredient I have the least of.
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} sandwich(es).\n".format(minIngredientQuantity)
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches.\n"

# Goal 3
# Create a program to allow you to make open-face sandwiches if you have an odd number of slices of bread
print "Goal 3"
print "How many peanut butter and jelly sandwiches can I make if I can also make an open-face sandwich?"
# If I have more than one bread slice, at least one serving of peanut butter, and at least one serving of jelly, I can make as many PB&J sandwiches as the the number of servings of the ingredient I have the least of.
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} sandwich(es) with two slices of bread.\n".format(minIngredientQuantity)
	# If I have an odd amount of bread, I may be able to make an additional open-face sandwich - there is a leftover slice of bread.
	if bread%2 != 0:
		# Do I have enough leftover PB&J after the sandwiches with two bread slices are made to make an open face sandwich?
		# minIngredientQuantity represents the number of sandwiches I can make with two slices of bread. Subtracting this from the number of servings of peanut butter and the number of servings of jelly will tell me whether there is leftover peanut butter or jelly. I need at least 1 additional serving of peanut butter and at least 1 additional serving of jelly.
		if peanutButter - minIngredientQuantity >= 1 and jelly - minIngredientQuantity >= 1:
			print "You can make an additional open-face sandwich.\n"
		else:
			print "You have leftover bread, but you've used up all your peanut butter and/or jelly. You cannot make an additional open-face sandwich.\n"
	else:
		print "You have an even number of bread slices, so you don't have any leftover bread to make open-face sandwiches.\n"
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches.\n"

# Goal 4
# Create a program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich
print "Goal 4"
print "How many peanut butter and jelly sandwiches can I make if I can also make peanut butter sandwiches if I run out of jelly?"
# If I have more than one bread slice, at least one serving of peanut butter, and at least one serving of jelly, I can make as many PB&J sandwiches as the the number of servings of the ingredient I have the least of.
if bread > 1 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} peanut butter and jelly sandwich(es).\n".format(minIngredientQuantity)
	# If I have leftover peanut butter and bread, I may be able to make additional peanut butter sandwiches.
	# I need to figure out how much peanut butter and bread I have leftover after making the PB&J sandwiches.
	extraPB = peanutButter - minIngredientQuantity
	extraBread = (bread - minIngredientQuantity*2)
	if extraPB >= 1 and extraBread > 1:
		# Which do I have the least of, PB or bread?
		print "You have {0} extra serving(s) of peanut butter.".format(extraPB)
		print "You have {0} extra slices of bread.".format(extraBread)
		minButterBread = min(extraPB, extraBread/2)
		print "You can make {0} peanut butter sandwich(es).\n".format(minButterBread)
	else:
		print "You don't have enough leftover bread and peanut butter to make any additional peanut butter sandwiches.\n"
# If I have more than one bread slice, at least one serving of peanut butter, and no jelly, I can make as many peanut butter sandwiches as whichever ingredient, peanut butter or bread/2, I have the least of.
elif bread > 1 and peanutButter >= 1 and jelly == 0:
	minButterBread = min(peanutButter,bread/2)
	print "You have no jelly, but you can make {0} peanut butter sandwich(es).\n".format(minButterBread)
else:
	print "You don't have sufficient ingredients to make any peanut butter and jelly sandwiches.\n"

# Goal 5
# Create a program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
print "Goal 5"
if sandwiches > 0 and peanutButter >= 1 and jelly >= 1:
	print "You can make {0} peanut butter and jelly sandwich(es).".format(sandwiches)
	if bread%2 != 0:
		if peanutButter%2 != 0 and jelly%2 != 0:
			print "You have an odd number of bread slices, and an odd amount of peanut butter and jelly. You can also make an open-face sandwich."
		else:
			print "You have an odd number of bread slices, but not an odd amount of peanut butter and jelly. You can't make an additional open-face sandwich."
	else:
		print "You have an even number of bread slices, so you don't have any leftover bread to make open-face sandwiches."
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