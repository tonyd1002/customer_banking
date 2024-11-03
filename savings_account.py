# Import the Account class from the Account.py file
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        tuple: The updated savings account balance and interest earned.
    """
    # Create an instance of the `Account` class and pass in the initial balance and an interest of 0
    savings_account = Account(balance, 0)

    # Calculate the monthly interest rate and interest earned (compounded monthly)
    monthly_interest_rate = interest_rate / 12 / 100
    interest_earned = savings_account.get_balance() * monthly_interest_rate * months

    # Update the savings account balance by adding the interest earned
    updated_balance = savings_account.get_balance() + interest_earned

    # Set the new balance and interest earned in the Account instance
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_rate)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned

