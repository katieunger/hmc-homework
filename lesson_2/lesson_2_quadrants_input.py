# # Quadrants Exercise

# # Use raw_input() to allow a user to type
# # Allow user to enter 3 addresses; after three, print the length and contents of each list
# address = raw_input("What is your address? ")
# To run this, use terminal:
# cd to file location
# Execute the file using the Python interpreter:
# (type python and then the filename)
# or use chmod to change the access mode of the file:
# (type chmod a+x and then the filename)
# This gives permission to all users to execute the file
# However, I still got syntax errors using this approach because
# the file was not being executed using Python interpreter

# For Python v3.x as raw_input() was renamed to input()
# # Creating array to hold addresses
addresses = []
# # Using range to prompt user to enter an address 3 times
for number in range(3):
	address = raw_input("Enter address {0}: ".format(number+1))
	addresses.append(address)
print("Address list: {0}\n".format(addresses))

NW = []
NE = []
SE = []
SW = []
other = []

quadrantList = [NW, NE, SE, SW, other]

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
print("List of addresses grouped by quadrant, made using a loop and splitting addresses on ' ':\n{0}\n".format(quadrantList))