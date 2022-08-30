###
### Author: Elliott Cepin
### Class: CSc 110
### Description: creates a fun story with promts answered by the user
###
import ans

questions = {
    "male"  : "A male name:",
    "female": "A female name:",
    "pet"   : "A pet name:",
    "place" : "A place:",
    "adj"   : "An adjective:",
    "animal": "An animal:",
    "ing"   : "A verb ending in ing:",
    "adverb": "An adverb:"
}
light_copy = questions.copy()
for i,j in questions.items():
    light_copy[i] = ans.ans(j, formatting_for_the_stupid_autograder="", newline=True)

print(f"""----------
{light_copy["male"]} and {light_copy["female"]} were best friends.
One day {light_copy["male"]} and {light_copy["female"]} decided to go on a
vacation to {light_copy["place"]}. However, they didn't know
what to do with their {light_copy["adj"]} pet {light_copy["animal"]} named {light_copy["pet"]}.
{light_copy["pet"]} had been causing problems, due to constant {light_copy["ing"]}.
{light_copy["male"]} found a sitter for their pet, and {light_copy["adverb"]} went on the trip.""")