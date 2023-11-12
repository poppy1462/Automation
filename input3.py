user_name = input("Hello! This program can create a short bio for you. To use the feature please enter your name:\n")
user_age = input("Please enter your age:\n")
user_hobby = input("What's your hobby?\n")


print("Hi! My name is " + user_name + ". It's nice to meet you.")
print("I am " + user_age + " years old. Did you know that Python is 32 years old?")
if int(user_age) < 32:
    python_age = 32 - int(user_age)
    print("I am " + str(python_age) + " years younger than Python.")
else:
    python_age_older = int(user_age) - 32
    print("I am " + str(python_age_older) + " years older than Python.")
print("My favorite thing to do is " + user_hobby)

prediction = int(user_age) + 1
user_future = input("I can also predict future. Would you like me to? (enter 'yes' or 'no')\n")
if user_future == "yes":
    print("Next year you will turn " +str(prediction)+ " and you will enjoy " +user_hobby)
