import sys
import re

"""
check if user provided relative path to data file
if they didn't
"""
sys.argv[0] = "data.csv"
inputFile = sys.argv[0]

if(inputFile == ""):
    print("Error: Input file path not provided")
    sys.exit()

"""
Make sure the program works for windows and Mac/Unix
"""



class Person:
    lastName = ""
    firstName = ""
    mi = ""
    id = ""
    phoneNumber = ""

    def __init__(self, lastName, firstName, mi, id, phoneNumber):
        self.lastName = lastName
        self.firstName = firstName
        self.mi = mi
        self.id = id
        self.phoneNumber = phoneNumber

    def display(self):
        print("Employee id: " + self.id)
        print("\t" + self.firstName + " " + self.mi + " " + self.lastName)
        print("\t" + self.phoneNumber)


def readInputFile(fileName):
    inputFile = open('data\data.csv', 'r')
    inputFile.__next__()
    for line in inputFile:
        employee = line.split(",")
        lastName = employee[0]
        firstName = employee[1]
        mi = employee[2]
        id = employee[3]
        phoneNumber = employee[4]

        #change format of first and last name to correct format
        lastName.lower()
        lastName[0] = lastName[0].upper()
        firstName.lower()
        firstName[0] = firstName[0].upper()

        #format middle initial
        if mi == "":
            mi = 'X'
        elif len(mi) > 1:
            mi = mi[0]

        mi = mi.upper()

        #check if id is correct format
        x = re.search("[A-Z][A-Z][0-9][0-9][0-9][0-9]")
        if not x:
            print("Error: ID is not valid")




    inputFile.close()



#employee0 = Person("smith", "joe", "V", "BF7654", "214-256-5500")
#employee0.display()
readInputFile("data.csv")