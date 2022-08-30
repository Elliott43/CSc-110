import ans

width = int(input(">> "))#ans.ans("Enter TIE width:", formatting_for_the_stupid_autograder="", newline=True, get_int=True)
character = "\\"
print(f"""|[ {" " * (2 * width + 7)}]|
|[ {" " * width}/=---=\\{" " * width}]|
|[{"/" * width}|== X ==|{character * width}]|
|[ {" " * width}\=---=/{" " * width}]|
|[ {" " * (2 * width + 7)}]|""")