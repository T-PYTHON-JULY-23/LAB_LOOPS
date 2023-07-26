#Bonus

n=int(input("Enter a positive integer: "))
sum=0
for i in range(1, n + 1):
    if i % 2 == 0:
      sum += i
else:
    print(f"The sum of even numbers between 1 and {n} is {sum}.")