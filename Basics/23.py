'''
Given numbers A,B find A^B.
Input Size : 1 <= A <= 5 <= B <= 50
Sample Testcase :
INPUT
3 4
OUTPUT
81
'''

A, B = [int(i) for i in input().split()]
print(A**B)