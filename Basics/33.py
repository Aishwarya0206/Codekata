'''
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.For the given input string(S) and shift print the encrypted string.
Sample Testcase :
INPUT
ABCdEFGHIJKLMNOPQRSTUVWXYz 23
OUTPUT
XYZaBCDEFGHIJKLMNOPQRSTUVw
'''

n, shift = tuple(map(str, input().split()))
l = []
for i in n:
  c = chr(ord(i)+int(shift))
  if((c.isupper() and i.isupper()) or (c.islower() and i.islower())):
    l.append(c)
  else:
    l.append(chr(ord(i)-3))
print(''.join(l))