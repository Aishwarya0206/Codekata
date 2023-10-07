'''


Shreya is a brilliant girl. She likes to memorize the numbers. These numbers will be shown to her. As an examiner develop an algorithm to test her memory.

 

CONSTRAINTS

1<=Y,N,T<=1000

Input Description:
First line contains no. of test cases(Y). Next line contains a number N. Next line contains n space separated numbers Next line contains a number T denoting the number of questions asked from you regarding the given array. Next line contains T space separated numbers.

Output Description:
Print the occurrence of each number if present else “NOT PRESENT”

Sample Input :
10
1 1 1 2 2 2 3 8 9 7
5
1 2 3 0 5

Sample Output :
3 3 1 Not Present Not Present


'''

n = int(input())
values_n = [int(val) for val in input().split()[:n]]
t = int(input())
values_t = [int(val) for val in input().split()[:t]]
a = []
b = []
for i in values_t:
  c=0
  for j in values_n:
    if(i==j):
      c+=1
  a.append(c)
for k in a:
  [b.append(str(k)) if(k>0) else b.append("Not Present")]
print(" ".join(b))