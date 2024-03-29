import sys
class depositeError(Exception):
    pass
class withdrawError(Exception):
    pass
class insuffbalError(Exception):
    pass
print("*****Wlcome to ICICI Bank *****")
print("Insert your card\n")

pin=12345
balance=5000

def deposite():
    amount=0
    global balance
    if amount< 0 :
        raise depositeError
    else:
        print("Deposite Information")
        amount=int(input("Enter anount to deposite : "))
        balance = amount + balance
        print("Amount Deposited ",amount)
        print("Total balance : ",balance)
         
        
def withdraw():
    amount=int(input("Enter amount to withdraw : "))
    global balance
    if amount <= 0:
        raise withdrawError
    elif (amount + 5000) > balance:
        raise insuffbalError
    else:
        if balance >= amount:
            balance = balance-amount
            print("Total Balance : ",balance)

def check_balance():
    print("Your Current Balance : ",balance)
    
def close():
    sys.exit()
    
pincode=int(input("Enter Your 5 digit code : "))
if pincode == pin:
    print("Yes.....you Successfuly entered")  
    while True:
        try:
            print("\nATM operation")
            print("\n1.Deposite \n2.Withdraw \n3.Check Balance \n4.Exit")
            ch=int(input("Enter Your choice : "))
            if ch == 1:
                print(" -----Deposite-----")
                try:
                    deposite()
                except ValueError:
                    print("Please Enter only Numeric Values")
                except depositeError:
                    print("Negative amount not allowed")
            elif ch == 2:
                print("-----Withdraw-----")
                try:
                    withdraw()
                except ValueError:
                    print("Please Enter only Numeric Values")
                except depositeError:
                    print("Negative amount not allowed")
                except insuffbalError:
                    print("Insufficient Balance")
            elif ch == 3:
                print("-----CheckBalance------")
                try:
                    check_balance()
                except ValueError:
                    print("Please Enter only Numeric Values")
                except depositeError:
                    print("Negative amount not allowed")
            else:
                exit()
        except:
            print("Special Character and symbol not allowed")