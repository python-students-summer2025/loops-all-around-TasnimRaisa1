def get_starting_number():
    while True:
        user_input = input("How many bottles of beer on the wall? ")
        if user_input.isnumeric() and int(user_input) >= 1:
            return int(user_input)
        print("Please enter a number 1 or greater. ")


def sing(starting_number):
    for bottles in range(starting_number, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. ")
            if bottles -1 == 1:
                print("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")


