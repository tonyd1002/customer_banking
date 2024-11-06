# Import the Account class from the Accounts.py file
from Accounts import Accounts

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        tuple: The updated CD account balance and interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and 0 as interest initially
    cd_account = Account(balance, 0)

    # Calculate interest earned (assuming interest is compounded monthly)
    monthly_interest_rate = interest_rate / 12 / 100
    interest_earned = cd_account.get_balance() * monthly_interest_rate * months

    # Update the CD account balance by adding the interest earned
    updated_balance = cd_account.get_balance() + interest_earned

    # Set the new balance and interest earned in the Account instance
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_rate)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned

