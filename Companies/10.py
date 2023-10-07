'''
Given a string and a number K, change every kth character to uppercase from beginning in string.
Sample Testcase :
INPUT
string 2
OUTPUT
sTrInG
'''

s, k = tuple(map(str, input().split()))
p = [i for i in s]
for i in range(len(s)):
    if(i%int(k)!=0):
        p[i] = p[i].capitalize()
    else:
        p[i] = p[i]

print(''.join(p))