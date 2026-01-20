account1_owner = "Dwayne Johnson"
account1_number = 1001
account1_balance = 2500.75


account2_owner = "Will Smith"
account2_number = 1002
account2_balance = 1800.00


account3_owner = "Martin Lawrence"
account3_number = 1003
account3_balance = 320.40


while True:
    print("\nSimple Banking System") 
    print("1. Create an Account") 
    print("2. Deposit Money") 
    print("3. Withdraw Money") 
    print("4. View Account Details") 
    print("5. Exit")

    choice = input("Enter your choice (1–5): ")

    if choice == "1": 
        print("You chose to create an account.")
        
    elif choice == "2": 
        print("You chose to deposit money.")

    elif choice == "3": 
        print("You chose to withdraw money.")

    elif choice == "4": 
        print("You chose to view account details.")

    elif choice == "5": 
        print("Exiting the system. Goodbye!") 
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")


    def create_account(): 
        global account1_owner, account1_number 
        global account2_owner, account2_number 
        global account3_owner, account3_number

        owner = input("Enter account owner's name: ")
        account_number = int(input("Enter account number: "))

        if account_number in [account1_number, account2_number, account3_number]:
            print("Error! Account number already exists.")
            return
        
        if account1_owner is None: 
            account1_owner = owner 
            account1_number = account_number
            print("Success! Account created successfully in slot 1.")

        elif account2_owner is None: 
            account2_owner = owner 
            account2_number = account_number
            print("Success!Account created successfully in slot 2.")

        elif account3_owner is None: 
            account3_owner = owner 
            account3_number = account_number
            print("Success!Account created successfully in slot 3.")

        else: 
            print("Error!Cannot create more than 3 accounts.")


def deposit_money():
    global account1_balance, account2_balance, account3_balance 
    global account1_number, account2_number, account3_number

    account_number = int(input("Enter account number: ")) 
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0: 
        print("Deposit amount must be greater than zero.") 
        return
    
    if account_number == account1_number: 
        account1_balance += amount
        print(f"${amount} deposited successfully into Account 1.")

    elif account_number == account2_number: 
        account2_balance += amount
        print(f"${amount} deposited successfully into Account 2.")

    elif account_number == account3_number: 
        account3_balance += amount
        print(f"${amount} deposited successfully into Account 3.")

    else: 
        print("Account not found.")


def withdraw_money():
    global account1_balance, account2_balance, account3_balance
    global account1_number, account2_number, account3_number

    account_number = int(input("Enter account number: "))
    amount = float(input("Enter amount to withdraw: "))

    if account_number == account1_number:
        if 0 < amount <= account1_balance:
            account1_balance -= amount
            print(f"${amount} withdrawn successfully from Account 1.")

        elif amount > account1_balance: 
            print("Insufficient balance.")

        else: 
            print("Invalid withdrawal amount.")
    elif account_number == account2_number:
        if 0 < amount <= account2_balance:
            account2_balance -= amount 
            print(f"${amount} withdrawn successfully from Account 2.")
        elif amount > account2_balance: 
            print("Insufficient balance.")
        else: 
            print("Invalid withdrawal amount.")
        
    elif account_number == account3_number:
        if 0 < amount <= account3_balance: 
            account3_balance -= amount 
            print(f"${amount} withdrawn successfully from Account 3.")
        elif amount > account3_balance: 
            print("Insufficient balance.")
        else: 
            print("Invalid withdrawal amount.")
    else:
        print("Account not found.")


def view_account_details(): 
    global account1_owner, account1_number, account1_balance 
    global account2_owner, account2_number, account2_balance 
    global account3_owner, account3_number, account3_balance

    account_number = int(input("Enter account number: "))

    if account_number == account1_number: 
        print(f"Account Owner: {account1_owner}") 
        print(f"Account Number: {account1_number}") 
        print(f"Account Balance: ${account1_balance:.2f}")

    elif account_number == account2_number: 
        print(f"Account Owner: {account2_owner}") 
        print(f"Account Number: {account2_number}") 
        print(f"Account Balance: ${account2_balance:.2f}")

    elif account_number == account3_number: 
        print(f"Account Owner: {account3_owner}") 
        print(f"Account Number: {account3_number}") 
        print(f"Account Balance: ${account3_balance:.2f}")
    else: 
        print("Account not found.")

    
    def exit_system(): 
        print("Exiting the system. Goodbye!")

    def invalid_choice(): 
        print("Invalid choice. Please enter a number from 1 to 5.")


    while True: 
        print("\nSimple Banking System") 
        print("1. Create an Account") 
        print("2. Deposit Money") 
        print("3. Withdraw Money") 
        print("4. View Account Details") 
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1": 
            create_account()
        elif choice == "2": 
            deposit_money()
        elif choice == "3": 
            withdraw_money()
        elif choice == "4": 
            view_account_details()
        elif choice == "5": 
            print("Exiting the system. Goodbye!") 
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

         
                  
        

      
    
   
   
    

    
        



   



    
