'''


Given a string find the number of special characters if their no special characters print -1

Input Description:
Given a string

Output Description:
Print number of special characters or -1

Sample Input :
Guvi Geek

Sample Output :
-1

'''


special_char = '''-\{};,.~'"!@#$%^&*()[]:?/|_'''
userInput = input()
k = 0
for i in userInput:
  if(i in special_char):
    k+=1
if(k>0):
  print(k)
else:
  print(-1)