'''
Rahul is given a task to manipulate a string, He hired you as a developer your task is to delete all the repeating characters and print the result left.

Input Description:
You are given a string ‘s’

Output Description:
Print the remaining string

Sample Input :
mississipie

Sample Output :
mpe
'''

#Getting input via STDIN
userInput = input()
get_remaining_list = [i for i in userInput if(userInput.count(i)==1)]
print(''.join(get_remaining_list))