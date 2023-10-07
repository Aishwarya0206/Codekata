'''
You are given a string s.Your task is to remove all the adjacent duplicate character from string.Print the string formed out of it.

Input Description:
You are given a string ‘s’

Output Description:
Print the resultant string

Sample Input :
Geeksforgeek

Sample Output :
Gksforgk
'''
s = input()
s1 = s
p = []
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        p.append(s[i])
        p.append(s[i+1])
for i in s:
  if(i in p):
    s1 = s1.replace(i, '')
print(s1)