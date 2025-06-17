def greetings():
    star_Design()
    print("\tWelcome to Indra Bank of India")
    star_Design()
    print("Here below have options to access our bank system...!!")
    print("\t1) Account Creation")
    print("\t2) Display All Account Details Display")
    print("\t3) Check Balance")
    print("\t4) Deposit Amount")
    print("\t5) Withdraw Amount")
    print("\t6) EXIT")
def star_Design():
    print("* "*25)
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
    star_Design()
    print("\t<< HERE YOUR ACCOUNT CREATION >>")
    star_Design()
    global client_name,client_ph_num,client_address,client_initial_amt,balance
    cus_name = input("Enter your Full Name Here: ")
    client_name.append(cus_name)
    cus_ph_num = int(input("Enter your Phone Number Here: "))
    client_ph_num.append(cus_ph_num)
    cus_address = input("Enter your Address here: ")
    client_address.append(cus_address)
    for i in range(3):
        client_initial_amt = float(input("Enter Your Deposit Initial Amount 500 only: "))
        if 500 > client_initial_amt >= 0:
            star_Design()
            print("\tPlease Enter as per required Amount")
            print("\tTry again..!!")
            star_Design()
        elif client_initial_amt < 0:
            star_Design()
            print("Dont Enter Negative number")
            star_Design()
        else:
            balance.append(client_initial_amt)
            star_Design()
            print("\tAccount Created SuccessFully")
            put_acc_num = gen_acc_no(acc_num)
            print("\tYour Account number is: ",put_acc_num)
            star_Design()
            break
    else:
        star_Design()
        print("\tYou have Reached Maximum Attempt")
        print("\ttry Again Later..!!")
        star_Design()

def acc_Detail_Display():
    if acc_num > 1000:
        star_Design()
        print("\t<< HERE DISPLAY ALL ACCOUNTS >>")
        star_Design()
        print()
        star_Design()
        print("Account_No", end="\t")
        print("Acc_Holder_Name", end="\t\t")
        print("Balance")
        for i in range(len(client_acc_no)):
            print(client_acc_no[i], end="\t\t")
            print(client_name[i], end="\t\t\t")
            print(balance[i])
        star_Design()
    else:
        star_Design()
        print("\t<< YOU DONT HAVE A ACCOUNT YET >>")
        print("you should create Account")
        print("Continue To type yes Then Enter option 1 to Create Account")
        star_Design()


def acc_check_balance():
    if acc_num > 1000:
        star_Design()
        print("\t<< CHECK BALANCE >>")
        star_Design()
        count1 = 0
        while count1 < 3:
            account_num = int(input("Enter your ACCOUNT Number: "))
            if account_num < 0:
                star_Design()
                print("Negative number not allowed.")
                star_Design()
            for i in range(len(client_acc_no)):
                if client_acc_no[i] == account_num:
                    star_Design()
                    print("Account Holder Name:", client_name[i])
                    print("Your Current Balance is ₹", balance[i])
                    star_Design()
                    return
            star_Design()
            print("\tIncorrect Account Number. Try again..")
            star_Design()
            count1 += 1
        star_Design()
        print("You have Reached Maximum Attempt!!")
        print("Try Again Later!!")
        star_Design()
    else:
        star_Design()
        print("\t<< YOU DON'T HAVE AN ACCOUNT YET >>")
        print("Please create an account (Option 1).")
        star_Design()


def acc_deposit():
    if acc_num > 1000:
        star_Design()
        print("\t<< DEPOSIT AMOUNT HERE >>")
        star_Design()
        count3 = 0
        while count3 < 3:
            account_num = int(input("Enter Your Account Number: "))
            if account_num < 0:
                star_Design()
                print("\tNegative number not Allowed")
                star_Design()
            for i in range(len(client_acc_no)):
                if client_acc_no[i] == account_num:
                    print("Your current Balance is ₹", balance[i])
                    while True:
                        dep_amt = float(input("Enter your Deposit Amount here: "))
                        if dep_amt < 0:
                            star_Design()
                            print("\tNegative amount not allowed.")
                            star_Design()
                        else:
                            break
                    balance[i] += dep_amt
                    star_Design()
                    print("Amount ₹", dep_amt, "has been Deposited Successfully")
                    print("Your current Balance is ₹", balance[i])
                    star_Design()
                    return
            star_Design()
            print("\tIncorrect Account Number. Try again.")
            star_Design()
            count3 += 1
        star_Design()
        print("\tYou have Reached Maximum Attempts!!")
        print("\tTry Again Later!!")
        star_Design()
    else:
        star_Design()
        print("\t<< YOU DON'T HAVE AN ACCOUNT YET >>")
        print("You should create an account first (Option 1).")
        star_Design()


def acc_withdraw():
    if acc_num > 1000:
        star_Design()
        print("\t<< WITHDRAW AMOUNT HERE >>")
        star_Design()
        count4 = 0
        while count4 < 3:
            account_num = int(input("Enter Your Account Number: "))
            if account_num < 0:
                star_Design()
                print("Negative Number not allowed..!!")
                star_Design()
            for i in range(len(client_acc_no)):
                if client_acc_no[i] == account_num:
                    print("Your Current Balance is ₹", balance[i])
                    wit_amt = float(input("Enter Your Withdraw Amount: "))
                    if wit_amt < 0:
                        print("Negative amount not allowed.")
                        return
                    if balance[i] >= wit_amt:
                        balance[i] -= wit_amt
                        star_Design()
                        print("Amount ₹",wit_amt,"has been Withdrawn Successfully")
                        print("Your Current Balance is ₹", balance[i])
                        star_Design()
                        return
                    else:
                        star_Design()
                        print("\tInsufficient Balance.")
                        star_Design()
                        return
            star_Design()
            print("\tIncorrect Account Number. Try again.")
            star_Design()
            count4 += 1
        star_Design()
        print("You have Reached Maximum Attempt!!")
        print("Try Again Later!!")
        star_Design()
    else:
        star_Design()
        print("\t<< YOU DONT HAVE A ACCOUNT YET >>")
        print("Continue To type yes Then Enter option 1 to Create Account")
        star_Design()

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