# Boyang Ji 201649047

import random
import datetime


class BasicAccount:
    """
    A class about basic bank accounts.
    Attributes:
        name (string): the account holder's name.
        acNum (int): the number of the account and should be “serial”.
        balance (float): The balance (in pounds) of the account.
        cardNum (string): The card number.
        cardExp (tuple(int,int)): Expiry date of the account(mm,yy).
        overdraft (boolean): a Boolean variable.
        overdraftLimit (float): Maximum overdraft on an account.
    """
    acNum = 0

    def __init__(self, acname, openingBalance):
        """
        Initialiser giving the account name and opening balance.
        Args:
            acName (string): the account holder's name.
            openingBalance (float): The balance (in pounds) of the account.
        """
        self.overdraft = False  # Initially set to no overdrafts
        self.overdraftLimit = 0  # Initially set to an overdraft amount of 0
        self.name = acname
        self.balance = float(openingBalance)
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum

    def __str__(self):
        """
        Presentation of basic information about the account.
        Returns:
            str : name, account number, balance, and current overdraft amount
        """
        return f"""This account belongs to {self.name},
             available balance is £{self.balance}
             and overdraft limit is {self.overdraftLimit}"""

    def deposit(self, amount):
        """
        Deposits the stated amount into the account.
        Deposits must be a positive amount.
        Args:
            amount (float): amount of money to be deposited
        """
        if amount <= 0:
            print("You can only deposit a positive amount of money!")
        else:
            self.balance += amount

    def withdraw(self, amount):
        """
        Function to withdraw money from the bank account.
        If an valid amount is requested, prints a message of
            “<Name> haswithdrawn £<amount>. New balance is £<amount>”.
        If an invalid amount is requested, prints a message of
            “Can not withdraw £<amount>".
        The amount is invalid:
            it is greater than the balance of the Basic Account
            it is greater than the balance + the overdraft limit of the Premium Account.
        Args:
            amount (float): amount of money to be withdrawn
        """
        if self.overdraft is False:
            if amount <= self.balance:
                self.balance -= amount
                print(f"""{self.name} has withdrawn £{amount}.
                 New balance is £{self.balance}.""")
            else:
                print(f"You can not withdraw £{amount} ")
        else:  # self.overdraft = True
            if amount > self.balance + self.overdraftLimit:
                print(f"You can not withdraw £{amount}")
            else:
                self.balance -= amount
                print(f"""{self.name} has withdrawn £{amount}.
                 New balance is £{self.balance}.""")

    def getAvailableBalance(self):
        """
        Returns the total balance that is available in the account as a float.
        It should also take into account any overdraft that is available.
        Returns:
            float : the total balance that is available in the account
        """
        return float(self.balance + self.overdraftLimit)

    def getBalance(self):
        """
        Returns the balance of the account as a float.
        If the account is overdrawn, it should return a negative value.
        Returns:
            float : the balance of the account
        """
        return float(self.balance)

    def printBalance(self):
        """
        Print out the balance of account on the screen.
        If an overdraft is available, then this should also be printed and
            it should show how much overdraft isremaining.
        """
        print(f"""{self.name} current balance is {self.balance} and
         now overdraft limit is £{self.overdraftLimit + self.balance}""")

    def getName(self):
        """
        Returns the name of the account holder as a string.
        Returns:
            str : name of the account holder
        """
        return self.name

    def getAcNum(self):  # need return string
        """
        Returns the account number as a string.
        Returns:
            str : account number
        """
        return str(self.acNum)

    def issueNewCard(self):
        """
        Creates a new card number,
            with the expiry date being 3 years to the month from now
        (e.g., if today is 1/12/21, then the expiry date would be (12/24)).
            cardNum (string): The card number.
            cardExp (tuple(int,int)): Expiry date of the account(mm,yy).
        """
        self.cardNum = "".join(random.choice("0123456789") for i in range(16))
        print(f"Your card number is {self.cardNum}")
        todayDate = datetime.date.today()
        extractYear = datetime.datetime.strftime(todayDate, '%y')
        self.createDate = (todayDate.month, int(extractYear))
        self.cardExp = (todayDate.month, int(extractYear) + 3)
        print(f"""Card opening date is {self.createDate}
         and expiry date is {self.cardExp}""")

    def closeAccount(self):
        """
        If the balance of the account is a positive number,
            withdraw all the amounts and close the account
            and returns True.
        If the balance of the account is a negative number, print
            Can not close account due to customer being overdrawn by £<amount>
            and returns False
        Returns:
            bool : account closing possible if True
        """
        if self.balance >= 0:
            self.withdraw(self.balance)
            return True
        else:
            print(f"""Can not close account
             due to customer being overdrawn by £{-self.balance}""")
            return False


class PremiumAccount(BasicAccount):
    """
    A class about premium bank accounts.
    Attributes:
        name (string): the account holder's name.
        acNum (int): the number of the account and should be “serial”.
        balance (float): The balance (in pounds) of the account.
        cardNum (string): The card number
        cardExp (tuple(int,int)): Expiry date of the account(mm,yy).
        overdraft (boolean): a Boolean variable
        overdraftLimit (float): Maximum overdraft on an account.
    """
    def __init__(self, acname, openingBalance, initialOverdraft):
        """
        Inherited attributes acname, openingBalance from parent class
        initialiser giving overdraft limit.
        Args:
            acName (str): name of the account holder
            openingBalance (float): balance on opening an account
            initialOverdraft (float): overdraft limit while opening an account
        """
        super().__init__(acname, openingBalance)
        self.overdraft = True
        self.overdraftLimit = float(initialOverdraft)

    def __str__(self):
        """
        Inherit this method from the parent class.
        """
        return super().__str__()

    def setOverdraftLimit(self, newLimit):
        """
        Sets the overdraft limit to the stated amount
        Args:
            newLimit (float): new overdraft limit to be set
        """
        self.overdraftLimit = newLimit

    def getAvailableBalance(self):
        """
        Inherit this method from the parent class.
        """
        return super().getAvailableBalance()

    def printBalance(self):
        """
        Inherit this method from the parent class.
        """
        return super().printBalance()

    def closeAccount(self):
        """
        Inherit this method from the parent class.
        """
        return super().closeAccount()
