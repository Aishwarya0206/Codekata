'''
Given 2 numbers N and K and followed by an array of N integers. The given element K is removed from the array and new array is printed. If after removing every occurance of K the array becomes empty, print 'empty' without quotes.
Example:
Input: {10,10,20,30,76}, K=10
Output: {20,20,76}
Input Size : N <= 100000
Sample Testcase :
INPUT
5 10
10 10 20 30 76
OUTPUT
20 30 76
'''

N, M = tuple(map(int, input().strip().split()))
A1 = [int(i) for i in input().strip().split()][:N]
A2 = []
while(M in A1):
  A1.remove(M)
for k in A1:
  A2.append(str(k))
if(len(A2)>0):
    print(' '.join(A2))
else:
    print('empty')