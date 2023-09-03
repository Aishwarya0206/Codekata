'''
Given a number N and an array of N elements, find the Bitwise OR of the array elements.
Input Size : N <= 100000
Sample Testcase :
INPUT
2
2 4
OUTPUT
6
'''

a = int(input())
s = list(map(int,input().strip().split()))[:2]
sum = 0
for i in s:
  sum = sum | i
print(sum)