'''


Given a two string print the common characters if their no common characters print -1

Input Description:
Given a two strings in one by one line

Output Description:
Print number of special characters or -1

Sample Input :
Guvi Geek
Guvi

Sample Output :
Guvi

'''
s1 = input()
s2 = input()
s = []
for i in s2:
    if(i in s1):
        s.append(i)
if(len(s)>0):
    print(''.join(s))
else:
    print(-1)