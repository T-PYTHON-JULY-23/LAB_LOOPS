n = int(input("Enter a posituve number:"))
sum = 0
for i in range(1,n+1):
    if i%2==0:
      sum=sum+i
      print("the sum of the even numbers is",sum)