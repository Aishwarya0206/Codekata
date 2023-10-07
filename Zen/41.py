'''


Given a string find the length of the string without space

Input Description:
Given a string

Output Description:
Print length in number

Sample Input :
guvi geek

Sample Output :
8

'''

n = input()
c = 0
for i in n:
    if i.isspace() == False:
        c+=1
print(c)