###
### Author: Elliott Cepin
### Course: CSc 110
### Description: Decides temperatures
###

temp = input("Temperature in fahrenheit:\n").strip()
temp_temp = temp
if temp.startswith("-"):

    # temporary temperature
    temp_temp = temp[1:]

if temp_temp.isnumeric():
    temp = int(temp)

else:
    exit()


if temp <= 32:
    print("Ice")

elif temp < 212:
    print("Water")

else:
    print("Steam")



