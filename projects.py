def length_converter():
    print("1. km to miles")
    print("2. miles to km")
    print("3. meter to feet")
    print("4. feet to meter")
    choice = input("Choose (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Select 1 to 4.")
        return
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == "1":
        print(f"{value:g} km = {value * 0.621371:.2f} miles")
    elif choice == "2":
        print(f"{value:g} miles = {value / 0.621371:.2f} km")
    elif choice == "3":
        print(f"{value:g} m = {value * 3.28084:.2f} feet")
    else:
        print(f"{value:g} feet = {value / 3.28084:.2f} m")


def weight_converter():
    print("1. kg to g")
    print("2. g to kg")
    print("3. kg to pounds")
    print("4. pounds to kg")
    choice = input("Choose (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Select 1 to 4.")
        return
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == "1":
        print(f"{value:g} kg = {value * 1000:.2f} g")
    elif choice == "2":
        print(f"{value:g} g = {value / 1000:.2f} kg")
    elif choice == "3":
        print(f"{value:g} kg = {value * 2.20462:.2f} pounds")
    else:
        print(f"{value:g} pounds = {value / 2.20462:.2f} kg")


def temperature_converter():
    print("1. C to F")
    print("2. F to C")
    choice = input("Choose (1-2): ")
    if choice not in ["1", "2"]:
        print("Invalid choice. Select 1 or 2.")
        return
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == "1":
        print(f"{value:g} C = {value * 9 / 5 + 32:.2f} F")
    else:
        print(f"{value:g} F = {(value - 32) * 5 / 9:.2f} C")


def time_converter():
    print("1. hours to minutes")
    print("2. minutes to hours")
    print("3. minutes to seconds")
    print("4. seconds to minutes")
    choice = input("Choose (1-4): ")
    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Select 1 to 4.")
        return
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid value. Enter a number.")
        return

    if choice == "1":
        print(f"{value:g} hours = {value * 60:.2f} minutes")
    elif choice == "2":
        print(f"{value:g} minutes = {value / 60:.2f} hours")
    elif choice == "3":
        print(f"{value:g} minutes = {value * 60:.2f} seconds")
    else:
        print(f"{value:g} seconds = {value / 60:.2f} minutes")


# Main menu
print("===== Unit Conversion System =====")
print("1. Length")
print("2. Weight")
print("3. Temperature")
print("4. Time")

menu = input("Select category (1-4): ")

if menu == "1":
    length_converter()
elif menu == "2":
    weight_converter()
elif menu == "3":
    temperature_converter()
elif menu == "4":
    time_converter()
else:
    print("Invalid choice. Select 1 to 4.")