'''


You are given a string ‘s’. Your task is to tell whether string is beautiful or not.A beautiful string is a string in which String starts with ‘a’ or ‘A’ and middle element is either ‘m’ or ‘M’ and last element is ‘z’or ‘Z’

 

Input Description:
You are given a string ‘s’.

Output Description:
Print 1 if string is beautiful and 0 if it is not

Sample Input :
Amz

Sample Output :
1

'''

s = input()
if((s[0]=='A' or s[0]=='a') and (s[len(s)//2]=='m' or s[len(s)//2]=='M') and (s[-1]=='z' or s[-1]=='Z')):
    print(1)
else:
  print(0)