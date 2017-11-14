from fileio import FileIO
from account import Account
from util import Utility

class Accounts:
    def __init__(self, oldMasterFile, newMasterFile, accountsFile):
        lines = FileIO.readLines(path)
        if len(lines) < 1:
            Utility.fatal('Empty Master Accounts File')
        self.newMasterFile = masterFile
        self.accountsFile = accountsFile
        self.list = []
        count = 0
        for line in lines:
            line = line.strip("\r\n ")
            params = line.split(' ')
            if (params.length != 3):
                Utility.fatal("Line " + count + " is invalid - parameter count != 3")
            if (not Utility.checkAccountNumber(params[0])):
                Utiltiy.fatal("Line " + count + " contains invalid account number")
            if (not Utility.checkAmount(params[1])):
                Utiltiy.fatal("Line " + count + " contains invalid account balance")
            if (not Utility.checkAccountName(params[2])):
                Utiltiy.fatal("Line " + count + " contains invalid account name")
            self.list.append(Account(int(params[0]), int(params[1]), params[2]))
    
    def addAccount(self, number, balance, name): #number and balance have to be int
        if getAccountByNumber(number) is None:
            Utility.log('Account already exists for account: ' + number)
        else:
            self.list.append(Account(number, balance, name))

    def getAccountByNumber(self, number):
        for account in self.list:
            if account.number == number:
                return account
        return None

    def getAccountByName(self, name):
        for account in self.list:
            if account.name == name:
                return account
        return None

    def deleteAccount(self, number, name):
        acct = getAccountByNumber(number)
        if acct is None:
            Utility.log('Aborting delete, account does not exist: ' + number)
            return
        elif acct.balance != 0:
            Utility.log('Aborting delete, account balance is not zero: ' + number)
        elif acct.name != name:
            Utility.log('Aborting delete, account names do not match: ' + name + ' / ' + acct.name)
        else:
            for i, account in enumerate(self.list):
                if account.number == number:
                    del self.list[i]
                    break

    def deposit(self, number, amount):
        acct = getAccountByNumber(number)
        if acct is None:
            Utility.log('Aborting deposit, account does not exist: ' + number)
            return
        acct.balance += amount
    
    def withdraw(self, number, amount):
        return

    def transfer(self, fromNumber, toNumber, amount):

        # if not fromAccount in self.accounts:
        #     Utility.error("Account does not exist")
        #     return

        # toAccount = Utility.getAccountNumber("To account #")
        # if toAccount is None:
        #     return
        # if not toAccount in self.accounts:
        #     Utility.error("Account does not exist")
        #     return

        # if (fromAccount == toAccount):
        #     Utility.error("Cannot transfer from and to the same account.")
        #     return

        # amount = Utility.getAmount(self.loginType, "Amount to transfer in cents")
        # if amount is None:
        #     return

        # self.transactions.transfer(fromAccount, toAccount, amount)

        return

    def finish(self): #sort and write
        return