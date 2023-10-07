'''


Given a year, find whether leap year or not?

Input Description:
Given a 4 digit number

Output Description:
Print leap year or not a leap year

Sample Input :
1996

Sample Output :
leap year

'''

#Getting input via STDIN
userInput = int(input())
print('leap year' if(userInput%4 == 0) else 'not a leap year')