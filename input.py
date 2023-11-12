numbers = []
def print_sum_avg(numbers):
    sum = 0
    for i in numbers:
        sum += i
    avg = sum/len(numbers)
    print(sum,avg)

def request_numbers(numbers):
    for i in range(3):
        user_number = input("Enter the number:\n")
        num = int(user_number)
        numbers.append(num)
    print_sum_avg(numbers)


request_numbers(numbers)