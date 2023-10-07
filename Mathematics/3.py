'''
boy rolls an unbiased die until he gets ‘1’. You are given a number n find the total sum of probability that he will get ‘1’ on or before nth trial.(Probability of getting 1 at 1 time + probability of getting 1 at 2 trial….+probability of getting 1 at nth trial)

 

Constraints

1<=n<=1000

Input Description:
You are given a number ‘n’.

Output Description:
Print two numbers denoting numerator and denominator

Sample Input :
1

Sample Output :
1 6
'''

from fractions import Fraction
n = int(input())
denom = 6**n
numer = 0
for i in range(1,n+1):
  for j in range(i+1):
    if(j==1):
      numer+=j
num, den = Fraction(numer, denom).numerator, Fraction(numer, denom).denominator
print(num, den)