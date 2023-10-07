'''


Given a number n followed by n numbers Print the largest number in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the largest number in an array

Sample Input :
6
5 7 4 4 6 8

Sample Output :
8

'''

#Getting input via STDIN
userInput = int(input())
val = max([int(i) for i in input().strip().split()][:userInput])
print(val)