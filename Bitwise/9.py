'''
Print the position of first 1 from right to left, in binary representation of an Integer.
Sample Testcase :
INPUT
18
OUTPUT
2
'''
userInput = int(input())
number = [i for i in str(userInput)][::-1]
print(number.index('1')+1)