#!/usr/bin/env python

#--------------------------------------------------------------------
# CMPE327 Assignment 4
# Jonathan Turcotte, Omar Sandarusi
# 1048455, 10097124
# 11JLT10, 12OZS
#--------------------------------------------------------------------

import sys
import argparse
from fileio import FileIO
from commands import Commands
from util import Utility

#--------------------------------------------------------------------
# Get the command line options
#--------------------------------------------------------------------
def commandArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("mergedtransactionfile")
    parser.add_argument("oldmasterfile")
    parser.add_argument("newmasterfile")
    parser.add_argument("newaccountsfile")
    return parser.parse_args()
          
#--------------------------------------------------------------------
# Validate that this is a valid command
#--------------------------------------------------------------------
def validCommand(inp):
    if (inp in Commands.VALID_COMMANDS):
        return True
    else:
        return False



#--------------------------------------------------------------------
# Main
#--------------------------------------------------------------------

# Get the commandline arguments
args = commandArgs()

# Read in the accounts file
try:
    accounts = readAccounts(args.accountfile)
except ValueError as e:
    print e.message
    FileIO.writeLines(args.transactionfile, ['EOS 0000000 000 0000000 ***'])
    sys.exit()

# Instantiate our commands object
commands = Commands(accounts, args.transactionfile)

print("\n############")
print(" BACK END")
print("############\n")

while(True):
    commands.runCommand(getCommand())