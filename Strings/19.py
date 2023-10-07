'''


Joyal was given a sentence. His task is to delete the two words that comes together and print the sentence so that the words in the output sentence have distinct words compared to their adjacent words. If no words are present in the output sentence print -1

Input Description:
You are given input string 'S'

Output Description:
Print the all the words that are left in the string 's' so that the words in the output sentence have distinct words compared to their adjacent words. Print -1 if no words are left

Sample Input :
I am john cena cena john

Sample Output :
I am

'''
S = [i for i in input().split()]
a = []
for i in S:
    if((i not in a) and (S.count(i)==1)):
        a.append(i)
if(len(a)>0):
    print(' '.join(a))
else:
    print(-1)