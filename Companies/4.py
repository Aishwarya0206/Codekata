'''
Given a number N and an array of N strings,Print yes, if all strings have atleast one vowel in them otherwise print no.
Input Size : N <= 1000
Sample Testcase :
INPUT
5
code
overload
vishal
sundar
anish
OUTPUT
yes
'''

vowels = ['a', 'e', 'i', 'o', 'u']
n = int(input())
s = []
for i in range(n):
    s.append(input())
k = []
for i in s:
    for j in i:
        if(j in vowels):
            k.append(True)
            break
        else:
            k.append(False)
if(k.count(True)==n):
    print('yes')
else:
    print('no')