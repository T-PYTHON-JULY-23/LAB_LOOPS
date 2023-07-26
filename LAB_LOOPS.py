

numbers_range =range(45,210) 
for number in numbers_range:
    if  number == 100:
        break
    elif number ==210:
         continue
         

product =  "what is the product of 7 * 24 ?"

while input(product) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")