'''
Given a number N, followed by an array of N elements,print 'yes' if it is a sorted array(either ascending or descending)otherwise print 'no'.
Input Size : 1 <= N <= 100000
Sample Testcase :
INPUT
3
2 3 7
OUTPUT
yes
'''
n = int(input())
l = [int(i) for i in input().split()][:n]
a = []
for i in range(n-1):
  if(l[i]<l[i+1]):
    a.append(True)
  else:
    a.append(False)
if(False in a):
  a = []
  for i in range(n-1):
    if(l[i]>l[i+1]):
      a.append(True)
    else:
      a.append(False)

if(False in a):
    print('no')
else:
    print('yes')