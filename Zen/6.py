'''


Given a number n followed by n numbers Find the sum of the elements in an array

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the sum of the elements in an array

Sample Input :
3
5 7 4

Sample Output :
16

'''

n = int(input())
userInput = [int(i) for i in input().strip().split()][:n]
print(sum(userInput))