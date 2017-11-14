from fileio import FileIO
from util import Utility

#--------------------------------------------------------------------
# Transaction container, exposes methods for adding different transactions to the in-memory list and then saving that list to the transaction file
#--------------------------------------------------------------------
class Transactions:
    transactions = []           
