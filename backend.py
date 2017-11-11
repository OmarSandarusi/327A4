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
from accounts import Accounts

#--------------------------------------------------------------------
# Get the command line options
#--------------------------------------------------------------------
def getCommandArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("mergedtransactionfile")
    parser.add_argument("oldmasterfile")
    parser.add_argument("newmasterfile")
    parser.add_argument("newaccountsfile")
    return parser.parse_args()
          
#--------------------------------------------------------------------
# Validate that this is a valid command
#--------------------------------------------------------------------
def validCommand(command):
    if (command in Commands.VALID_COMMANDS):
        return True
    else:
        return False

#--------------------------------------------------------------------
# Main
#--------------------------------------------------------------------

args = getCommandArgs()
Accounts.initialize(args.accountfile)
commands = Commands(args.transactionfile)

while(True):
    commands.runCommand(getCommand())