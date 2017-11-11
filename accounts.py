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
        if (not isinstance(number, int) or not isinstance(balance, int)):
            Utility.fatal('Add account must receive integer numbers and balances')
        for account in self.list:
            if account.number == number:
                Utility.fatal('Attempting to add account: Account already exists for number ' + number)
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

    def deleteAccount(self, number):
        for i, account in enumerate(self.list):
            if account.number == number:
                del self.list[i]
                break

    def deposit(self, number, amount):
        return
    
    def withdraw(self, number, amount):
        return

    def finish(self): #sort and write
        return