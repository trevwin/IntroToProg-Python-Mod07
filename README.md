Trevor Huynh

Nov 29, 2022

IT FDN 110 A

Assignment 07

https://github.com/trevwin/IntroToProg-Python-Mod07

# **Structured Error Handling / Pickling**
## **1.0 Introduction**

In this week, the topics covered were structured error handling / pickling. 

In this assignment, structured error handling and pickling will be explained along with code demos to show their functionality. A final script will be presented that incorporates both demos into a combined script based on a modification of assignments 05, 06, and Lab 7-1. 

## **2.0 Python Error Types**

There are 2 types of errors in Python: syntax and exception errors [2]. Syntax errors occur when the code has incorrect statements (ie. mismatched brackets). Exception errors occur when syntactically correct Python code results in an error [3]. In this assignment, exception errors will be covered. 

## **3.0 Basic Exception Error Catching**

Although Python has a standard library of built-in exceptions, it sometimes is not intuitive to the user at first glance. Understanding the standard exception error in Python may require going into the official Python 3 documentation and looking into the specific error class. Structured error handling allows for the user to display more easy to follow error descriptions for diagnosing errors in Python code. 

The most basic form of error handling comes in the form of a try-except statement. The try clause executes the statement between the try and except keywords. If there is no exception, the code skips the except block. If there is an exception (ie. exception error), the except block then executes. Without this basic exception handling, the exception error could crash the script. As this is a basic method to catch an exception error, one of the issues is that it hides all errors and catches it with this basic clause. Essentially, you wouldn’t be able to tell if you had a Python built-in ZeroDivisionError or a FileNotFoundError as the except block catches all of the errors. 

![Figure 1. Try Except Block Summary. Taken from [3]](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F1.png)

*Figure 1. Try Except Block Summary. Taken from [3]*

## **4.0 Custom Exception Error Catching**

The basic try-except block can be made more sophisticated in order to catch specific errors. 

Python automatically creates an Exception object with error information when an error occurs [4]. This can be captured in a try-except block with error information extracted out. 

In addition, catching specific errors can be done by “raising” an exception. Raising an exception creates an exception based on a specific condition [3]. 

## **4.1 Demo 1 – Error Catching**

In this demo, error handling will be applied to the user inputs section of the script. This demo is similar to the HomeInventory script in assignments 05 and 06 where the user inputs the name of an item and it’s associated value. 

![Figure 2. User Inputs Script](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F2.png)

*Figure 2. User Inputs Script*

The anticipated error here is if the user enters a string for the value. At first glance, it is not possible to know what kind of exception object will be created so before doing the error handling, the script is first run by entering a string for the value of the item. 

![Figure 3. Exception Error - ValueError](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F3.png)

*Figure 3. Exception Error - ValueError*

We can see here that the since the item name is a string variable, it can take integer inputs and will not result in an error. Conversely, we can also see that entering a string input to the value of the item then results in an error that crashes the script. 

The exception object created by the error of entering a string for the value is exception object ValueError. We can then use this to deal with this specific exception. 

The addition of an if-else statement with the isnumeric() function can also catch if the user does not enter a proper item name.  Also, I decided to raise a custom exception for this specific case to contain the numeric error. 

![Figure 4. Completed Error Handling for User Input](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F4.png)

*Figure 4. Completed Error Handling for User Input*

![Figure 5. Error Handling Result (ValueError)](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F5.png)

*Figure 5. Error Handling Result (ValueError)*

## **5.0 Pickling**

Pickling is a method to store data in a binary format that obscures the data [4]. This means it converts Python objects into a binary data. The advantage of pickling is to allow for easy data transfer from one system to another and then store it in a file or database [5]. 

To pickle data, the pickle library must be imported into Python. Two functions save_data_to_file, read_data_from_file were defined to save data into binary (pickle) and to read the binary file as text (unpickle). 

Pickling and unpickling requires pickle library specific functions pickle.dump() and pickle.load() which convert data into binary and convert binary to text respectively. 

## **5.1 Demo 2 - Pickling**

Two functions were created based on Lab 7-1 to demonstrate this. 

![Figure 6. Saving Data as Binary to File Function](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F6.png)

*Figure 6. Saving Data as Binary to File Function*

![Figure 7. Reading Data From Binary to Text Function (one line)](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F7.png)

*Figure 7. Reading Data From Binary to Text Function (one line)*

![Figure 8. Demo 2 – Main Script](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F8.png)

*Figure 8. Demo 2 – Main Script*

![Figure 9. PyCharm Output of Script and Binary Data](https://github.com/trevwin/IntroToProg-Python-Mod07/blob/main/docs/F9.png)

*Figure 9. PyCharm Output of Script and Binary Data*
