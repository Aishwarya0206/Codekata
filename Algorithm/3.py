'''
Given a number N and an array of N elements,sort the array in increasing order and print the original indices of the elements present in sorted array.
Input Size : N <= 100000
Sample Testcase :
INPUT
5
5 4 3 2 1
OUTPUT
5 4 3 2 1
'''

N = int(input())
l = [int(i) for i in input().split()][:N]
s = sorted(l)
k = []
for i in s:
  k.append(l.index(i)+1)
print(*k)