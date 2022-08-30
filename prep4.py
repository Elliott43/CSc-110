import ans

to_inches = lambda feet: "Inches: " + str(round(feet * 12, 3))
to_meters = lambda feet: "Meters: " + str(round(feet * .3048, 3))
to_rods   = lambda feet: "Rods: "   + str(round(feet * 0.061, 3))


feet = ans.ans("Number of feet:", get_int=True, formatting_for_the_stupid_autograder="", newline=False)
print("", to_inches(feet), to_meters(feet), to_rods(feet), sep="\n")
