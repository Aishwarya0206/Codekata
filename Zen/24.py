'''


Given a string reverse the string

Input Description:
Given a string

Output Description:
Print string into reverse

Sample Input :
guvi geek

Sample Output :
geek guvi

'''

#Getting input via STDIN
userInput = [i for i in input().strip().split()]
a = []
for i in range(-1, -(len(userInput)+1), -1):
    a.append(userInput[i])
print(' '.join(a))