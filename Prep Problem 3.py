import ans

# while nothing in this code intrinsically hasn't been taught yet...
# (im not sure if string multiplication (is it called concatenation when you are multiplying too?) has been taught)
# The stuff in the library certainly hasn't been taught, but I really like the library, works fine with int(input())
# I don't know how to achieve this result without try statements though
print("we are going to make a rectangle")
w = ans.ans("please provide a width", get_int=True)
h = ans.ans("please provide a height", get_int=True)

for i in range(h):
    print("#"*w)
