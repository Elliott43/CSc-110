### 
### Author: Your Name Here
### Class: CSc 110
### Description: A fun madlib game
###
import funclib

story = """??? decided to move from her apartment on 5th
to a condo on ???. She called her friend ???
for help. However, they could not fit ??? into
the moving truck, so they had to rent a ??? ???
in order to move it!"""


print(funclib.mad_lib_handler(story, *[
    "A female name:",
    "A street name:",
    "A male name:",
    "An object:",
    "A vehicle:",
    "An adjective:"
    ]))
