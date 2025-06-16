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

client_acc_no = []
client_name = []
client_ph_num = []
client_address = []
balance = []
acc_num = 1000
client_initial_amt = 0

def gen_acc_no(val):
    global acc_num
    acc_num += 1
    val = acc_num
    client_acc_no.append(val)
    return val

def acc_creation():
    print("\t<< HERE YOUR ACCOUNT CREATION >>")
    global client_name,client_ph_num,client_address,client_initial_amt,balance
    cus_name = input("Enter your Full Name Here: ")
    client_name.append(cus_name)
    cus_ph_num = int(input("Enter your Phone Number Here: "))
    client_ph_num.append(cus_ph_num)
    cus_address = input("Enter your Address here: ")
    client_address.append(cus_address)
    while True:
        client_initial_amt = float(input("Enter Your Deposit Initial Amount 500 only: "))
        if client_initial_amt != 500:
            print("Please Enter as per required Amount")
            print("Try again..!!")
        else:
            balance.append(client_initial_amt)
            break
    print("\tAccount Created SuccessFully")
    put_acc_num = gen_acc_no(acc_num)
    print("\tYour Account number is: ",put_acc_num)


def acc_Detail_Display():
    print("\t<< HERE DISPLAY ALL ACCOUNTS >>")
    print("Account_No", end="\t")
    print("Acc_Holder_Name", end="\t\t")
    print("Balance")
    for i in range(len(client_acc_no)):
        print(client_acc_no[i], end="\t\t")
        print(client_name[i], end="\t\t\t")
        print(balance[i])


def acc_check_balance():
    print("\t<< CHECK BALANCE >>")
    account_num = int(input("Enter your ACCOUNT Number: "))
    for get in range(len(client_acc_no)):
        if client_acc_no[get] == account_num:
            print("Your Current Balance is ₹",balance[get])
            print("Account Holder Name:",client_name[get])
            break
    else:
        print("invalid Account number Try again..!!")

def acc_deposit():
    account_num = int(input("Enter Your Account Number: "))
    while True:
        dep_amt = float(input("Enter your Deposit Amount here: "))
        if dep_amt < 0:
            print("Invalid amount Try again")
        else:
            break

    for get in range(len(client_acc_no)):
        if client_acc_no[get] == account_num:
            balance[get]+= dep_amt
            print("Amount ₹",dep_amt,"has been Deposited Successfully")
            print("Your current Balance is ₹",balance[get])
            break
    else:
        print("InCorrect Account number Please Try again..!!")
def acc_withdraw():
    account_num = int(input("Enter Your Account Number: "))
    wit_amt = float(input("Enter Your Withdraw Amount: "))
    for get in range(len(client_acc_no)):
        if client_acc_no[get] == account_num:
            if balance[get] >= wit_amt:
                balance[get] -= wit_amt
                print("Amount ₹",wit_amt,"has been Withdraw Successfully")
                print("Your Current Balance is ₹",balance[get])
            else:
                print("Insufficient Balance ")
            break
    else:
        print("InCorrect Account number Please Try again..!!")

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