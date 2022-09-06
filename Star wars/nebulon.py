###
### Author: Your name here
### Course: CSc 110
### Description: Builds a nebulon
###

# This one doesn't use ans.ans, because I got kinda nervous about my grade
# it's not like it's a thing that actually effects the program, i just like how it's written
# it isn't worth losing points over. it's just for fun



# Each of these do the same things
#    assign user_input to input()
#    if the string user_input only contains numbers
#        variable = user_input as an integer
#    otherwise
#        exit program
#    if i don't prgram it like this
#        this code would be 4 times as long
#        I get a better grade on the code
#    otherwise
#        The code is 1 line per variable
#        I get a worse grade
large_layer_count = int(user_input) if (user_input := input("Large Layers on bottom:\n")).isnumeric() else exit()
medium_layer_count = int(user_input) if (user_input := input("Medium Layers on bottom:\n")).isnumeric() else exit()
small_layer_count = int(user_input) if (user_input := input("Small Layers on bottom:\n")).isnumeric() else exit()
length = int(user_input) if (user_input := input("Front length:\n")).isnumeric() else exit()

main_ship = f"""\n  /={"-"*length}\\                 /--------|
 /=={"/"*length}====\\            |=========|
|==-{"/"*length}======\----================|
 \\=={"="*length}==-------------------------|
  \\={"-"*length}=///              \=======/\n"""

# makes each layer using the formulas provided in the assignment
# layercount decides the important stuff
# math woulda been way easier, simpler, and cleaner with len()
large_layer = f"{' ' * 4}\\{'-' * (length-4)}|\n" * large_layer_count
medium_layer = f"{' ' * ((length//2) + (length % 2))}:{'+' * (length // 2)}|\n" * medium_layer_count

# takes the amount of spaces in medium_layer's beginning, and then adds the difference between the formulas given for the size of
#   medium layer and the size of small layer
small_layer = f"{' ' * ((length//2) + (length % 2) + ((length//2) - (length // 3)))}\\{'#' * (length // 3)}|\n" * small_layer_count

# sep="" is an argument of the print function that decides what happens between
print(main_ship, large_layer, medium_layer, small_layer, sep="")
        