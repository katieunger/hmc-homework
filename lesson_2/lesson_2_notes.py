# # Lesson 2
# # Lists and Loops

# # Lightning Review

# # Variables

# # Variables are names that you can assign values to
# # Variables can contain numbers, strings, lists, True/False
# # Variable names can contain letters and underscores and should be descriptive

# # Strings

# # Strings can contain anything that you can type out on the keyboard
# # Strings are commonly used for names, phone numbers, etc.
# # Slicing is used to see parts of a string
# # String methods allow you to do special actions on strings (find, replace, count, lowercase, etc.)

# # Conditionals

# # Conditionals allow you to change behavior of your program

# # Lists

# # Lists are containers that can hold multiple pieces of information. They can hold strings, numbers, etc.

# # Lists: Syntax

# # Lists are created by placing items inside of square brackets: []
# # Items in a list are separated by commas

# # Holding the name of each attendee in a separate variable isn't efficient:
attendee1 = 'Katie'
attendee2 = 'Michelle'
attendee3 = 'Di'

# # Below is a list of attendees:
attendees = ['Katie', 'Michelle', 'Di', 'Lauren', 'Sam', 'Allie', 'Samantha', 'Lisa', 'Jocelyn', 'Stacey', 'Tamar', 'Megan', 'Katie', 'Kelly', 'JihFan', 'Serena', 'Claudia']
print(attendees)

# # An empty lists looks like []
people_who_didnt_do_pbj = []

# # Lists: Slicing

# # A list can be sliced like a string can be sliced
# # Instead of printing characters by index, this will print items in the list by index
# # This will print the first two people in the list:
print(attendees[0:2])
# # This will print the fourth person in the list:
print(attendees[3])
# # To print all attendees on list using slice:
print(attendees[:])
# # To print last three people:
# # We could use negative indexing like this
# # This could be useful if you don't know how long your list is
# # (Though you can just get the length of the list using len())
print(attendees[-3:])

# # Lists: Length

# # The length of the list can be calculated using len()
print(len(attendees))

# # Lists: Adding Items

# # To add to the end of a list, use .append() method
attendees.append('Mary')
print(attendees)

# # Lists: Changing Existing Items

# # An item in a list can be changed by getting the item using its index and setting it
attendees_ages = [28, 36, 32, 18, 25, 28]

# # To get the first age in the list and change it:
attendees_ages[0] = 29
print(attendees_ages)

# # Lists: Deleting Existing Items

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
day = days_of_week.pop()
print day
day = days_of_week.pop(3)
print day
print days_of_week
# # Saturday and Wednesday have been removed from the list entirely!

# # pop() method removes item from the list!
# # To store removed item:
TA = attendees.pop(9)
print TA
print attendees
print (len(attendees))

# # Lists: Quick Exercise
months = ['January', 'February']
months.append('March')
print months
months.extend(['April', 'May', 'June'])
print months
monthsToAdd = ['July', 'August', 'September', 'October', 'November', 'December']
# months.append(monthsToAdd)
# print months
months.extend(monthsToAdd)
print months

# # Append() will always add item at end of list

# # Lists: Add/Remove

# # Remove the first month:
months.pop(0)
print months

# # Insert 'January' before index 0:
months.insert(0, 'January')
print months

# # To get an item from a list without removing it:
thisMonth = months[8]
print thisMonth

# # In Python 3, print is defined as a function so we print like this:
print(thisMonth)

# # Lists: Strings to Lists

# # In this example, every time Python sees a space, it will use that to know
# # where to split the string into a list (you can split on any character)
addressTest = '1133 19th St. Washington, DC 20036'
address_as_list = addressTest.split(" ")
print(address_as_list)

# # Lists: Membership
# # The in keyword allows you to check whether a value exists in the list
# # It will return a True/False boolean
# # Also works with strings!

nameCheck = 'ann' in 'Shannon'
print nameCheck

print 'Frankenstein' in attendees

# # Lists: Exercise
# Use raw_input() to allow a user to type
# address = raw_input("What is your address? ")

# # For now, let's just create lists:
NW = []
NE = []
SE = []
SW = []
other = []

quadrantList = [NW, NE, SE, SW, other]

# if "NW" in address:
# 	NW.append(address)
# elif "NE" in address:
# 	NE.append(address)
# elif "SE" in address:
# 	SE.append(address)
# elif "SW" in address:
# 	SW.append(address)
# else:
# 	other.append(address)
# 	print("Not in any quadrant!")

address1 = "815 16 St NW Washington D.C. 20005"
address2 = "123 SEA LANE SW"
address3 = "125 L'Enfant Plaza SW Washington D.C. 22033"

addresses = [address1, address2, address3]

# print(addresses)

# # # If that address contains a quadrant (NW, NE, SE, SW), then add it to that quadrant's list

# if "NW" in address1:
# 	NW.append(address1)
# elif "NE" in address1:
# 	NE.append(address1)
# elif "SE" in address1:
# 	SE.append(address1)
# elif "SW" in address1:
# 	SW.append(address1)
# else:
# 	print("Not in any quadrant!")

