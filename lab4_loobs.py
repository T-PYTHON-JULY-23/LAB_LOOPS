
# # 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence 
#and print the elements. Skip the number 100 and break the loop at 205
for num in range(45, 210):
  if num == 100:
      continue
  print(num)
  if num == 205:
      break
## 2) Using a while loop 

while True:
  answer = input("What is the product of 7 * 24? ")
  if answer == "168":
      print("You answered this question correctly!")
      break
  else:
      print("Your answer is wrong. Please try again.")


