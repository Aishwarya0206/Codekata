'''
Given a number N, print 'yes' if it is a multiple of 13 else print 'no'.
Sample Testcase :
INPUT
26
OUTPUT
yes
'''
#Getting input via STDIN
N = int(input())
print("yes" if(N%13==0) else "no")