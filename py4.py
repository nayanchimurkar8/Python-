x= input("enter your role:").lower()
age= int(input("enter age:"))
eligibal= (x == "student")and (age < 21)
print ("eligibal for discount:", eligibal)
