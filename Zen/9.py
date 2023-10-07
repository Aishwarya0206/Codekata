'''


Given a number  n Find the number of the digits of number n

Input Description:
0<n<10000 Given number n

Output Description:
Print the number of the digits of number n

Sample Input :
3589

Sample Output :
4

'''


userInput = int(input())
n = len([i for i in str(userInput)])
print(n)