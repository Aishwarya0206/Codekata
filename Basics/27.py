'''
Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
Input Size : |s| <= 10000000(complexity O(n))
Sample Testcase :
INPUT
codekata
OUTPUT
ocedakat
'''

a = input()

s = [i for i in a]

p = len(a) if(len(a)%2 == 0) else len(a)-1
for i in range(0, p, 2):
  t = s[i]
  s[i] = s[i+1]
  s[i+1] = t

print(''.join(s))