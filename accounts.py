from fileio import FileIO

class Accounts:
    #--------------------------------------------------------------------
    # Read in the given accounts file and construct the accounts list
    #--------------------------------------------------------------------
    @staticmethod
    def initialize(path):
        lines   = FileIO.readLines(path)
        cleaned = []
        
        if len(lines) < 1:
            raise ValueError('Empty Master Accounts File')

        # Clean and strip newlines from the numbers, then
        # ensure that they're valid account entries
        for line in lines:
            clean = Utility.cleanString(line)
            if (not clean.isdigit() or len(clean.strip()) != 7 or (
                clean != lines[-1].strip() and clean[0] == '0')):
                raise ValueError('Invalid accounts file, error: ' + clean)
            cleaned.append(clean)
        
        # Ensure that the last line is the all zero account number
        if (cleaned[-1] != "0000000"):
            raise ValueError('Invalid accounts file, missing zero account number at file end')

        return cleaned