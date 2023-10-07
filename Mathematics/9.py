'''
Given 3 numbers a,b,c print a*b mod c.
Sample Testcase :
INPUT
5 3 2
OUTPUT
1
'''

a,b,c = [int(i) for i in input().split()]
print(a*b%c)