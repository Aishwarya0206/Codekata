'''


Given a string print the vowels in the string

Input Description:
Given a string

Output Description:
Print the String

Sample Input :
guvi geek

Sample Output :
ui ee

'''


userInput = input()
vowels = 'aeiou'
for j in userInput:
  if(j in vowels or j.isspace()):
    print(j, end='')