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
            Utility.fatal('Invalid amount in EOS command: ' + amount)
        elif name != Unused.name:
            Utility.fatal('Invalid account name in EOS command: ' + name)
        else:
            # If this is the second EOS in a row, exit
            if cmd is 'EOS' and self.lastCommand is 'EOS':
                self.accounts.finish()
                sys.exit()

    #--------------------------------------------------------------------
    # Createacct
    #--------------------------------------------------------------------
    def NEW(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAccountName(name)
        if account2 != Unused.account:
            Utility.fatal('Invalid account number in NEW command' + account2)
        elif amount != Unused.amount:
            Utility.fatal('Invalid amount in NEW command: ' + amount)

        acct = self.accounts.getAccountByNumber(account1)
        if acct is not None:
            Utility.log('Account number already exists.')
        else:
            self.accounts.addAccount(account1, 0, name)
    #--------------------------------------------------------------------
    # Deleteacct
    #--------------------------------------------------------------------
    def DEL(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAccountName(name)

        if account2 != Unused.account:
            Utility.fatal('Invalid account number in DEL command' + account2)
        elif amount != Unused.amount:
            Utility.fatal('Invalid amount in DEL command: ' + amount)
        else:
            self.accounts.deleteAccount(account1, name)

    #--------------------------------------------------------------------
    # Withdraw
    #--------------------------------------------------------------------
    def WDR(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAmount(amount)

        if account2 != Unused.account:
            Utility.fatal('Invalid account number in WDR command' + account2)
        elif name != Unused.name:
            Utility.fatal('Invalid account name in WDR command: ' + name)
        else:
            self.accounts.withdraw(account1, amount)

    #--------------------------------------------------------------------
    # Deposit
    #--------------------------------------------------------------------
    def DEP(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAmount(amount)

        if account2 != Unused.account:
            Utility.fatal('Invalid account number in DEP command' + account2)
        elif name != Unused.name:
            Utility.fatal('Invalid account name in DEP command: ' + name)
        else:
            self.accounts.deposit(account1, amount)

    #--------------------------------------------------------------------
    # Transfer
    #--------------------------------------------------------------------
    def XFR(self, account1, account2, amount, name):
        Utility.checkAccountNumber(account1)
        Utility.checkAccountNumber(account2)
        Utility.checkAmount(amount)

        if name != Unused.name:
            Utility.fatal('Invalid account name in XFR command: ' + name)
        else:
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