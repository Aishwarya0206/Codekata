'''


Given a number n followed by n numbers Print the smallest number in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the smallest number in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
4

'''

n = int(input())
userInput = [int(i) for i in input().strip().split()][:n]
print(min(userInput))