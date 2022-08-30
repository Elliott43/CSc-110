import ans

# while nothing in this code intrinsically hasn't been taught yet...
# (im not sure if string multiplication (is it called concatenation when you are multiplying too?) has been taught)
# The stuff in the library certainly hasn't been taught, but I really like the library, works fine with int(input())
# I don't know how to achieve this result without try statements though

# I did have to add formatting and newline to ans.ans, because of the autograder
w = ans.ans("Rectangle width: ", get_int=True, formatting_for_the_stupid_autograder="", newline=False)
h = ans.ans("Rectangle height: ", get_int=True, formatting_for_the_stupid_autograder="", newline=False)
print()

for i in range(h):
    print("#"*w)
