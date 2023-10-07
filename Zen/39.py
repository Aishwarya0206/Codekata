'''
Given a number n followed by n numbers Print the 2nd  largest number in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the second largest number in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
7
'''


n = int(input())
l = sorted(list(set(list(map(int, input().split()))[:n])), reverse=True)
print(l[1])