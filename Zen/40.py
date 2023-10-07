'''


Given a string convert string into camel case

Input Description:
Given a string

Output Description:
Print string into camel case

Sample Input :
guvi geek

Sample Output :
guviGeek

'''


n = [i for i in input().split()]
s = []
for i in range(len(n)):
  if(i!=0):
    s.append(n[i].capitalize())
  else:
    s.append(n[i])
print(''.join(s))