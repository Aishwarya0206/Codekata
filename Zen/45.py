'''


Given a numbers n followed by n*n numbers in matrix format print the sum of the numbers in the row

Input Description:
You will given a number n followed by n*m numbers in matrix format .

Output Description:
print the sum of the numbers in the row

Sample Input :
3 3
1 2 3
4 5 6
7 8 9

Sample Output :
6 15 24

'''

n, m = tuple(map(int, input().split()))
l = []
for i in range(n):
    get = sum([int(j) for j in input().split()][:m])
    l.append(get)

print(*l)