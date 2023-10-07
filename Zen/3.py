'''


 Given a number n followed by n numbers print the number which is greater than 15 if there is no number exits print -1

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print the number which is greater than 15 if there is no number exits print -1

Sample Input :
3
5 7 4

Sample Output :
-1

'''


n = int(input())
l = list(map(int, input().split(' ')))[:n]
get = [str(i) for i in l if(i>15)]
if(len(get)>0):
  print(' '.join(get))
else:
  print(-1)