from util     import Utility
from accounts import Accounts

#--------------------------------------------------------------------
# Contains command-specific infomation and the functions that run each command, eg. login, createacct, etc..
#--------------------------------------------------------------------
class Commands:
    # Enumeration of valid commands
    VALID_COMMANDS = [
        'DEP',
        'WDR',
        'XFR',
        'NEW',
        'DEL',
        'EOS'
    ]

    # Enumeration of unused values
    Unused = {
        'account' : '0000000',
        'amount'  : '000',
        'name'    : '***'
    }

    def __init__(self, oldMasterFile, newMasterFile, accountsFile): 
        self.lastCommand = ''
        self.accounts = Accounts(oldMasterFile, newMasterFile, accountsFile)

    #--------------------------------------------------------------------
    # EOS
    #--------------------------------------------------------------------
    def EOS(self, account1, account2, amount, name):
        if account1 != Unused.account or account2 != Unused.account:
            Utility.fatal('Invalid account number(s) in EOS command' + account1 + ' / ' + account2)
        elif amount != Unused.amount:
            fatalAmount('EOS', amount)
        elif name != Unused.name:
            fatalAccountName('EOS', name)
        else:
            # If this is the second EOS in a row, exit
            if cmd is 'EOS' and self.lastCommand is 'EOS':
                self.accounts.finish()
                sys.exit()

    #--------------------------------------------------------------------
    # Createacct
    #--------------------------------------------------------------------
    def NEW(self, account, amount, name):
        Utility.checkAccountNumber(account)
        Utility.checkAccountName(name)
        if account == Unused.account:
            fatalAccountNumber('NEW', account)
        if amount == Unused.amount:
            fatalAmount('NEW', amount)

        acct = self.accounts.getAccountByNumber(account)
        if acct is not None:
            Utility.log('Account number already exists.')
        else:
            self.accounts.addAccount(account1, 0, name)
    #--------------------------------------------------------------------
    # Deleteacct
    #--------------------------------------------------------------------
    def DEL(self, account, amount, name):
        Utility.checkAccountNumber(account)
        Utility.checkAccountName(name)
        if account == Unused.account:
            fatalAccountNumber('DEL', account)
        if amount == Unused.amount:
            fatalAmount('DEL', amount)
        self.accounts.deleteAccount(account1, name)

    #--------------------------------------------------------------------
    # Withdraw
    #--------------------------------------------------------------------
    def WDR(self, account, amount, name):
        Utility.checkAccountNumber(account)
        Utility.checkAmount(amount)
        if account == Unused.account:
            fatalAccountNumber('WDR', account)
        if name == Unused.name:
            fatalAccountName('WDR', name)
        self.accounts.withdraw(account, amount)

    #--------------------------------------------------------------------
    # Deposit
    #--------------------------------------------------------------------
    def DEP(self, account, amount, name):
        Utility.checkAccountNumber(account)
        Utility.checkAmount(amount)
        if account != Unused.account:
            fatalAccountNumber('DEP', account)
        self.accounts.deposit(account, amount)

    #--------------------------------------------------------------------
    # Transfer
    #--------------------------------------------------------------------
    def XFR(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAccountNumber(account2)
        Utility.checkAmount(amount)
        if account1 == Unused.account:
            fatalAccountNumber('XFR', account1)
        if account2 == Unused.account:
            fatalAccountNumber('XFR', account2)
        if name == Unused.name:
            fatalAccountName('XFR', name)
        self.accounts.transfer(account1, account2, amount)

    #--------------------------------------------------------------------
    # Dispatcher function that ensures it is a valid command
    #--------------------------------------------------------------------
    def runCommand(self, cmd, account1, account2, amount, name):
        if cmd not in VALID_COMMANDS:
            raise ValueError('Invalid command code: ' + cmd)
        else:
            getattr(Commands, cmd)(self)
            self.lastCommand = cmd

    def fatalAccountNumber(command, number):
        Utility.fatal('Invalid account number in ' + command + ' command: ' + number)

    def fatalAccountName(command, name):
        Utility.fatal('Invalid account name in ' + command + ' command: ' + name)

    def fatalAmount(command, amount):
        Utility.fatal('Invalid amount in ' + command + ' command: ' + amount)