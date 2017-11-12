contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Katie"] = {"twitter":"@KatieMode", "github":"https://github.com/katieunger"}
print("Exercise 1:\n{0}\n".format(contacts))

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner

print("Exercise 2:")
for contact in sorted(contacts.keys()):
    print("{0}'s info:".format(contact))
    print("\ttwitter: {0}".format(contacts[contact]["twitter"]))
    print("\tgithub: {0}".format(contacts[contact]["github"]))


# # This will print the keys of the contacts dictionary as a list:
print("\nPrinting contacts.keys():")
print(contacts.keys())

# # This will print each contact's key one by one:
print("\nFor loop printing each contact in contacts.keys():")
for contact in contacts.keys():
    print(contact)

# # This will print the dictionary for each contact one by one:
print("\nFor loop printing contacts[contact] for each contact in contacts.keys():")
for contact in contacts.keys():
    print(contacts[contact])

# # This will print the twitter handle for each contact
print("\nFor loop printing the twitter handle for each contact in contacts.keys():")
for contact in sorted(contacts.keys()):
    print(contacts[contact]["twitter"])
# # This prints twitter handles alphabetically in order of name!

print("\nPrinting contacts.items():")
print(contacts.items())