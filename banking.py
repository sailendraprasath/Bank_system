def greetings():
    print("\tWelcome to Indra Bank of India")
    print("Here below have options to access our bank system...!!")
    print("\t1) Account Creation")
    print("\t2) Display All Account Details Display")
    print("\t3) Check Balance")
    print("\t4) Deposit Amount")
    print("\t5) Withdraw Amount")
    print("\t6) EXIT")

def ask_client():
    ask = input("Do you want to continue (Yes/No): ")
    if ask == "yes" or ask == "YES":
        print("")
    elif ask == "no" or ask == "NO":
        print("Thanks For your Time with us")
        exit()
    else:
        print("Plzz Enter Your words should be yes OR no")
        ask_client()
data = []
acc_no = 1001
client_name = ""
client_ph_num = 0
client_email = ""
client_address = ""
client_pan_num = ""
acc_type = 0
client_initial_amt = 0
balance = 0

def acc_creation():
    print("\t<< HERE YOUR ACCOUNT CREATION >>")
    global client_name,client_ph_num,client_email,client_address,client_pan_num,acc_type,client_initial_amt,balance
    client_name = input("Enter your Full Name Here: ")
    client_ph_num = int(input("Enter your Phone Number Here: "))
    client_email = input("Enter Your Email here: ")
    client_address = input("Enter your Address here: ")
    client_pan_num = input("Enter Your PAN Card Code here: ")
    print("Account Type Option")
    print("\t1) Savings Account")
    print("\t2) Current Account")
    while True:
        acc_type = int(input("Enter Your Option here: "))
        if acc_type == 1:
            print("Accepted Savings Account")
            break
        elif acc_type == 2:
            print("Accepted Current Account")
            break
        else:
            print("Option Should be 1 or 2 Accept here")
            print("\tPlease Try Again..!!")
    while True:
        client_initial_amt = float(input("Enter Your Deposit Initial Amount 500 only: "))
        if client_initial_amt >=501  or client_initial_amt <= 0:
            print("Please Enter as per required Amount")
            print("Try again..!!")
        else:
            balance += client_initial_amt
            break
    print("\tAccount Created SuccessFully")
    print("\tYour Account number is: ",acc_no)


def acc_Detail_Display():
    if client_name == "":
        print("\t<< UNAVAILABLE NOW >>")
        print("Currently you dont have a account")
        print("First enter yes to continue press 1 to Create a Account")
    else:
        while True:
            acc_num = int(input("Enter your Account number here: "))
            if acc_num == 1001:
                break
            else:
                print("\t<< UNAVAILABLE NOW >>")
                print("Please Enter correct Account number")
                print("Try again..!!")
        print("\t<< DISPLAY ACCOUNT DETAIL >>")
        print("Name", end="\t\t")
        print("AccountNo", end="\t\t")
        print("Balance")
        print(client_name, end="\t\t ")
        print(acc_no, end="\t\t\t ")
        print(balance)


def acc_check_balance():
    if client_name == "":
        print("\t<< UNAVAILABLE NOW >>")
        print("Currently you dont have a account")
        print("First enter yes to continue press 1 to Create a Account")
    else:
        print("\t<< HERE YOUR BALANCE AMOUNT >>")
        while True:
            acc_num = int(input("Enter your Account number here: "))
            if acc_num == 1001:
                break
            else:
                print("\t<< UNAVAILABLE NOW >>")
                print("Please Enter correct Account number")
                print("Try again..!!")
        print("Account Holder name: ", client_name)
        print("Account number:", acc_no)
        print("Account holder Address:", client_address)
        print("You have ₹", balance, "amount in your Account")

def acc_deposit():
    if client_name == "":
        print("\t<< UNAVAILABLE NOW >>")
        print("Currently you dont have a account")
        print("First enter yes to continue press 1 to Create a Account")
    else:
        while True:
            acc_num = int(input("Enter your Account number here: "))
            if acc_num == 1001:
                global balance
                print("\t<< HERE YOU DEPOSIT YOUR AMOUNT >>")
                dep_amt = float(input("Enter your Deposit amount here: "))
                balance += dep_amt
                print("Your deposit Amount is:",dep_amt)
                print("You have ₹", balance, "amount in your Account")
                break
            else:
                print("\t<< UNAVAILABLE NOW >>")
                print("\tPlease Enter correct Account number")
                print("\tTry again..!!")


def acc_withdraw():
    if client_name == "":
        print("\t<< UNAVAILABLE NOW >>")
        print("Currently you dont have a account")
        print("First enter yes to continue press 1 to Create a Account")
    else:
        while True:
            acc_num = int(input("Enter your Account number here: "))
            if acc_num == 1001:
                global balance
                print("\t<< HERE YOU WITHDRAW YOUR AMOUNT >>")
                while True:
                    wit_amt = float(input("Enter your Withdraw amount here: "))
                    if wit_amt > balance or wit_amt == 0 or wit_amt <= 0:
                        print("check your enter number")
                        print("Try Again..!!")
                    else: #wit_amt <= balance
                        balance-=wit_amt
                        print("You Withdraw Amount:",wit_amt)
                        print("You have ₹", balance, "amount in your Account")
                        break
                break
            else:
                print("\t<< UNAVAILABLE NOW >>")
                print("\tPlease Enter correct Account number")
                print("\tTry again..!!")


while True:
    greetings()
    opt = int(input("Enter Your Option here: "))
    match opt:
        case 1:
            acc_creation()
        case 2:
            acc_Detail_Display()
        case 3:
            acc_check_balance()
        case 4:
            acc_deposit()
        case 5:
            acc_withdraw()
        case 6:
            print("Thanks for using our Software")
            break
        case _:
            print("Invalid Option Try again")
    ask_client()