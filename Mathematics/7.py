'''
You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.

Input Description:
You are given with a number n.

Output Description:
Print Saturated if it is saturated else it is Unsaturated

Sample Input :
121

Sample Output :
Saturated
'''

userInput = [x for x in input()]
checkset = set(userInput)
if(len(checkset)==2):
    print("Saturated")
else:
    print("Unsaturated")