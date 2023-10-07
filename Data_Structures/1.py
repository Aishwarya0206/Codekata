'''
Given 2 numbers a and B.Print the value of a!/b!.
Input Size : A,B <= 10000 and A-B <= 5
Sample Testcase :
INPUT
4 2
OUTPUT
12
'''

def fact(val):
  a = 1
  while val>0:
    a*=val
    val-=1
  return(a)

l = list(map(int, input().split(' ')))[:2]
a = fact(l[0])
b = fact(l[1])
print(a//b)