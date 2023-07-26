num=int(input("Enter postive number:"))
f = 0 
for nmu in range(1,num+1): 
    if(nmu %2 == 0):
        print ("{0}".format(nmu))
        f = f + nmu 
    print(f"The Sum of even numbers btween 1 and {num} is{f}.")