# if "NW" in address2:
# 	NW.append(address2)
# elif "NE" in address2:
# 	NE.append(address2)
# elif "SE" in address2:
# 	SE.append(address2)
# elif "SW" in address2:
# 	SW.append(address2)
# else:
# 	print("Not in any quadrant!")

# if "NW" in address3:
# 	NW.append(address3)
# elif "NE" in address3:
# 	NE.append(address3)
# elif "SE" in address3:
# 	SE.append(address3)
# elif "SW" in address3:
# 	SW.append(address3)
# else:
# 	print("Not in any quadrant!")

# print(quadrantList)

# # # Do the same thing using OR
# # # This doesn't work right...

# if "NW" in (address1 or address2 or address3):
# 	if "NW" in address1:
# 		NW.append(address1)
# 	if "NW" in address2:
# 		NW.append(address2)
# 	if "NW" in address3:
# 		NW.append(address3)
# elif "NE" in (address1 or address2 or address3):
# 	if "NE" in address1:
# 		NE.append(address1)
# 	if "NE" in address2:
# 		NE.append(address2)
# 	if "NE" in address3:
# 		NE.append(address3)
# elif "SE" in (address1 or address2 or address3):
# 	if "SE" in address1:
# 		SE.append(address1)
# 	if "SE" in address2:
# 		SE.append(address2)
# 	if "SE" in address3:
# 		SE.append(address3)
# elif "SW" in (address1 or address2 or address3):
# 	if "SW" in address1:
# 		SW.append(address1)
# 	if "SW" in address2:
# 		SW.append(address2)
# 	if "SW" in address3:
# 		SW.append(address3)
# else:
# 	print("Not in any quadrant!")

print(quadrantList)

# # Allow user to enter 3 addresses; after three, print the length and contents of each list

# # Try Code Academy Intro to Terminal!

# # Ranges

for number in range(1,11):
	print number

# # Try quandrant exercise with loops

for address in addresses:
	if " NW " in address:
		NW.append(address)
	elif " NE " in address:
		NE.append(address)
	elif " SW " in address:
		SW.append(address)
	elif " SE " in address:
		SE.append(address)
	else:
		other.append(address)
print quadrantList

# # How to deal with SEA LANE?

# # This puts addresses in quadrant lists more than once
for address in addresses:
	addressAsList = address.split(' ')

	if "NW" in addressAsList:
		NW.append(address)
	elif "NE" in addressAsList:
		NE.append(address)
	elif "SW" in addressAsList:
		SW.append(address)
	elif "SE" in addressAsList:
		SE.append(address)
	else:
		other.append(address)
print quadrantList

# # Simple loop for printing days of the week

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

for day in days_of_week:
	print day

# # Loops: Nested For Loops

months_in_year = ["January","February","March","April","May","June","July","August","September","October","November","December"]

for month in months_in_year:
	print "\n" + month + "\n"
	for week in range(1,5):
		print "Week {0}".format(week)
		for day in days_of_week:
			print "\t" + day

# # Loops: Enumerate
# # enumerate() is a function that you use with a for loop to get the index (position) of that list item, too.
# # Commonly used when you need to change each item in a list one at a time.

# # Put underscore in front of variables that may be reserved keywords
# # PEP 8 = conventions for Python coding
for _index, month in enumerate(months_in_year):
	print(_index)
	print(month)

# # So if I want to change just February to 'Febrewary'
# for _index, month in enumerate(months_in_year):
# 	if (month == 'February'):
# 		febIndex = _index
# 		print(febIndex)
# 	else:
# 		print("February not found!")
# 	if febIndex:
# 		months_in_year[febIndex] = "Febrewary"
# 		print months_in_year


# # Loops: Zip

states = ['Arizona', 'Virginia', 'Maryland']
stateAbbreviation = ['AZ', 'VA', 'MD', 'RI']

for items in zip(states, stateAbbreviation):
	print items

# # Loops: While

# # A for loop lets you use each item in a single list one at a time,
# # which is great for performing actions a certain number of times.

bread = 8

if bread >= 2:
	print "I'm making a sandwich"

while bread >= 2:
	print "I'm making a sandwich"
	# # bread = bread - 2
	# # Shorthand:
	bread -= 2
	# # This does something else!
	# # bread =- 2
	# # Make an open face sandwich:
	if bread == 1:
		print("I'm making an open face sandwich!")

# # Python Resources:

# # The Python Standard Library by Example
# # Regular Expressions - allows you to look through strings and look for specific patterns
# # within strings - good for address/quandrant exercise
# # Data Science from Scratch: First Principles with Python
# # Wes McKinney also wrote Python for Data Analysis: Data Wrangling with Pandas, NumPy, and
# # iPython (2nd Edition not out yet)
# # Python Programming for the Absolute Beginner, 3rd Edition (build games!)

		






