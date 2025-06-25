def get_starting_number():
    while True:
        if user_input.isnumeric() and int(user_input) >= 1:
            return int(user_input)
        print("please enter a number 1 or greater.")


def sing(starting_number):
    bottles = starting_number
    keep_singing = True

    while keep_singing:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            if bottles -1 == 1:
                print ("Take one down, pass it around, 1 bottle of beer on the wall.\n")
            else:
                print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        elif bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
            keep_singing = False # stop loop after this line

        bottles -= 1

