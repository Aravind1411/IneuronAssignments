'''1.Introduction
This assignment will help you to consolidate the concepts learnt in the session.
2.Problem Statement
1. Write a program which accepts a sequence of comma-separated numbers from console
and generate a list.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
Sample Output:
1. Create the below pattern using nested for loop in Python.
2. Write a Python program to reverse a word after accepting the input from the user.
Input word: ineuron
Output: norueni
'''
n=int(input())
for i in range(1,(n//2)+2):
    print("*"*i)
for i in range(n//2,0,-1):
    print("*"*i)


a=input()
print(a[::-1])