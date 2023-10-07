'''
Given a numbers n and m followed by n*m numbers in matrix format print the sum of the elements in the matrix the element which is even number

Input Description:
You will given a number n and m followed by n*m numbers in matrix format . 0<n<100 0,m<100

Output Description:
print the sum of the elements in the matrix the element which is even number

Sample Input :
3 3
1 2 3
4 5 6
7 8 9

Sample Output :
20
'''
from re import L
n, m = tuple(map(int, input().split()))
s = []
for i in range(n):
    l = [int(j) for j in input().split()][:m]
    s.append(l)
c = 0
for i in s:
  for j in range(len(i)):
    if((i[j]%2) == 0):
      c+=i[j]
print(c)