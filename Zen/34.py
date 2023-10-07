'''


Given a number n followed by n numbers short the n number in descending order 

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print short the n number in descending order

Sample Input :
6
5 7 4 4 6 8

Sample Output :
8 7 6 5 4 4

'''

#Getting input via STDIN
n = int(input())
userInput = sorted([int(i) for i in input().split()][:n], reverse=True)
print(*userInput)