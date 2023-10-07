'''


Given a number n followed by n numbers short the n number in ascending order 

 

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the n number in ascending order

Sample Input :
6
5 7 4 4 6 8

Sample Output :
4 4 5 6 7 8

'''


#Getting input via STDIN
n = int(input())
userInput = sorted([int(i) for i in input().split()][:n])
print(*userInput)