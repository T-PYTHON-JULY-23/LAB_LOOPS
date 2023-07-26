## 1)
element_in_range = range(45,210)

for print_element in element_in_range :
    if print_element == 100 :
        continue
    elif print_element == 205 :
        break
    print(print_element)
## 2)
answer ="what is the product of 7 * 24 ?"
while int(input(answer)) != 168 :
    print("Your Answer is wrong try again..")
    continue
else :
    print("You answered this Question correctly")
