'''


Given a number m and k separated by a space print the numbers between m and k

Input Description:
number m and n separated by a space 0<m<1000 0<n<1000 m<n

Output Description:
print the numbers between this two numbers

Sample Input :
5 8

Sample Output :
6 7

'''


userInput = [int(i) for i in input().strip().split()]
s = [str(i) for i in range(userInput[0]+1, userInput[1])]
print(' '.join(s))