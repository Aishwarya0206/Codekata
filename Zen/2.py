'''


Given a number n followed by n numbers find whether it is odd or even

Input Description:
0<n<100 Given a number n Followed by n number in next line

Output Description:
Print whether odd or even

Sample Input :
3
5 7 4

Sample Output :
odd odd even

'''


n = int(input())
l = list(map(int, input().split(' ')))[:n]
odd_even = []
for i in l:
  if(i%2==0):
    odd_even.append('even')
  else:
    odd_even.append('odd')
print(' '.join(odd_even))