'''
Given the values of a,b and x in the equation ax + b = y. Find the value of y.
Sample Testcase :
INPUT
3 5 2
OUTPUT
11
'''

a, b, x = [int(i) for i in input().split()]
print(a*x+b)