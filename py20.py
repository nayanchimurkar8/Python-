#Alphabet Diamond Pattern
n=int(input("Enter no of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print(chr(65+j), end=" ")
    print()
for i in range(n-2, -1, -1):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        print(chr(65+j), end=" ")
    print()