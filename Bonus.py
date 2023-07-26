print(" ''' Hello ... here we can help you to calculates the sum of all even numbers from 1 to any number you want " ,("\U0001F600") , ("'''"))
pos_int = int(input("Please enter a positive integer :"))
sum = 0
for number in range(1 , pos_int + 1):
        if (number %2 ==0 ):
           sum = sum + number
print(f"The sum of even numbers between 1 and {pos_int} is {sum}")