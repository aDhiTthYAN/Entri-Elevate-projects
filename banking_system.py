import random
import re
import json



class Bank:
    def __init__(self):
        self.load_accounts()

    def load_accounts(self):
        try:
            with open('accounts.json', 'r') as file:
                self.accounts = json.load(file)

        except FileNotFoundError:
            self.accounts={}
    def save_accounts(self):
        with open('accounts.json','w') as file:
            json.dump(self.accounts,file,indent=2)




    def account_creation(self):
        name=str(input("enter your name: "))
        if not re.match('^[a-zA-z\s]+$',name):
            print("Enter a valid name!")
            return None

        mobile_number = str(input("enter your mobile number: "))
        if not re.match('^\d{10}$', mobile_number):
            print("invalid mobile number")
            return None

        pancard =input("enter your pancard number: ").upper()
        if pancard in[account_data.get('pancard','').upper()  for account_data in self.accounts.values()]:
            print("Invalid pancard number! Pancard number must be unique.")
            return None


        if not re.match('^[A-Z]{5}[0-9]{4}[A-Z]$', pancard):
               print("invalid pancard number!!")
               return None

        pin = input("Enter your  Four Digit PIN: ")
        if len(pin) > 4:
            print("Invalid pin!!!Enter a PIN of size 4!")
            return None

        balance=0
        account_number = self.generate_account_number()
        print(f"your account number is {account_number}")
        new_account = BankAccount(account_number, pin, balance,name, accounts=self.accounts)
        self.accounts[account_number] = {"pin": pin,"pancard":pancard,"name":name, "balance":balance}
        return new_account
    def generate_account_number(self):
        while True:
            account_number = ''.join(str(random.randint(0, 9)) for i in range(5))
            if account_number not in self.accounts:
                return account_number

class BankAccount:
    def __init__(self, account_number, pin, balance,name, accounts):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.name= name
        self.accounts = accounts

    def login(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            print(f"Hello {self.accounts[account_number].get('name') }  welcome")
            return True
        else:
            print("Login failed!! invalid Account number or PIN")
            return False

    def deposit(self, amount):
        if self.account_number in self.accounts:
            current_balance = self.accounts[self.account_number]["balance"]
            new_balance = current_balance + amount
            self.accounts[self.account_number]["balance"] = new_balance
            print(f"Balance {new_balance}")
        else:
            print("Invalid account number or pin")

    def withdrawal(self,  amount):
        if self.account_number in self.accounts:
            current_balance = self.accounts[self.account_number]["balance"]
            if current_balance >= amount:
                new_balance = current_balance - amount
                self.accounts[self.account_number]["balance"] = new_balance
                print(f"Balance: {new_balance}")
            else:
                print("Insufficient balance")
        else:
            print("Invalid account number or pin")

Bank = Bank()
print("Welcome to SIB BANKING SYSTEM")
print("Enter C for The creation Of A New Account")
print("Enter L for Login")
print("Enter B for Checking Bank Balance ")
print("Enter N of Changing Password")
option = input("Enter your option:\t ")

if option.upper() == "C":
    New_account=Bank.account_creation()
    if New_account:
        print("Account Created Successfully")
        Bank.save_accounts()

elif option.upper() == "N":
    account_number = input("Enter The Account Number:\t")
    if account_number in Bank.accounts:
        new_pin = input("Enter The New PIN:\t")
        if len(new_pin) > 4:
            print("Invalid pin!!! Enter a PIN of size 4!")
        else:
            Bank.accounts[account_number]["pin"] = new_pin
            Bank.save_accounts()
            print("PIN changed successfully!")
    else:
        print("Invalid account number.")




elif option.upper() =="B":
    account_number = input("\nEnter your account number:\t ")
    pin = input("Enter your PIN:\t ")

    user_account = BankAccount(account_number, pin, 0, "", accounts=Bank.accounts)

    if user_account.login(account_number,pin):
        print(f"hi {user_account.accounts[account_number].get('name')}  your balance is {user_account.accounts[account_number].get('balance')} RS")


elif option.upper() == "L":
    account_number = input("\nEnter your Account Number:\t")
    pin = input("Enter Your PIN:\t ")


    user_account = BankAccount(account_number, pin, 0,"", accounts=Bank.accounts)


    if user_account.login(account_number, pin):
        print("Enter 1 for Deposit")
        print("Enter 2 for Withdrawal")

        option = int(input("\nEnter your option:\t "))

        if option == 1:
            deposit_amount = float(input("\nEnter your Deposit Amount:\t "))
            user_account.deposit(deposit_amount)
            Bank.save_accounts()
        elif option == 2:
            withdrawal_amount = float(input("\nEnter your Withdrawal Amount:\t "))
            user_account.withdrawal(withdrawal_amount)
            Bank.save_accounts()
        else:
            print("Invalid option")
else:
    print("Invalid option")





