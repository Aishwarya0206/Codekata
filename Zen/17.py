'''


Given a number n print the three prime number which comes next to number n

Input Description:
0<n<100 Given a number n

Output Description:
print the three prime number which comes next to number n

Sample Input :
3

Sample Output :
5 7 11

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