'''


Given a numbers n followed by n*n numbers in matrix format print the sum of the numbers in the column

Input Description:
You will given a number n followed by n*m numbers in matrix format .

Output Description:
print the sum of the numbers in the column

Sample Input :
3 3
1 2 3
4 5 6
7 8 9

Sample Output :
12 15 18

'''


n, m = tuple(map(int, input().split()))
s = []
for i in range(n):
  l = [int(j) for j in input().split()][:m]
  s.append(l)
k = []
for i in range(n):
  c = 0
  for j in range(m):
    c+=s[j][i]
  k.append(c)
print(*k)