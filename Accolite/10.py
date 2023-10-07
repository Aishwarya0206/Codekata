'''
Given 2 numbers N and K followed by N elements, find the Kth smallest element.If the element cannot be found then print -1
Input Size : N <= 100000
Sample Testcase :
INPUT
5 2
1 1 2 4 5
OUTPUT
2
'''

n, m = tuple(map(int, input().strip().split()))
s = sorted(list(set([int(i) for i in input().strip().split()][:n])))
if(m in s):
  print(s[m-1])
else:
  print(-1)