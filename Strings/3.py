'''


You are given a string.Your task is to print only the consonants present in the string without affecting the sentence spacings if present. If no consonants are present print -1

Input Description:
You are given a string ‘s’.

Output Description:
Print only consonants.

Sample Input :
I am shrey 

Sample Output :
 m shry
'''

#Getting input via STDIN
userInput = input()

vowels = 'aeiou'
result = ""
for char in userInput:
  if char not in vowels and char not in vowels.upper():
    result = result+char
print(result)