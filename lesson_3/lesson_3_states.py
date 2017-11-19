# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

with open("states.txt", "r") as states_file:
	statesList = states_file.read().split("\n")

for index, state in enumerate(statesList):
	statesList[index] = state.split("\t")

print("<select>")
for state in statesList:
	print("<option value='{0}'>{1}</option>".format(state[0], state[1]))
print("</select>")

# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

with open("states.html", "w") as statesSelectFile:
	statesSelectFile.write("<select>\n")
	for state in statesList:
		statesSelectFile.write("\t<option value='{0}'>{1}</option>\n".format(state[0], state[1]))
	statesSelectFile.write("</select>")

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

# # Make a states dictionary using state_info.csv
with open("state_info.csv", "r") as stateInfoFile:
	stateInfoList = stateInfoFile.read().split("\n")

for index, state in enumerate(stateInfoList):
	stateInfoList[index] = state.split(",")
print(stateInfoList)

statesDictionary = {}
for state in stateInfoList:
	statesDictionary[state[1]] = {
		"popRank":state[0],
		"popEst":state[2],
		"houseSeats":state[3],
		"percentPop":state[4]
	}
print(statesDictionary)

# # Use dictionary to write states-table.html
with open("states-table.html", "w") as statesTableFile:
	for state in sorted(statesDictionary.keys()): 
		statesTableFile.write("<table border='1'>\n")
		statesTableFile.write("\t<tr>\n")
		statesTableFile.write(("\t\t<td colspan='2'>{0}</td>\n").format(state))
		statesTableFile.write("</table>\n")


# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.