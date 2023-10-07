'''
Given a number n followed by n numbers Find the sum of the elements in an array and print sum of number is odd or even

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
print sum of number is odd or even

Sample Input :
3
5 7 4

Sample Output :
even
'''


n = int(input())
userInput = sum([int(i) for i in input().strip().split()][:n])
print('even' if(userInput%2==0) else 'odd')