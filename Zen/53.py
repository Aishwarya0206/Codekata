'''


Given a number n followed by n numbers Print the index 2nd  smallest number in an array (1 base index)

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the smallest number index in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
1

'''


n = int(input())
l = [int(i) for i in input().split()][:n]
s_l = sorted(list(set(l)))
print(l.index(s_l[1])+1)