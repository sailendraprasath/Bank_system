data =[]
def greetings():
    print("\tWelcome to Indra Bank of India")
    print("Here below have options to access our bank system...!!")
    print("\t1) Account Creation")
    print("\t2) Display All Account Details Display")
    print("\t3) Check Balance")
    print("\t4) Deposit Amount")
    print("\t5) Withdraw Amount")
    print("\t6) EXIT")
def acc_creation():
    client_name = input("Enter Your Full Name here: ")
    client_ph_num = int(input("Enter your Phone number here: "))
    client_email = input("Enter your Email here: ")
    client_address = input("Enter your Address here: ")
    print("\tAccount Type Option number given below")
    print("\t\t1) Savings Type")
    print("\t\t2) Current Type")
    acc_type = int(input("Enter your Option here: "))
    if acc_type == 1:
        print("Saving Account")
    elif acc_type == 2:
        print("Current Account")
    else:
        print("<<...Invalid option you Should provide given option...>>")
    client_pan_num = input("Enter your PAN Card Code here: ")
    client_initial_amt = float(input("Enter your Initial Amount Deposit 500: "))

    print("<<...Your Account has been Created Successfully...>>")
def acc_Detail_Display():
    print("All Account Detail Show Here")
def acc_check_balance():
    client_acc_num = int(input("Enter your Account Number here: "))
    print("Current balance")
def acc_deposit():
    acc_num = int(input("Enter your Account number here: "))
    deposit = float(input("Enter Your Deposit Amount here: "))
    print("Display balance amt")
def acc_withdraw():
    acc_num = int(input("Enter your Account Number here: "))
    withdraw = float(input("Enter your Withdraw Amount here: "))

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
            