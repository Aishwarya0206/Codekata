'''
Given a string as input, you have to reverse the string by keeping the punctuation and spaces intact. You have to modify the source
string itself without creating another string.

Input Description:
1<=string length<=500

Output Description:
Print the string in reverse

Sample Input :
A man, in the boat says : I see 1-2-3 in the sky

Sample Output :
y kse, ht ni3 21ee sIsy : a sta o-b-e ht nin amA
'''

import string
s = input()
j = ''
p = []
o = []
for i in s:
  if((i.isspace() == True) or (i in string.punctuation)):
    o.append(i)
  else:
    p.append(i)
p = p[::-1]
for i in range(len(s)):
  if(s[i] in o):
    p.insert(i, s[i])
print(''.join(p))