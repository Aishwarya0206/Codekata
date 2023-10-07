'''


you are given a string made up of parenthesis only.Your task is to check whether parenthesis are balanced or not.If they are balanced print 1 else print 0

Input Description:
You are given a string ‘s’

Output Description:
Print 1 for balanced and 0 for imbalanced

Sample Input :
{({})}

Sample Output :
1

'''

n = input()
s = [char for char in n]
even = len(s)//2
odd = (len(s)+1)//2
first = s[:even] if(len(s)%2 == 0) else s[:odd]
second = s[even:] if(len(s)%2 == 0) else s[odd:]
check = []
for i in range(len(first)):
  for j in range(len(second)):
    if(i==j and (first[i]=='{' and second[j] == '}') or (first[i]=='(' and second[j]==')') or (first[i]=='[' and second[j]==']')):
      check.append('1')

if(set(check) == set('1')):
  print(1)
else:
  print(0)