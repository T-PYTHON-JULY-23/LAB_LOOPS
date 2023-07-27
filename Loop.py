## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip ithe number 100 and break the loop at 205
numberes_range=range(45,210)
for x in numberes_range :
    if x==100:
        continue
    print(x)
    if x==205:
        break
    print (x)

## 2) Using a while loop and input , do the following :

puzzle="what is the product of 7 * 24 ?"
while input(puzzle) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")
    
## Bonus

### Sum of Even Numbers

n = int(input("Enter a positive integer: "))
sum =0
for number in range(1, n+1):
    if number %2 == 0:
        sum+= number
print(f"The sum of even numbers between 1 and {n} is: {sum}")
    
    