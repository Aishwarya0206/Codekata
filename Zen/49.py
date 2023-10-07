'''


Given a numbers n followed by n*n numbers in matrix format print the column which sum of the numbers in the column should be equal to multiple of 3 if there is no column print -1.

Input Description:
You will given a number n followed by n*m numbers in matrix format

Output Description:
print the column in row format

Sample Input :
3 3
1 2 3
4 5 6
7 8 9

Sample Output :
1 4 7
2 5 8
7 8 9

'''

n, m = tuple(map(int, input().split()))
s = []
for i in range(n):
  l = [int(j) for j in input().split()][:m]
  s.append(l)
for i in range(n):
  for j in range(m):
    print(s[j][i], end = ' ')
  print()