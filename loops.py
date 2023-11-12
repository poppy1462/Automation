xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)

#using while loop:
#count = 0
#while count < len(xs):
    #print(xs[count])
    #count += 1


for i in xs:
    print(i, i*i)
    #can also use i**2 for square

total = 0
for i in xs:
    total += i

print(total)


total = 1
for i in xs:
    total *= i

print(total)