'''


Design a simple mathematical calculator using C.

Input Description:
The first line of the input consists of integer input C indicating the chosen calculation operation.

Below are details of the choices available.
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division

The second line of the input consists of two space-separated integer values N and M upon which the arithmetic operations are needed to be performed depending upon the chosen operation like below:
N + M
N - M
N x M
N / M

Output Description:
The output will be the result of the arithmetic operation.

Note: Round the Decimal values to two decimal places

Sample Input :
1
5 5

Sample Output :
10

'''

c = int(input())
if(c==1):
  N, M = tuple(map(int, input().strip().split()))
  print(round(N+M, 2))
elif(c==2):
  N, M = tuple(map(int, input().strip().split()))
  print(round(N-M, 2))
elif(c==3):
  N, M = tuple(map(int, input().strip().split()))
  print(round(N*M, 2))
elif(c==4):
  N, M = tuple(map(int, input().strip().split()))
  print(round(N/M, 2))