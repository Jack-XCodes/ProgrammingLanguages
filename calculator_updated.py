#  Adjust your Simple calculator app to a version that takes the year of birth of a person and
# # calculates their age in years, months and days respectively. Your app should give all three
# # output
from math import floor
print(".....SIMPLE calculator......")

print("The Calculator can be used to \n1.add\n2.minus\n3.multiplication\n4.division\n 5.Exit")
while True:
    #Prompts user to enter the operation of choice
    operation = int(input("Choose your operation from choices above: "))
    #prevents program from executing due to wrong choice and exits if choice is 5
    if operation not in (1, 2, 3,4,5):
        print("Wrong choice,Please try again and give valid choice")
        continue
    elif operation ==5 :
        print("Exiting the program")
        break
    #prompts user to enter two numbers
    num1 = int(input("First number:"))
    num2 = int(input("Second number: "))

     #logic of the program to carry out the operation as per users choosing
    if operation == 1:
        print(num1 + num2)
    elif operation == 2:
        print(num1 - num2)
    elif operation == 3:
        print(num1 * num2)
    elif operation == 4:
        print(str(floor(num1 / num2)) +" reminder: "+str(num1%num2))

   