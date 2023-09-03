'''
Given a string S consisting of 2 words reverse the order of two words .
Input Size : |S| <= 10000000
Sample Testcase :
INPUT
hello world
OUTPUT
world hello
'''

#Getting input via STDIN
userInput = [i for i in input().strip().split()]
t = []
for i in userInput[::-1]:
    t.append(i)
print(' '.join(t))