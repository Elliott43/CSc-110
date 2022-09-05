import ans
if __name__ == "__main__": pass
legs = """     ([])         ([])
    /||||\\       /||||\\
   |=}--{=|     |=}--{=|
  .-4----4-.   .-4----4-."""
illegal_character = "}"


head = """     _..-Y  |  |  Y-._
 .--"   ||  |  |  |   "-."""

leg_length = "     |\\n|         |\\n|\n"
head_length = " |______________________|\n"


neck_length = ans.ans("Neck Length:", formatting_for_the_stupid_autograder="", get_int=True, newline=False)
head_height = ans.ans("Head Height:", formatting_for_the_stupid_autograder="", get_int=True, newline=False)
height = ans.ans("Leg Height:", formatting_for_the_stupid_autograder="", get_int=True, newline=False)
print(head)
body = f""" |______________________|    _____
 L______________________[{"-" * neck_length}----------).
I____________________ [__L]{"_" * neck_length}[----(_{illegal_character}--P
L________________________j~ {" " * neck_length}'+++++++//
\________________________]
  [___________________]
     I--I"~~""\"~~"I--I"""
# end="" means that the print statement will not automatically create a newline
print(head_length*head_height, end="")
print(body)

# same as before with end="" (\n is at the end of leg_length, so it is not necessary)
print(leg_length*height, end="")
print(legs)
