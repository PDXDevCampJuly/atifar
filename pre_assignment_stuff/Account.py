""" An account file for our Simple bank.
"""

import itertools

class Account:
    """An Account class that stores account info."""

    def __init__(self, balance, account_type="checking"):
        self.balance = balance
        self.account_type = account_type


    def deposit(self, money):
        self.balance += money


    def withdraw(self, money):
        if self.balance < money:
            print("Withdrawal failed due to insufficient funds. Your current balance is ", end="")
            self.print_balance()
        else:
            self.balance -= money


    def check_balance(self):
        return self.balance


    def print_balance(self):
        readable_balance = '${:,.2f}'.format(self.balance)
        print(readable_balance)


    def deposit_earned_interest(self, percentage):
        def truncate(amount, decimals):
            return int(amount * 10**decimals) / 10**decimals

        increase = truncate(self.balance * percentage/100, 2)
        self.balance += increase


class Person:
    """A class that tracks Persons in our bank."""

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.accounts = {}


    def open_account(self, initial_balance, account_name, account_type="checking"):
        self.accounts[account_name] = Account(initial_balance, account_type)


    def close_account(self, account_name):
        del self.accounts[account_name]


    def deposit(self, money, account_name):
        self.accounts[account_name].deposit(money)


    def withdraw(self, money, account_name):
        self.accounts[account_name].withdraw(money)


    def show_accounts(self):
        """ Display on the screen all of a user's account info."""
        for account_name, account in self.accounts.items():
            print("_____________________________")
            print("Account name: {}\nAccount type: {}\nBalance: ${}".format(
                account_name, account.account_type, account.balance))
        print("_____________________________")


class Bank:
    """A simple Bank class."""
    def __init__(self):
        self.customers = {}
        self.savings_interest_rate = 2.15   # percent


    def new_customer(self, first_name, last_name, email):
        self.customers[email] = Person(first_name, last_name, email)


    def remove_customer(self, email):
        del self.customers[email]


    def show_customer_info(self, email):
        cust = self.customers[email]
        print()
        print("Name: {} {}\nEmail: {}".format(cust.first_name, cust.last_name, cust.email))
        cust.show_accounts()


    def is_existing_customer(self, email):
        """ Returns True if the customer, associated with 'email', exists, otherwise return False."""
        return email in self.customers


    def is_existing_account(self, email, account_name):
        """ Returns True if the customer, associated with 'email', has 'account_name',
        otherwise return False.
        """
        if self.is_existing_customer(self, email):
            return account_name in self.customers[email].accounts
        else:
            return False


    def customer_deposit(self, email, money, account_name):
        if self.is_existing_account(email, account_name):
            self.customers[email].deposit(money, account_name)
        else:
            print("Deposit can't be processed. '{}' account associated with '{}' not found.".format(
                account_name, email))


    def customer_withdrawal(self, email, money, account_name):
        if self.is_existing_account(email, account_name):
            self.customers[email].withdraw(money, account_name)
        else:
            print("Withdrawal can't be processed. '{}' account associated with '{}' not found.".format(
                account_name, email))


    def make_customer_account(self, initial_balance, email, account_name, account_type="checking"):
        if self.is_existing_customer(self, email):
            self.customers[email].open_account(initial_balance, account_name, account_type)
        else:
            print("New account can't be created. Customer associated with '{}' not found.".format(
                email))


    def remove_customer_account(self, email, account_name):
        if self.is_existing_account(self, email, account_name):
            self.customers[email].close_account(account_name)
        else:
            print("Account can't be removed. '{}' account associated with '{}' not found.".format(
                account_name, email))


    def show_customer_worth(self, email):
        """ Display on the screen a user's total holdings at the bank."""
        if self.is_existing_customer(self, email):
            total_deposits = sum([account.balance for account in self.customers[email].accounts.values()])
            print("Customer associated with '{}' has ${:,.2f} total deposits in the bank.".format(
                email, total_deposits))
        else:
            print("Customer associated with '{}' not found.".format(email))


    def monthly_interest_give(self, interest_rate_percent):
        """ Deposit earned interes into the savings accounts of all customers."""
        for customer in self.customers.values():
            for account in customer.accounts.values():
                if account.account_type == "savings":
                    account.deposit_earned_interest(interest_rate_percent)


    def main(self):
        """ Present to user a menu of account operations in this bank. Perform operations."""
        pass

# new_customers: [(<first_name>, <last_name>, <email>, <initial_balance>), ...]
new_customers = [
    ("Bugs", "Bunny", "bugs.bunny@go.com", 67),
    ("Jane", "Doe", "janey@abc.com", 960),
    ("Lucky", "Ducky", "ducky@quack.com", 8)
]

def show_all_customers(bank):
    # Show all customers in the bank
    print("The bank has the following customers:")
    for customer in bank.customers:
        bank.show_customer_info(customer)
    print()


def test_new_customer():
    bank = Bank()
    # Fetch a test customer's info
    cust = new_customers[0]
    print("Add new customer '{} {}' with email '{}'.".format(
        cust[0], cust[1], cust[2]))
    # Create new customer
    bank.new_customer(cust[0], cust[1], cust[2])
    show_all_customers(bank)
    # Fetch another test customer's info
    cust = new_customers[1]
    print("Add new customer '{} {}' with email '{}'.".format(
        cust[0], cust[1], cust[2]))
    # Create new customer
    bank.new_customer(cust[0], cust[1], cust[2])
    # Show all customers in the bank
    print("The bank has the following customers:")
    for customer in bank.customers:
        bank.show_customer_info(customer)
    print()


def add_test_customers(bank):
    for cust in new_customers:
        bank.new_customer(cust[0], cust[1], cust[2])


def test_remove_customer():
    bank = Bank()
    add_test_customers(bank)


test_new_customer()


# def test_person(self):
#     man = Person("Lucky", "Ducky", "ducky@deet.net")
#     print("Name: '{} {}'. Email: '{}'".format(man.first_name, man.last_name, man.email))
#     account_type = "savings"
#     account_name = "Slush Fund"
#     balance = 146
#     print("Open a '{}' account '{}' for '{} {}' with ${} initial balance.".format(
#         account_type, account_name, man.first_name, man.last_name, balance))
#     man.open_account(balance, account_name, account_type)
#     man.show_accounts()
#     account_type = "checking"
#     account_name = "College Fund"
#     balance = 500
#     print("Open a '{}' account '{}' for '{} {}' with ${} initial balance.".format(
#         account_type, account_name, man.first_name, man.last_name, balance))
#     man.open_account(balance, account_name, account_type)
#     man.show_accounts()
#     account_name = "Slush Fund"
#     print("Close the '{}' account for '{} {}'.".format(
#         account_name, man.first_name, man.last_name))
#     man.close_account(account_name)
#     man.show_accounts()


# def test_account(self):
#     acct = Account(300.67, "Genghis Khan")
#     acct.print_balance()
#     deposit = 20.81
#     print("depositing:", deposit)
#     acct.deposit(deposit)
#     acct.print_balance()
#     withdraw = 670
#     print("withdrawing:", withdraw)
#     acct.withdraw(withdraw)
#     acct.print_balance()
#     withdraw = 65.9
#     print("withdrawing:", withdraw)
#     acct.withdraw(withdraw)
#     acct.print_balance()
#     interest = 0.52
#     print("accruing interest at rate:", interest, "%")
#     acct.deposit_earned_interest(interest)
#     acct.print_balance()

