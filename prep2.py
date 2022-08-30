###
### Author: Your name here
### Course: CSc 110
### Description: prompts the user for an eye character and, once a valid character is recieved, prints a little guy
###

eyes = ""
while len(eyes) != 1:
    eyes = input("Eye style: ")
    if len(eyes) != 1:
        print("Only one character please.")
        print()

# I just read the style guide, and it says i shouldn't use things that haven't been covered yet
# I don't think while loops or f-strings have been covered
# Does that mean I should not use them?
print(f"""

|||||||
| {eyes} {eyes} |
|  _  |
 -----""")
