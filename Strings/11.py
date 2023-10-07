'''
You are given a paragraph.Your task is to print the words that come just after articles.

Input Description:
You are given a string ‘s’

Output Description:
print the words that come just after articles and -1 if there are no articles

Sample Input :
The sun rises in the east

Sample Output :
sun east
'''

userInput = input().split()
articles = ['a', 'an', 'the']
result = [userInput[i+1] for i in range(len(userInput)) if userInput[i].lower() in articles]
print(' '.join(result))