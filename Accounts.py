class Account:
    """A class to represent a bank account with balance and interest rate management."""

    def __init__(self, balance=0.0, interest=0.0):
        """
        Initialize the account with an initial balance and interest rate.

        Parameters:
        balance (float): The initial balance of the account.
        interest (float): The interest rate of the account as a percentage.
        """
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """
        Set the balance of the account.

        Parameters:
        balance (float): The balance to set.
        """
        self.balance = balance

    def set_interest(self, interest):
        """
        Set the interest rate of the account.

        Parameters:
        interest (float): The interest rate as a percentage.
        """
        self.interest = interest

    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
        float: The current account balance.
        """
        return self.balance

    def get_interest(self):
        """
        Get the current interest rate of the account.

        Returns:
        float: The current interest rate as a percentage.
        """
        return self.interest

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.

        Parameters:
        amount (float): The amount to deposit. Must be positive.

        Raises:
        ValueError: If the deposit amount is not positive.
        """
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account.

        Parameters:
        amount (float): The amount to withdraw. Must be positive and not exceed the balance.

        Raises:
        ValueError: If the withdrawal amount is not valid.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount.")

    def calculate_interest(self):
        """
        Calculate the interest earned on the current balance.

        Returns:
        float: The interest earned based on the current balance and interest rate.
        """
        return self.balance * (self.interest / 100)

