#program for withdrawing money from atm

print("""
*****************************
          WELCOME
*****************************

MONNEY TRANSACTİONS:
---------------------
1 --> BALANCE INQUIRY
2 --> DEPOSİT MONEY
3 --> WITHDRAW MONEY
---------------------
To exit the program, press 'q'."
""")

balance = 100000

while True:
    op = input("Please select a money transaction: ")

    if op == "q":
        print("Exiting the Program...\nHave a good day!")
        break;
    elif op == "1":
        print("Your Balance :",balance)
    elif op == "2":
        depo_money = int(input("Enter the amount you want to deposit: "))
        balance += depo_money
        print("Your money has been deposited\n")
    elif op == "3":
        while True:
            withdraw_money = int(input("Enter the amount you want to withdraw: "))
            if withdraw_money > balance:
                print("!Invalid Amount! Please try again")
            else: 
                balance -= withdraw_money
                print("Your money has been withdrawn\n")
                break;