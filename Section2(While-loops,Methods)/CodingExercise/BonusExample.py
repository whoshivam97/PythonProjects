The first one is a very small program where we ask the user to enter a password, and then we try to check
if the password is correct.
If it is correct, we tell the user that the password was correct.
If it's not, we continue to ask the user to enter a password over and over again.

password = input("Enter your password: ")
while password != "pass123":
    password = input("Enter your password: ")
print("Password is correct")


This time I want to use the World Loop to produce a series of numbers as output.
So I want to produce numbers from one, two, three, four, five, six.
x = 1
while x <= 6:
    print(x)
    x = x + 1
