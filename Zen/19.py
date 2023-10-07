'''


Given a string remove special characters if there is no special characters print -1

Input Description:
Given a string

Output Description:
Print the string or -1

Sample Input :
Xyz-aBc-nMk

Sample Output :
XyzaBcnMk

'''

special_char = '''-\{};,.~'"!@#$%^&*()[]:?/|_'''
userInput = input()
userInput1 = ''
s = []
for i in userInput:
  for j in special_char:
    if(i==j):
      userInput1 = userInput.replace(i, '')
    else:
      s.append(-1)
if(userInput1!=''):
  print(userInput1)
else:
  print(-1)