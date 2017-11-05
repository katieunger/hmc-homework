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
print("Attendees list: {0}\n".format(attendees))
# # In Python 3, print is defined as a function so we print like this: print("Print me")

# # An empty lists looks like []
people_who_didnt_do_pbj = []

# # Lists: Slicing

# # A list can be sliced like a string can be sliced
# # Instead of printing characters by index, this will print items in the list by index
# # This will print the first two people in the list:
print("First two people in attendees list: {0}\n".format(attendees[0:2]))
# # This will print the fourth person in the list:
print("Fourth person in attendees list: {0}\n".format(attendees[3]))
# # To print all attendees on list using slice:
print("Printing the attendees list again using attendees[:]: {0}\n".format(attendees[:]))
# # To print last three people:
# # We could use negative indexing like this
# # This could be useful if you don't know how long your list is
# # (Though you can just get the length of the list using len())
print("Last three people in attendees list: {0}\n".format(attendees[-3:]))

# # Lists: Length

# # The length of the list can be calculated using len()
print("Length of attendees list: {0}\n".format(len(attendees)))

# # Lists: Adding Items

# # To add to the end of a list, use .append() method
attendees.append('Mary')
print("Adding 'Mary' to end of attendees list: {0}\n".format(attendees))

# # Lists: Changing Existing Items

# # An item in a list can be changed by getting the item using its index and setting it
attendees_ages = [28, 36, 32, 18, 25, 28]
print("Attendees' ages list: {0}\n".format(attendees_ages))

# # To get the first age in the list and change it:
attendees_ages[0] = 29
print("Changed first age in attendees' ages list to 29: {0}\n".format(attendees_ages))

# # Lists: Deleting Existing Items

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print("Days of week list: {0}\n".format(days_of_week))
# # An item can be removed from a list using pop()
# # This will remove the last item from the list:
day = days_of_week.pop()
print("Last day removed from days of week list: {0}\n".format(day))
# # This will remove the fourth item from the list:
day = days_of_week.pop(3)
print("Fourth day removed from days of week list: {0}\n".format(day))
print("Days of week list now looks like: {0}\n".format(days_of_week))

# # To store removed item:
# # This will store the name of the TA in a variable
TA = attendees.pop(9)
print("Our TA is {0}\n".format(TA))
print("Now our attendees list looks like: {0}\n".format(attendees))
print("The length of the attendees list is now: {0}\n".format(len(attendees)))

# # Lists: Quick Exercise
months = ['January', 'February']
print("Months list: {0}\n".format(months))
months.append('March')
print("Append() adds one item at a time: {0}\n".format(months))
months.extend(['April', 'May', 'June'])
print("Extend() adds multiple items: {0}\n".format(months))
monthsToAdd = ['July', 'August', 'September', 'October', 'November', 'December']
months.extend(monthsToAdd)
print("Adding all months: {0}\n".format(months))

# # Append() will always add item at end of list

# # Lists: Add/Remove

# # Remove the first month:
months.pop(0)
print("Removing first month using pop(): {0}\n".format(months))

# # Insert 'January' before index 0:
months.insert(0, 'January')
print("Adding January back using insert(): {0}\n".format(months))

# # To get an item from a list without removing it:
thisMonth = months[8]
print("Printing month by index - months[8] is: {0}\n".format(thisMonth))

# # Lists: Strings to Lists

# # In this example, every time Python sees a space, it will use that to know
# # where to split the string into a list (you can split on any character)
addressTest = '1133 19th St. Washington, DC 20036'
addressAsList = addressTest.split(" ")
print("Printing address as a list using split(' '): {0}\n".format(addressAsList))

# # Lists: Membership
# # The in keyword allows you to check whether a value exists in the list
# # It will return a True/False boolean
# # Also works with strings!

nameCheck = 'ann' in 'Shannon'
print("Using 'in' to see if 'ann' is in string 'Shannon' - will return a boolean: {0}\n".format(nameCheck))

frankensteinMembership = 'Frankenstein' in attendees
print("Using 'in' to see if 'Frankenstein' is in attendees list - will return a boolean: {0}\n".format(frankensteinMembership))

# # Lists: Exercise

# # See quadrants.py for quadrant list exercise

# # Lists: Ranges of Numbers

# # The range function generates a list of numbers
print("Creating a list of numbers using range(): {0}\n".format(range(5)))
# # The range function can be provided with a start and a stop
print("Creating a list of numbers using range with start and stop: {0}\n".format(range(5, 10)))
# # We can use range when we need to do a task a certain number of times

print("Printing numbers in range(1,11):\n")
for number in range(1,11):
	print(number)

# # Loops: For Loop Exercise
# # See quadrants.py for quadrant list exercise

# # Loops: For Loop

# # Simple loop for printing days of the week
days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

print ("\nPrinting days of the week:\n")
for day in days_of_week:
	print(day)

# # Loops: Nested For Loops

months_in_year = ["January","February","March","April","May","June","July","August","September","October","November","December"]

# # This loop will print 4 weeks with 7 days per week for each month of the year
for month in months_in_year:
	print "\n" + month + "\n"
	for week in range(1,5):
		print "Week {0}".format(week)
		for day in days_of_week:
			print "\t" + day

# # Loops: Enumerate
# # enumerate() is a function that you use with a for loop to get the index (position) of that list item, too.
# # Commonly used when you need to change each item in a list one at a time.

# # This loop will print each month and its index
# # Put underscore in front of variables that may be reserved keywords
for _index, month in enumerate(months_in_year):
	print(_index)
	print(month)

# So if I want to change just February to 'Febrewary'
for _index, month in enumerate(months_in_year):
	if (month == 'February'):
		febIndex = _index

months_in_year[febIndex] = "Febrewary"
print(months_in_year)


# # Loops: Zip

# # A for loop iterates over each item in a single list one at a time
# # zip() can be used to combine lists into a single list so that items from multiple lists can be used in a loop together
states = ['Arizona', 'Virginia', 'Maryland']
stateAbbreviation = ['AZ', 'VA', 'MD', 'RI']

for items in zip(states, stateAbbreviation):
	print(items)

# # Note that RI is left off because the two lists have different lengths

# # Loops: While

# # A for loop lets you use each item in a single list one at a time, which is great for performing actions a certain number of times.
# # Loops using while function like conditionals - will perform an action while a condition is true

# This loop will print a message about making a sandwich and subtract 2 from bread until bread is no longer greater than or equal to 2

bread = 9

while bread >= 2:
	print("I'm making a sandwich")
	# # bread = bread - 2
	# # Shorthand:
	bread -= 2
	print("I now have {0} slices of bread left".format(bread))
	# # This does something else!
	# # bread =- 2
	# # Make an open face sandwich:
	if bread == 1:
		print("I'm making an open face sandwich!")



