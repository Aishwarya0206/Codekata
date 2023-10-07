'''
Given a number N, print yes if the number is a multiple of 7 else print no.
Sample Testcase :
INPUT
49
OUTPUT
yes
'''

#Getting input via STDIN
userInput = int(input())
print("yes" if(userInput%7==0) else "no")