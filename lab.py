r = range(45, 210)

for i in r:
    if i == 100:
        continue
    if i == 206:
        break
    print(i)

question =  "what is the product of 7 * 24 = ?"
while int(input(question)) != 7*24:
    print("please try again..")
else:
    print("GOOD JOP !! correct answer")