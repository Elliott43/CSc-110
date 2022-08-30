# This function is my pride and joy (also, it worked first try)
def ans(message="", options=(), get_int=False):
    assert not (options and get_int), "two conflicting parameters, 'options' and 'get_int', were assigned values"
    output = None

    if message:
        print(message)

    if options:
        for i, j in enumerate(options):
            print(f"\t{i + 1}) {j}")

        output = options[ans(get_int=(1, len(options)))-1]

    elif get_int:
        assert type(get_int) in [tuple, bool], f"parameter, 'get_int', was assigned a value with an invalid type: {type(get_int)}"
        not_in_range = ""

        try:
            output = int(input(""))

            if isinstance(get_int, tuple):
                if not ((output >= get_int[0]) and (output <= get_int[-1])):
                    not_in_range = f"Integers from {get_int[0]} to {get_int[-1]} are considered valid\n"
                    raise ValueError

        except ValueError:
            print("Please enter a valid integer")
            print(not_in_range, end="")

            output = ans(get_int=get_int)

    else:
        output = input("")

    # I am aware that in a majority of the places where there is an "output = thing" I could have put a "return thing"
    # That was aesthetically (and also maybe programmatically) unpleasing
    return output

def mad_lib_handler(story, *questions):
    answers = []
    for j in questions:
        answers.append(ans(j))
    split_story = story.split("???")
    new_story = ""
    index = 0
    for i in answers:
        new_story += split_story[index]
        new_story += i
        index += 1

    return new_story
    
