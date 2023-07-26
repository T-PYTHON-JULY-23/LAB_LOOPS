"""# LAB_LOOPS

## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205


"""
rangeRange=range(45,210)
for i in rangeRange : 
    if i==100:
        continue
    if i==205:
        break
    print(i)