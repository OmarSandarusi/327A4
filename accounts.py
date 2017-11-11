from fileio import FileIO
from account import Account
from util import Utility

class Accounts:
    def __init__(self, path):
        lines = FileIO.readLines(path)
        if len(lines) < 1:
            Utility.fatal('Empty Master Accounts File')
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
            self.list.append(Account(params[0], params[1], params[2]))