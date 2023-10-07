'''
Given a string 'S' print the sum of weight of the String. A weight of character is defined as the ASCII value of corresponding character.

Input Description:
You are given a string ‘s’

Output Description:
Print weight

Sample Input :
abc

Sample Output :
294
'''

#Getting input via STDIN
userInput = input()
ascii_list = [ord(i) for i in userInput]
print(sum(ascii_list))