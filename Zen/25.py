'''


 Given a string find the number of uppercase letters and lowercase letters

Input Description:
Given a string

Output Description:
Print the number of uppercase and lowercase

Sample Input :
Guvi Geek

Sample Output :
2 6

'''

#Getting input via STDIN
userInput = input()
c1 = 0
c2 = 0
for i in userInput:
  if(i.isupper()):
    c1+=1
  if(i.islower()):
    c2+=1
print(c1, c2)