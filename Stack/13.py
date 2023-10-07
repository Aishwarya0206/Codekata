'''


Given two strings S1 and S2. The task is to find if a string 'S2’' can be obtained by rotating another string 'S1’' by 2 places using Stack.

Input Description:
The first line of the input contains the string S1. The second line of the input contains the string S2

Output Description:
Print 1 if the string S2 can be obtained by rotating string S1 by two places else print 0.

Sample Input :
amazon
azonam

Sample Output :
1

'''

s1 = input()
s2 = input()
s1_l = [i for i in s1]
for i in range(len(s1_l)-2):
  t = s1_l[i]
  s1_l[i] = s1_l[i+2]
  s1_l[i+2] = t

if(s2 == ''.join(s1_l)):
  print(1)
else:
  print(0)