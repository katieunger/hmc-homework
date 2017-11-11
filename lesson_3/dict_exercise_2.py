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
contacts["ZAliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Katie"] = {"twitter":"@KatieMode", "github":"https://github.com/katieunger"}
print(contacts)

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

print(contacts.keys())

for contact in contacts.keys():
    print(contact)

for contact in contacts.keys():
    print(contacts[contact])

for contact in sorted(contacts.keys()):
    print(contacts[contact]["twitter"])
# # This prints twitter handles alphabetically in order of name!

print(contacts.items())

for contact in sorted(contacts.keys()):
    print("{0}'s info:".format(contact))
    print("\t\t\ttwitter: {0}".format(contacts[contact]["twitter"]))
    print("\t\t\tgithub: {0}".format(contacts[contact]["github"]))

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner
