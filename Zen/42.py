'''


Given a string remove the vowels in the string

Input Description:
Given a string

Output Description:
Print the string

Sample Input :
guvi geek

Sample Output :
gv gk

'''
vowels = ['a', 'e', 'i', 'o', 'u']
n = input()
s = ''
for j in n:
  if(j not in vowels):
    s+=j

print(s)