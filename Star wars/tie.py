import ans
if __name__ == "__main__":
    width = int(input(">> "))#ans.ans("Enter TIE width:", formatting_for_the_stupid_autograder="", newline=True, get_int=True)
    character = "\\"
    print(f"""|[{" " * (width*2 + 9)}]|
|[{" " * (width + 1)}/=---=\{" " * (width + 1)}]|
|[{"/" * width}|== X ==|{character * width}]|
|[{" " * (width + 1)}\=---=/{" " * (width + 1)}]|
|[{" " * (width*2 + 9)}]|""")