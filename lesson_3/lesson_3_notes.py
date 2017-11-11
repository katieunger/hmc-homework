# # Lesson 3

# # Teacher: Anna
# # Note: on Windows, can use Idle or Jupyter Notebooks

# # Lightning Review (Lesson 2)

# # Lists

# # Lists can hold multiple items

# # Slicing allows us to view individual or multiple items in a list

# # The in keyword allows us to check whether a given item appears in that list

# # .append() adds one item to the end of the list

# # .pop() removes one item from the end of the list

# # Loops

# # Loops run through a block of code multiple times

# # For loops: for each item in this list, do something

# # While loops: does something while a condition is true

# # File Handling

# # File handling lets Python read and write to files, such as a spreadsheet or text file

# # File Handling: Most Common Syntax

with open("states.txt", "r") as states_file:
	states = states_file.read()
print(states)

# # "with" keyword: tells Python we're going to do something with a file we're about to open
# # When all commands within the indented block have been run, the file is closed automatically.
# # open() is a function that tells Python to open a file.
# # open() takes two arguments:
	# # Argument 1: the file we want to open, using a relative path
		# # "states.txt" is our file
		# # Relative paths are the pathway to the file we want to open relative to where the script file we're running is
		# # In this case, the file "states.txt" is in the same directory as the script we're running
	# # Argument 2: the mode to the open the file in, as a string
		# # r: read-only mode
		# # w: write mode
		# # a: append mode
# # The "as" keyword creates a variable for your file handler - we're calling it "states_file"
# # .read() is a file method - a function that only works with file handlers (in this example "states_file")
# # .read() will read the entire contents of the file. We're saving these contents into the variable "states"
# # Outcome:
	# # 1. Open a file (states.txt)
	# # 2. Create a variable called states that has the entire contentsof the file states.txt

 # # states is a string. When we print the first item, we get the letter "A":
print(states[0])

# # Let's Try It Out: Text Files
# # .read() gives us the file contents as a string. If we have  a string, we can turn it into a list!
# # Turning states into a list is useful because now we can get the first state using index, rather than the first letter - the content is more organized

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")
print(states)

# # enumerate(): gives you the index and the list item
# # We are looping on this list using enumerate to get the index and each list item
# # For each state, we are splitting that list item on tab into another list (containing state abbreviation and state name)
# # We use enumerate so that we can put our new state list back into the full states list in the correct place

# for index, state in enumerate(states):
# 	states[index] = state.split("\t")
# print(states)

# # This doesn't work because we aren't saving our state that is split on tab back into the states list
for state in states:
	state = state.split("\t")
print(states)

# # Here, we are splitting on newlines to make a list and saving these results into states
# # Then, we are looping on this list using enumerate to get the index and each list item
# # For each state, we are splitting that list item on tab into another list (containing state abbreviation and state name)
with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")
for index, state in enumerate(states):
	states[index] = state.split("\t")
print(states)

firstAbbrev = states[0][0]
print(firstAbbrev)

print(states[0][0][0])

print(states[3][0])

# # Exercise: Part One
# # Open states file and use it to create two lists:
# # One with state abbreviations
# # One with state names

# # Open file
with open("states.txt", "r") as states_file:
	# # Create states list by reading file and splitting on newlines
	states = states_file.read().split("\n")
# # Create improved states list by turning each item in this list into another list with state abbreviation and state name
for index, state in enumerate(states):
	states[index] = state.split("\t")
# # Create state abbreviation list
# # Create state name list
stateAbbreviationList = []
stateNameList = []
for state in states:
	stateAbbreviationList.append(state[0])
	stateNameList.append(state[1])
print(stateAbbreviationList)
print(stateNameList)

# # Exercise: Part Two
# # Instead of printing, loop through your two lists to write to files

# # Example:
# # This doesn't work because we can't use write() with a list
# # .write() only works with strings
# with open("state-abbrev.txt", "w") as abbrev_file:
# 		abbrev_file.write(stateAbbreviationList)

# # This creates a file, but it doesn't look very nice - state abbreviations all run together
with open("state-abbrev.txt", "w") as abbrev_file:
	for stateAbbreviation in stateAbbreviationList:
		abbrev_file.write(stateAbbreviation)

# # This creates the state abbreviation file with newlines
with open("state-abbrev.txt", "w") as abbrev_file:
	for stateAbbreviation in stateAbbreviationList:
		abbrev_file.write(stateAbbreviation+"\n")

# # This creates the state name file with newlines 
with open("state-name.txt", "w") as name_file:
	for stateName in stateNameList:
		name_file.write(stateName+"\n")

# # Dictionaries: Why

# # To create a list of names and Github handles for each student in the class, we could create a list of lists...

# # We'd have to loop through each list and look for a member in that list...

# # ... there's got to be a better way!

# # Dictionaries are another way of storing information in Python
# # They have two components: a key and a corresponding value
# # This can be thought of like a phone book or contact list - if you know a name (key) you can look up a number (value)

# # Dictionaries: Syntax

phonebook = {}

phonebook = {
	"Shannon": "202-555-1234",
	"Bridgit": "703-555-9876",
	"Christine": "410-555-1293"
}


# # Reading dictionaries is different from reading strings and lists
# # Reading part of a string:
name = "Shannon"
print(name[0:5])
# # Reading part of a list:
attendees = ["Amy", "Jen", "Julie"]
print(attendees[:3])
# # Reading part of a dictionary:
print(phonebook["Shannon"])
print(phonebook["Bridgit"])
print(phonebook["Christine"])

# # Lists Within Lists

# # Dictionaries: Syntax

# # Adding to a dictionary:
phonebook["Mel"] = "301-555-1111"

# # Reading from a dictionary (error prone):
# # print(phonebook["Frankenstein"])
# # This gives a KeyError

# # Reading from a dictionary (no error):
print(phonebook.get("Frankenstein"))

# # What's None?

# # None is a special type in Python, similar to True or False
# # None is returned by the .get() dictionary method when it couldn't find the key you're looking for.
# # By default, .get() will give you None when it didn't find the key you were looking for.
# # But you can tell it to give you a different value -- anything you wnat! A string, an empty dictionary, anything you can think of!

number = phonebook.get("Frankenstein","I couldn't find that name!")
print(number)

# # Dictionaries: Syntax
# # Dictionaries can contain strings, lists, or other dictionaries.

# # Dictionary Methods

# # .keys() will create a list of all the keys in your dictionary.
# # Because dictionaries are unordered, you might get keys in a different order 

# # Dictionaries Are Unordered
# # Dictionaries themselves have no ordering, but we can order their keys

# # Dictionary Methods

# # .items() will create a list of all the key/value pairs in your dictionary
