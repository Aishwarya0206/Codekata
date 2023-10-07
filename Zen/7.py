'''
Given a two number n and m find the Quotient and remainder

Input Description:
0<n<10000 0<m<10000 Given two number separated by a space

Output Description:
Need to print Quotient and remainder separated by a space

Sample Input :
6 3

Sample Output :
2 0
'''

#Getting input via STDIN
userInput = [int(i) for i in input().strip().split()]
print(userInput[0]//userInput[1], userInput[0]%userInput[1])