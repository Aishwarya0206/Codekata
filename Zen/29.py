'''


Given a string reverse the words in the string

Input Description:
Given a string

Output Description:
Print string into reverse the words in the string

Sample Input :
guvi geek

Sample Output :
ivug keeg

'''

#Getting input via STDIN
userInput = [i for i in input().strip().split()]
k = []
for j in userInput:
  r = ''
  for i in j:
    r = i+r
  k.append(r)
print(' '.join(k))