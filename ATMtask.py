def displayMenu():
    print()
    print("Menu")
    print("1.Withdraw")
    print("2.Deposite")
    print("3.Check balance")
    print("4.Change Pin")
    print("Exit")
    
def withdraw():
    global pin1,balance
    while True:
        print()
        user_pin=input("Enter your pin : ")
        if user_pin == pin1:
            while True:
                amount= int(input("Enter amount to withdraw : "))
                if amount > balance:
                    print("Insufficient Balance ! balance : ",balance)
                else:
                    balance -= amount
                    print("Withdraw Succesful ! Balance : ",balance)
                    break
            else:
                print("Invalid pin")
            break

def deposite():
    global balance
    
    while True:
        user_pin=input("Enter your Pin : ")
        if user_pin == pin1:
            amount=int(input("Enter amount to deposite : "))
            balance += amount
            print("Deposite Successful ! Balance : ", balance)
            break
        else:
            print("Invalid Pin")

def CheckBalance():
    while True:
        user_pin=input("Enter your pin : ")
        if user_pin==pin1:
            print("Your Balance :",balance)
        else:
            print("Invalid Pin")
            
def ChangePin():
    global pin1
    while True:
        user_pin=input("Enter Your current Pin : ")
        if user_pin == pin1:
            new_pin=input("Enter Your new Pin : ")
            pin1=new_pin
            print("Pin changed :",new_pin)
        else:
            print("Invalid pin")
        break
  
        
def main():
    while True:
        displayMenu()
        ch = int(input("Enter choice : "))
        if ch == 1:
            withdraw()
        elif ch == 2:
            deposite()
        elif ch == 3:
            CheckBalance()
        elif ch == 4:
            ChangePin()
        elif ch == 5:
            break
        else:
            print("Wrong Input")
        print("Thank you")
            
    
    
print("----------ATM----------")
name = input("Enter name : ")
balance=int(input("Set balance : "))
while True:
    print()
    pin1=input("Enter Pin : ")
    pin2=input("Confirm pin : ")
    if pin1 == pin2:
        print("Pin set successful ")
        break
    else:
        print("Password Not Matching ")
        
main()