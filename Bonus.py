
positive = input("Enter a positive integer:")
sum_all_even =0
positive_int = int(positive)

for number in range(positive_int+1):
    if number%2 == 0:
        sum_all_even += number

print(f"The sum of even numbers between 1 and {positive_int} is {sum_all_even}.")