'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1.Takes an integer input from the user.
2.  Checks whether the number is even or odd using an if-else
statement.
3. Displays the result accordingly.
'''

n = int(input("Enter a number: "))
if n%2 ==0:
    print(n,"is an even number")
else:
    print(n,"is an odd number")