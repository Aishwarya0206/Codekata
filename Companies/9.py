'''
Given a string S ,print the vowels first and then consonants in the same order as they have occurred in the string.
Input Size : N <= 10000
Sample Testcase :
INPUT
GuVI
OUTPUT
uIGV
'''

S = input()
vowels = 'aeiou'
vow = []
cons = []
for i in S:
    if((i in vowels) or (i in vowels.upper())):
        vow.append(i)
    else:
        cons.append(i)
        
for i in cons:
    vow.append(i)

print(''.join(vow))