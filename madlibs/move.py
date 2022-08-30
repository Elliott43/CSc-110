###
### Author: Elliott Cepin
### Class: CSc 110
### Description: creates a fun story with promts answered by the user
###

from ans import ans

if __name__ == "__main__":
    female = ans("A female name:", formatting_for_the_stupid_autograder="", newline=True)
    street = ans("A street name:", formatting_for_the_stupid_autograder="", newline=True)
    male = ans("A male name:", formatting_for_the_stupid_autograder="", newline=True)
    ob = ans("An object:", formatting_for_the_stupid_autograder="", newline=True)
    vehicle = ans("A vehicle:", formatting_for_the_stupid_autograder="", newline=True)
    adj = ans("An adjective:", formatting_for_the_stupid_autograder="", newline=True)

    print(f"""----------
{female} decided to move from her apartment on 5th
to a condo on {street}. She called her friend {male}
for help. However, they could not fit {ob} into
the moving truck, so they had to rent a {adj} {vehicle}
in order to move it!""")