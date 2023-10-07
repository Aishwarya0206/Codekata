'''


Given a number n followed by n numbers Print the 2nd  smallest number in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the 2nd smallest number in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
5

'''

n = int(input())
l = sorted(list(set([int(i) for i in input().split()][:n])))
print(l[1])