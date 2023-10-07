'''


Given a numbers n  followed by x and y array of n numbers add the array x and y and print the numbers

Input Description:
0<n<100 Given a number n Followed by n number in next line Followed by n number in next line

Output Description:
Print added n numbers

Sample Input :
6
5 7 4 4 6 8
1 2 3 5 1 1

Sample Output :
6 9 7 9 7 9

'''
n = int(input())
x = [int(i) for i in input().split()][:n]
y = [int(i) for i in input().split()][:n]
s = []
for i in range(n):
    for j in range(n):
        if(i==j):
            s.append(x[i]+y[j])
print(*s)