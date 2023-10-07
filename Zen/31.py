'''


Given a number n followed by n numbers print the number less than 15 if there is no number exits print -1

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the number which is less than 15 if there is no number exits print -1

Sample Input :
3
5 7 4

Sample Output :
5 7 4

'''

n = int(input())
userInput = [int(i) for i in input().strip().split()][:n]
k = []
for i in userInput:
  if(i<15):
    k.append(str(i))
if(len(k)>0):
  print(' '.join(k))
else:
  print(-1)