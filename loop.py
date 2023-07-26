
"""
#1) Using range(), make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
range_num= range(45,210)

for number in range_num:
    
    if number ==100 :
        continue
    if number ==205:
        break
    print(number)
    """
#2) Using a while loop and input , do the following :

qus = "what is the product of 7 * 24 ? "
ansuer=7*24
while int(input(qus))!= 7*24 :
    print("Your Answer is wrong try again.")
else:
    print("You answered this Question correctly")