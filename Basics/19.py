'''
Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
Input Size N <= 100000
Sample Testcase :
INPUT
4
4 3 2 1
OUTPUT
0
'''

a = int(input())
s = list(map(int,input().strip().split()))[:a]
sum = s[0]
for i in s[1:]:
  sum = sum & i
print(sum)