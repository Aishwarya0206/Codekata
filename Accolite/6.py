'''
Given 2 numbers N and M followed by 2 arrays A an B of sizes N and M. Check if array B is a subset of array A. if yes print 'yes' else print 'no'.
Input Size : 1 <= N <= 1000000
Sample Testcases :
INPUT
7 6
1 2 3 4 5 6 7
3 4 5 6 7 1
OUTPUT
yes
'''

N, M = tuple(map(int, input().strip().split()))
A1 = [int(i) for i in input().strip().split()][:N]
A2 = [int(i) for i in input().strip().split()][:M]
s = []

for i in range(M):
  if(A2[i] in A1):
    s.append(True)
  else:
    s.append(False)
if(False in s):
  print('no')
else:
  print('yes')