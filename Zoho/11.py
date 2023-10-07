'''
Given k sorted arrays of possibly different sizes, merge them and print the sorted output.
Input Size : N<=100
Example:
INPUT
k = 3
1 3
2 4 6
0 9 10 11
OUTPUT
0 1 2 3 4 6 9 10 11
'''

k = int(input())
l1 = []
l2 = []
for i in range(k):
    l1.append([int(i) for i in input().split()])
for i in l1:
  for j in i:
    l2.append(j)
l2 = sorted(l2)
l1 = []
for k in l2:
  l1.append(str(k))
print(' '.join(l1))