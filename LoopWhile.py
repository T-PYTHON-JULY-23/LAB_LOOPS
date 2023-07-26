
# Q1
number_range = range(45,211)

for number in number_range:
    if number == 100:
        pass
    elif number == 205:
        break
    else:
        print(number)


# Q2 
Q ="what is the product of 7 * 24 ?"

while input(Q) != "168":
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")
