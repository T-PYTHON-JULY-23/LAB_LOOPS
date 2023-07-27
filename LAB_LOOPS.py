

numbers_range =range(45,210) 
for number in numbers_range:
    
    if number ==205:
        break
    elif  number == 100:
        continue
    print(number)
    

         
product =  "what is the product of 7 * 24 ?"

while int(input(product))!= 168:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")