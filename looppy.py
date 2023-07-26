for num in range (45,210) :
    if num == 100:
        continue
    if num == 205:
        break
    print(num)
Question = "What is the prodect of 7*24?"

while int(input(Question)) != 168: 
    print("Your Answer is weong try again..")
    
else: 
    print("You answered this Question correctly")