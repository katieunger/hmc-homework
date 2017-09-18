# # Intro to Python

# # Useful shortcut: Press command + B to run in the console
# # in Sublime Text.

# # Variables
# # These variables are used throughout Lesson 1.
twitter = "@hearmecode"
members = 902
article = """At Hear Me Code, students are teachers in training.
The key to the classes' appeal, said Criqui, who is now an assistant
at Hear Me Code? "It's by women, for women," she said..."""
phone1 = "(202) 456-7890"
name = "Shannon"
age = 29
phone2 = "202-555-6789"
tweet = """In just over one year, @hearmecode has reached
over 800 members who are learning how to code together."""
address = "                1600 Pennsylvania Avenue"
email = "shannon@hearmecode.com"
gender = "F"

# # The Print Command

# This will print a line of text:
print "Watch out, world!"

# This will print the string we stored in the variable twitter
print twitter

# This will print the number we stored in the variable members
print members

# This will print out the word "twitter"
print "twitter"

# Strings - The Basics

# A string which contains any single quotes should be contained 
# within double quotes.
print "My governor's name is Martin O'Malley"

# This print causes a syntax error because the single quote
# in O'Malley is interpreted by Python as the end of the string.
# print My governor's name is Martin O'Malley'

# # \n starts a new line
# # \t inserts a tab
print "Contact Info: \nShannon \tshannon@hearmecode.com"

# # Strings - Quick Exercise

print "Lesson \t\tTopic\n1\t\t\tStrings and Conditionals\n2\t\t\tLists and Loops\n3\t\t\tDictionaries & Files"

# # How Long Is My String?

# # This prints the length of the string stored in the twitter
# # variable ("@hearmecode") - which is 11 characters.
print len(twitter)

# # Strings: Slicing

# # The index starts at 0!
# # This will slice the string stored in the twitter variable
# # at the index 0 (the first character) - giving me "@""
print twitter[0]

# # This will slice the string stored in the twitter variable
# # to include character at index 1 (the second character)
# # and all the characters up until index 5 - it does not include
# # the character at [5] (the sixth character).
# # This will print 4 characters - "hear"
print twitter[1:5]

# # If you do not include a left (start) index, Python starts
# # at the beginning and prints up until right index.
# # This will print "@hear"
print twitter[:5]

# # Similarly, if you do not include a right (end) index, Python
# # will print from the left index until the end.
# # This will print "hearmecode"
print twitter[1:]

# # Strings: Slicing Exercise

# # Print area code of the phone number stored in the phone1
# # variable.
print phone1[1:4]

# # Print the are code (including the parentheses) of phone1.
print phone1[:6]

# # Print the middle 3 numbers of phone1.
print phone1[6:9]


# # Strings: String Formatting

# # Using the format function allows us to insert the values
# # of variables into strings.
# # This will print "My name is: Shannon and my age is: 29"
print "My name is: {0} and my age is: {1}".format(name,age)

# # A string can be sliced within the format function.
# # This will print "Call 555-6789 for great pizza"
print "Call {0} for great pizza".format(phone2[4:])

# # This will print the number of characters remaining (out of 140)
# # in the tweet string - using the len method inside the format function.
print """That tweet is {0} characters. You have {1} characters left.""".format(len(tweet), 140-len(tweet))

# # Strings: Formatting Exercise

# # Slice phone2 into the area code:
areaCode = phone2[:3]

# # Slice phone2 into the local number:
local = phone2[4:]

print "Area Code: {0}".format(areaCode)
print "Local: {0}".format(local)
print "Different format: ({0}) {1}".format(areaCode,local)

# # Strings: String Methods

# # This will find and print the index of the "@" character in the 
# # email string.
print email.find("@")

# # This returns an index of -1 because there is no "Z" in the email!
print email.find("Z")

# # This will replace the "@" character with the "#" character
# # in the twitter string. 
print twitter.replace("@","#")

# # By printing twitter now, we can see that the value of the variable
# # twitter was not changed above.
print twitter

# # To make @hearmecode into a hashtag, we can save the value in a
# # new variable:
hashtag = twitter.replace("@","#")
print "Hashtag: {0}".format(hashtag)
print "Twitter: {0}".format(twitter)
# # We can see that printing hashtag prints #hearmecode
# # and printing twitter prints @hearmecode

# # How Functions Work

# # Return Values

# # Using len, we can save the value of the length of the tweet 
# # variable to a new variable (length).
length = len(tweet)
print "Length: {0}".format(length)

# # Using find, we can save the index of the "(" character in phone1
position = phone1.find("(")
print "Position: {0}".format(position)

# # Strings: String Methods

# # Strip will remove the leading and trailing whitespace from the 
# # string stored in the address variable, but leave all spaces inside
# # the string
print "Address: {0}".format(address.strip())

# # Lower will lowercase all characters in a string
print gender.lower()

# # Upper will uppercase all characters in a string
print gender.upper()

# # Title will uppercase the first letter of each word.
sentence = "Make me a title"
print sentence.title()

# # Count will find all occurences of a string.
print article.count(" he said")
print article.count(" she said")

# # Conditionals
# # Conditionals let you compare things and use the results of the comparisons
# # to make decisions, or make your program behave differently

# if gender == 'F':
# 	print "Welcome to Hear Me Code"

# # Vars for Conditional Exercises
students = 50
capacity = 50
teaching_assistants = 5

# if students <= capacity:
# 	print "Keep recruiting"
# else:
# 	print "End ticket signups"



# if students <= capacity:
# 	print "Keep recruiting"
# else:
# 	print "End ticket signups"

# if teaching_assistants == 0:
# 	print "None? Uh oh!"
# elif teaching_assistants < students / 5:
# 	print "Keep recruiting TAs"
# else:
# 	print "Aren't the TAs great though?"

# print 5 > 5
# print 5 >= 5

# # Conditional Exercise
# volunteers = 90
# goal = 100
# if volunteers < goal:
# 	volunteersNeeded = goal - volunteers
# 	print "You are behind by {0} volunteers.".format(volunteersNeeded)
# elif volunteers > goal:
# 	extraVolunteers = goal - volunteers
# 	print "You have surpassed your goal by {0} volunteers.".format(extraVolunteers)
# elif volunteers == goal:
# 	print "You have met your goal exactly!"
# else:
# 	print "Something ain't right."

# # Complex Conditionals
if gender.lower() == "f":
	print "Welcome to Hear Me Code"