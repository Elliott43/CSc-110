menu ={
    "large": {
        "regular": 300,
        "diet": 100,
        "water": 0
    },
    "small": {
        "regular": 150,
        "diet": 50,
        "water": 0
    }
}

drink_size = input("Drink Size:\n").strip().lower()
drink_type = input("Drink type:\n").strip().lower()

print()
print(menu[drink_size][drink_type], "calories")