'''


 You are given a string. You have to print “Wonder” if the string is wonderful and -1 if it is not. A wonderful string is a string,which is made up of exactly 3 different characters.

Input Description:
You are given a string

Output Description:
Print “Wonder” if it is wonderful and -1 if it is not

Sample Input :
aabbcc

Sample Output :
Wonder

'''

#Getting input via STDIN
userInput = input()
s = set([i for i in userInput])
print("Wonder") if(len(s)==3) else print(-1)