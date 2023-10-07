'''
Given an array of N elements switch(swap) the element with the adjacent element and print the output.
Sample Testcase :
INPUT
5
3 2 1 2 3
OUTPUT
2 3 2 1 3
'''
a = int(input())

s = list(map(int,input().strip().split()))[:a]

a = a if(a%2 == 0) else a-1
for i in range(0, a, 2):
  t = s[i]
  s[i] = s[i+1]
  s[i+1] = t
k = [str(i) for i in s]
print(' '.join(k))