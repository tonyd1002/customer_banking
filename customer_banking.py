# Import the create_cd_account and create_savings_account functions
from Accounts import create_cd_account, create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the initial balance for the Savings Account: "))
    savings_interest = float(input("Enter the annual interest rate (APR) for the Savings Account: "))
    savings_maturity = int(input("Enter the number of months for the Savings Account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance.
    print(f"\nSavings Account:")
    print(f"Interest Earned: ${savings_interest_earned:.2f}")
    print(f"Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nEnter the initial balance for the CD Account: "))
    cd_interest = float(input("Enter the annual interest rate (APR) for the CD Account: "))
    cd_maturity = int(input("Enter the number of months for the CD Account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance.
    print(f"\nCD Account:")
    print(f"Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()

