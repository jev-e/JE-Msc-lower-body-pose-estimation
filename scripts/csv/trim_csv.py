import sys, getopt
import csv
import pandas as pd

def ParseCommandLine(argv):
    inputFile = ""
    try:
        opts, args = getopt.getopt(argv[1:], "i:")
    except:
        print("Error parsing CSV")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i"):
            inputFile = arg
    print("Input File:", inputFile)
    ProcessCSVMain(inputFile)

def ProcessCSVMain(file):
    csv_data = pd.read_csv(file)
    print(csv_data.pop("timestamp"))
    
    


    

def PopColumns():
    print()




    

if __name__ == "__main__":
    ParseCommandLine(sys.argv)