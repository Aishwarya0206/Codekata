'''


Given a number n and m followed by n numbers remove the number m in the n number and print the remaining n number if m is not found print -1

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the remaining numbers or -1

Sample Input :
6 43
5 7 4 4 6 8

Sample Output :
-1

'''


n, m = tuple(map(int, input().split()))
l = list(map(int, input().split()))[:n]
if(m in l):
    l.remove(m)
    print(*l)
else:
    print(-1)