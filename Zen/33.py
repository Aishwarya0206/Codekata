'''


Given a string convert string into upper case where their vowel character

Input Description:
Given a string

Output Description:
Print string into upper case

Sample Input :
guvi geek

Sample Output :
gUvI gEEk

'''

userInput = input()
vowels = 'aeiou'
for j in userInput:
  if(j in vowels):
    userInput = userInput.replace(j, j.upper())
print(userInput)