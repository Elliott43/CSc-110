###
### Author: Elliott Cepin
### Course: CSc 110
### Description: Builds a TIE fighter
###



# This library holds a function that basically just does, for our present purposes, int(input(message + "\n")) w/flashy error handeling
import ans
if __name__ == "__main__":
    width = ans.ans("Enter TIE width:", formatting_for_the_stupid_autograder="", newline=True, get_int=True)
    character = "\\"
    print(f"""|[{" " * (width*2 + 9)}]|
|[{" " * (width + 1)}/=---=\{" " * (width + 1)}]|
|[{"/" * width}|== X ==|{character * width}]|
|[{" " * (width + 1)}\=---=/{" " * (width + 1)}]|
|[{" " * (width*2 + 9)}]|""")