#Sum of Even Numbers
integer=int(input("Enter a positive integer: "))
for number in range(1,integer):
    if number%2 == 0 :
        continue 
else:
  print(f"The sum of even numbers between 1 and {integer} is {30}.")
