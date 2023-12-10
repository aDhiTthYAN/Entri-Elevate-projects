""""""
import json

def delete_account(account_number):

    with open('accounts.json', 'r') as file:
        accounts_data = json.load(file)


    if account_number in accounts_data:
        del accounts_data[account_number]
        print(f"Account {account_number} deleted successfully.")
    else:
        print(f"Account {account_number} not found.")


    with open('accounts.json', 'w') as file:
        json.dump(accounts_data, file, indent=2)

delete_account("17580")

