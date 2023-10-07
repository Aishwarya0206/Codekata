'''
Given a number N followed by an array of N integers, every element appears twice except for one. Find that single one and print it.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
30 5 5 30 -45
OUTPUT
-45
'''

N = int(input())
l = [int(i) for i in input().split()][:N]
s = []
for i in l:
    if(l.count(i) == 1):
        s.append(i)
print(*s)