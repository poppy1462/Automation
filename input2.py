def print_sum_avg_args(*args):
    sum = 0
    for i in args:
        sum += i
    avg = sum/len(args)
    print(sum,avg)

print(print_sum_avg_args(1,2,3))
