#write a program to cheak whether the given number is palindrome or not
num = int(input("Enter a number: "))
temp = num
reverse = 0
while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if(temp == reverse):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    