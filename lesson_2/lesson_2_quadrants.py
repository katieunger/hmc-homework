# # Quadrants Exercise

# # Use raw_input() to allow a user to type
# # Allow user to enter 3 addresses; after three, print the length and contents of each list
# address = raw_input("What is your address? ")

# # For now, let's just create lists:
address1 = "815 16 St NW Washington D.C. 20005"
address2 = "123 SEA LANE SW"
address3 = "125 L'Enfant Plaza SW Washington D.C. 22033"

addresses = [address1, address2, address3]
print("Address list: {0}\n".format(addresses))

NW = []
NE = []
SE = []
SW = []
other = []

quadrantList = [NW, NE, SE, SW, other]

# # If that address contains a quadrant (NW, NE, SE, SW), then add it to that quadrant's list
# # Using only if/elif/else statements to group addresses by quadrant:
if "NW" in address1:
	NW.append(address1)
elif "NE" in address1:
	NE.append(address1)
elif "SE" in address1:
	SE.append(address1)
elif "SW" in address1:
	SW.append(address1)
else:
	other.append(address1)

if "NW" in address2:
	NW.append(address2)
elif "NE" in address2:
	NE.append(address2)
elif "SE" in address2:
	SE.append(address2)
elif "SW" in address2:
	SW.append(address2)
else:
	other.append(address2)

if "NW" in address3:
	NW.append(address3)
elif "NE" in address3:
	NE.append(address3)
elif "SE" in address3:
	SE.append(address3)
elif "SW" in address3:
	SW.append(address3)
else:
	other.append(address3)

print("\nList of addresses grouped by quadrant, made using if/elif/else:")
print("NW List: {0}".format(quadrantList[0]))
print("NE List: {0}".format(quadrantList[1]))
print("SE List: {0}".format(quadrantList[2]))
print("SW List: {0}".format(quadrantList[3]))
print("Other List: {0}".format(quadrantList[4]))

# # Clearing out quadrant lists
NW = []
NE = []
SE = []
SW = []
other = []

quadrantList = [NW, NE, SE, SW, other]

# # Try quadrant exercise with loops instead of repeating if statements
# # Using a loop to group addresses by quadrant:
for address in addresses:
	if "NW" in address:
		NW.append(address)
	elif "NE" in address:
		NE.append(address)
	elif "SW" in address:
		SW.append(address)
	elif "SE" in address:
		SE.append(address)
	else:
		other.append(address)
print("\nList of addresses grouped by quadrant, made using a loop:")
print("NW List: {0}".format(quadrantList[0]))
print("NE List: {0}".format(quadrantList[1]))
print("SE List: {0}".format(quadrantList[2]))
print("SW List: {0}".format(quadrantList[3]))
print("Other List: {0}".format(quadrantList[4]))

# # Clearing out quadrant lists
NW = []
NE = []
SE = []
SW = []
other = []

quadrantList = [NW, NE, SE, SW, other]

# # SEA LANE is a problem because it's being added to the NE list even though it should be in SW list because "NE" string appears in address
# # We can correct this by splitting the addresses on space characters, which will make lists out of the strings making up each address
# # Then we can check if the quadrant appears in that address list
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
print("\nList of addresses grouped by quadrant, made using a loop and splitting addresses on ' ':")
print("NW List: {0}".format(quadrantList[0]))
print("NE List: {0}".format(quadrantList[1]))
print("SE List: {0}".format(quadrantList[2]))
print("SW List: {0}".format(quadrantList[3]))
print("Other List: {0}".format(quadrantList[4]))