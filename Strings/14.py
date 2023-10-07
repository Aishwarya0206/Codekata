'''


You are given a string ‘s’.Your task is to print the string in the order they are present and then sum of digits.

Input Description:
You are given a string ‘s’.

Output Description:
Print the string and then at last sum of all the digits

Sample Input :
AC30BD40

Sample Output :
ACBD7
'''

s = [i for i in input()]
a = []
c = 0
for i in s:
    if(i.isalpha()):
        a.append(i)
    if(i.isdigit()):
        c+=int(i)
print("".join(a)+str(c))