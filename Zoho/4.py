'''
You are provided with a string ‘s’. Your task is to reverse the string using stack Data Structure.

 

Input Description:
You are given a string ‘s’.

Output Description:
Print the reverse string

Sample Input :
i am jsb

Sample Output :
jsb am i
'''

userInput = input().split(' ')
s = [userInput[i] for i in range(-1, -(len(userInput)+1), -1)]
print(' '.join(s))