# ------------------------------------------------- #
# Title: Assignment 07
# Description: Simple Modification of HomeInventory Script with Pickling and Error Handling
# ChangeLog: (Who, When, What)
# TH,11/29/2022,Created Script
# ------------------------------------------------- #
# -------------------DATA--------------------------------#
# Import Other Libraries
import pickle # imports pickle library

# Global Variable Declarations
strFileName = 'A07.dat'  # file name changed from Lab 7-1 as to not conflict with Lab 7-1 file
lstItemValue = []

# -------------------PROCESSING---------------------------#
# Define Functions
def save_data_to_file(file_name, list_of_data):
    """
    This function saves a list of data to a binary file.

    :param file_name: Name of binary file (.dat format)
    :param list_of_data: List of user data
    :return: No return variable, this function just saves the data to the file
    """

    file = open(file_name, "ab")  # ab = a refers to append, b refers to binary
    pickle.dump(list_of_data, file)  # pickle.dump() function means to "dump" data into the file. Pickle specific
    file.close()

def read_data_from_file(file_name):
    """
    This function reads 1 row of existing binary data from the binary file

    :param file_name: Name of binary file
    :return: Returns 1 row of list_of_data which is converted from binary to text
    """
    file = open(file_name, "rb")  # rb = r refers to read, b refers to binary
    list_of_data = pickle.load(file)  # pickle.load() function ONLY unpickles 1 line!!
    file.close()
    return list_of_data

def read_ALLdata_from_file(file_name):
    """
    This function reads all rows of existing binary data from the binary file.
    As the function automatically returns a print statement, you only need to call the function (don't print call)

    :param file_name: Name of binary file
    :return: Returns and PRINTS all rows of list_of_data which is converted from binary to text. Call function only
    """
    try:
        file = open(file_name, "rb")  # rb = r refers to read, b refers to binary
        for row in file_name:
            list_of_data = pickle.load(file)
            print(list_of_data)
    except EOFError as e:
        file.close()
        return print("No more contents in file!!")
    except Exception as e:
        file.close()
        return print("unspecified error!")

# ------------------PRESENTATION---------------------------#
# Main Script Body
while(True):
    print("""
    Menu of Options
    1) Enter and append data to binary file
    2) Read 1 line of existing data in binary file
    3) Read all existing data in binary file
    4) Exit Menu
    Note: If you enter anything but the above options, the menu will persist
    """)

    strChoice = str(input("Which option would you like to perform? [1-4]:   "))
    print() # line for looks

# Choice 1: User Input / Append
    if (strChoice.strip() == '1'):
        try:
            strName = str(input("Enter an item name: "))
            if strName.isnumeric():
                raise Exception("Please do not use numbers!")
            else:
                intValue = int(input("Enter a value ($): "))
                lstNameValue = [intValue, strName]
                save_data_to_file(strFileName, lstNameValue)
                print()
                print("Data saved as binary to:", strFileName)
        except ValueError as e:
            print("Please enter a number for the item's value!")
        except Exception as e:
            print()  # space for looks
            print("There was a non specific error!")
            print()  # space for looks
            print("Built in Python error info: ")
            print(e, sep='\n')

# Choice 2: read 1 line of data
    elif (strChoice.strip() == '2'):
            print(read_data_from_file(strFileName))

# Choice 3: read all lines of data
    elif (strChoice.strip() == '3'):
        read_ALLdata_from_file(strFileName) # function has built in print, removed print

# Choice 4: exit and terminate program
    elif (strChoice.strip() == '4'):
        break