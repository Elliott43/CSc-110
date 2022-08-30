### 
### Author: Your Name Here
### Class: CSc 110
### Description: A fun madlib game
###

from funclib import mad_lib_handler

story = """??? and ??? were best friends.
One day ??? and ??? decided to go on a
vacation to ???. However, they didn't know
what to do with their ??? pet ??? named ???.
??? had been causing problems, due to constant ???.
??? found a sitter for their pet, and ??? went on the trip."""

print(mad_lib_handler(story, *[
    "A male name:",
    "A female name:",
    "A pet name:",
    "A place:",
    "An adjective:",
    "An animal:",
    "A verb ending in ing:",
    "An adverb:"]))

