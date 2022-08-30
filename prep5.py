import ans

def main():
    food  = ans.ans("Enter food:", formatting_for_the_stupid_autograder="", newline=True)
    price = ans.ans("Enter price:", formatting_for_the_stupid_autograder="", newline=False, get_int=True)

    word = "expensive" if is_expensive(price) else "affordable"
    print(f"That {food} is {word}.")


PRICE_POINT = 20
is_expensive = lambda cost: cost >= PRICE_POINT

if __name__ == "__main__":
    main()