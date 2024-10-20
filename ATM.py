import os
print("Welcome!!")
print("Main menue :")
print("1.Register New Card")
print("2.Charge Your Phone")
print("3.Account Balance")
print("4.Pay To Other Card")
print("5.Exit...")
password=1234
user=int(input('Enter your paasword:'))
while True:
    if user==password:
        khadamat=int(input("Which One:"))
        if khadamat==1:
            print("Card Collected")
        elif khadamat==2:
            print("Your Phone Charged")
        elif khadamat==3:
            print("$512,000,000,000 Youre Balance")
        elif khadamat==4:
            maghsad=int(input("Destination Card Number:"))
            if maghsad==6037:
                print("You Succeed!")
            else:
                print("False...! please Enter Correct Destination Card Number")
        elif khadamat==5:
            break
    else:
        print("Password isnt Correct & Try Again!!!")
        break
