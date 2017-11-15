from fileio import FileIO
from account import Account
from util import Utility

class Accounts:
    def __init__(self, oldMasterFile, newMasterFile, accountsFile):
        lines = FileIO.readLines(oldMasterFile)
        if len(lines) < 1:
            Utility.fatal('Empty Master Accounts File')
        self.newMasterFile = newMasterFile
        self.accountsFile = accountsFile
        self.list = []
        count = 0
        for line in lines:
            line = line.strip("\r\n ")
            params = line.split(' ')

            if (len(params) != 3):
                Utility.fatal("Line " + str(count) + " is invalid - parameter count != 3")
         
            Utility.checkAccountNumber(params[0])
            Utility.checkAmount(params[1])  
            Utility.checkAccountName(params[2])

            self.list.append(Account(int(params[0]), int(params[1]), params[2]))
    
    def addAccount(self, number, name): #number and balance have to be int
        if self.getAccountByNumber(number) is None:
            Utility.log('Account already exists for account: ' + number)
        else:
            self.list.append(Account(number, 0, name))

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
        acct = self.getAccountByNumber(number)
        if acct is None:
            Utility.log('Aborting delete, account does not exist: ' + number)
            return

        if acct.balance != 0:
            Utility.log('Aborting delete, account balance is not zero: ' + number)
        elif acct.name != name:
            Utility.log('Aborting delete, account names do not match: ' + name + ' / ' + acct.name)
        else:
            for i, account in enumerate(self.list):
                if account.number == number:
                    del self.list[i]
                    break

    def deposit(self, number, amount):
        acct = self.getAccountByNumber(number)
        if acct is None:
            Utility.log('Aborting deposit, account does not exist: ' + number)
            return
        acct.balance += amount
    
    def withdraw(self, number, amount):
        acct = self.getAccountByNumber(number)
        if acct is None:
            Utility.log('Aborting withdrawal, account does not exist: ' + number)
            return
        if acct.balance < amount:
            Utility.log('Aborting withdrawal, the account does not have enough funds: ' + number)
        else:
            acct.balance -= amount

    def transfer(self, fromNumber, toNumber, amount):
        fromAcct = self.getAccountByNumber(fromNumber)
        toAcct   = self.getAccountByNumber(toNumber)

        if fromAcct is None:
            Utility.log('Aborting transfer, account does not exist: ' + fromNumber)
        elif toAcct is None:
            Utility.log('Aborting transfer, account does not exist: ' + toNumber)
        elif fromNumber == toNumber:
            Utility.log('Aborting transfer, cannot transfer between the same accounts: ' + fromNumber + '/' + toNumber)
        elif fromAcct.balance < amount:
            Utility.log('Aborting transfer, not enough funds in the source account: ' + fromNumber)
        else:
            fromAcct.balance -= amount
            toAcct.balance   += amount
        return

    def finish(self): #sort and write
        return


#--------------------------------------------------------------------
# Sort our points by x and y
#--------------------------------------------------------------------
def sort():
    global xPoints
    global yPoints

    xPoints = mergesort('x', Points)
    yPoints = mergesort('y', Points)

#--------------------------------------------------------------------
# Sort each pair of coordinates by either their x or y values
#--------------------------------------------------------------------
def mergesort(coord, points):
    if (len(points) == 1 or len(points) == 0):
        return points

    mid = len(points) / 2
    
    l = mergesort(coord, points[:mid])
    r = mergesort(coord, points[mid:])

    return merge(coord, l, r)