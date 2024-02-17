from datetime import datetime


while True:
    user_input = input("Enter the date in the specified format (MM-DD-YYYY) to get the corresponding day of the week\n")
    if user_input == "stop":
        break
    try:
        user_input_str = datetime.strptime(user_input, "%m-%d-%Y")
        day_of_week = user_input_str.strftime("%A")
        print(f"The entered date {user_input} is {day_of_week}")
    except ValueError:
        print("The entered format is incorrect. Please try again.")
        raise








