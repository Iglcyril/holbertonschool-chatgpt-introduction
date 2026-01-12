#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance inquiries.
    """
    
    def __init__(self):
        """Initialize the checkbook with a balance of 0.0"""
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit money into the checkbook.
        
        Parameters:
        amount (float): The amount to deposit. Must be positive.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the checkbook.
        
        Parameters:
        amount (float): The amount to withdraw. Must be positive and not exceed balance.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Main function to run the checkbook program."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            # MODIFICATION: Added a friendly exit message
            print("Thank you for using the checkbook program. Goodbye!")
            break
        
        elif action.lower() == 'deposit':
            # MODIFICATION: Added try-except block to handle conversion errors
            try:
                amount = float(input("Enter the amount to deposit: $"))
                
                # MODIFICATION: Added validation for negative amounts
                if amount < 0:
                    print("Error: Amount cannot be negative. Please try again.")
                else:
                    cb.deposit(amount)
            
            # MODIFICATION: Catch ValueError exception if user enters text instead of number
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif action.lower() == 'withdraw':
            # MODIFICATION: Added try-except block to handle conversion errors
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                
                # MODIFICATION: Added validation for negative amounts
                if amount < 0:
                    print("Error: Amount cannot be negative. Please try again.")
                else:
                    cb.withdraw(amount)
            
            # MODIFICATION: Catch ValueError exception if user enters text instead of number
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif action.lower() == 'balance':
            cb.get_balance()
        
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()