'''


Given a string print the duplicate in the string  if their no duplicate  print -1

Input Description:
Given a string

Output Description:
Print duplicate of the string or -1

Sample Input :
Guvi Geek

Sample Output :
Ge

'''

s = input()
l = []
for i in s:
    if((s.count(i)>1) and (i not in l)):
        l.append(i)
print(''.join(l))