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
