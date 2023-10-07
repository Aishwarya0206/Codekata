'''


Given a number n Find whether the number is divisible  by 2,3 and 5.if divisible print yes else print no

Input Description:
0<n<1000 Given a number n

Output Description:
Print yes or no

Sample Input :
30

Sample Output :
yes

'''

userInput = int(input())
print('yes' if(userInput%2 == 0 and userInput%3 == 0 and userInput%5 == 0) else 'no')