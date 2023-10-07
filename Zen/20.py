'''
Given a number n,m and k separated by a space followed by n numbers print the numbers between this two numbers listed in a array if there is no number exits print -1

Input Description:
number n, m and k separated by a space 0<n<1000 0<m<1000 0<k<1000 m<k Given a number n Followed by n number in next line

Output Description:
print the numbers between this two numbers listed in a array if there is no number exits print -1

Sample Input :
3 5 8
5 7 4

Sample Output :
7
'''

n, m, k = tuple(map(int, input().strip().split()))
s = [int(i) for i in input().strip().split()][:n]
if(len(s)>=3):
  if((len(s)%2)!=0):
    print(s[(len(s)//2)])
  else:
    print(s[(len(s)//2)-1], s[(len(s)//2)])
else:
  print(-1)