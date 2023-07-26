n = int(input("Enter a positive integer: "))
sum = 0

for num in range(1, n+1):
    if num % 2 == 0:
        sum += num

print("The sum of even numbers between 1 and {} is {}.".format(n, sum))