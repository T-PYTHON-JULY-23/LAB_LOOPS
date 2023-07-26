lim = int(input("Enter a positive integer:"))
r = range(1, lim + 1)
sum = 0
for num in r:
    if num % 2 != 0:
        continue   
    sum = sum + num

print(f"The sum of even numbers between 1 and {lim} is {sum}") 