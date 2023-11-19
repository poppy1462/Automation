import random

my_num = random.randint(0, 50)
print(my_num)


def guess_numbers():
    for i in range(7):
        user_number = input("Enter the number:\n")
        if int(user_number) < my_num:
            print("The value is too low")
        elif int(user_number) > my_num:
                print("The number is too high")
        else:
            print("You guessed correctly")
            break


guess_numbers()
