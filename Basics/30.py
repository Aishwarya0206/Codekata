'''


Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.

Input Description:
A single line containing 2 integers separated by space.

Output Description:
Print the HCF of the integers.

Sample Input :
2 3

Sample Output :
1

'''

n, m = tuple(map(int, input().strip().split()))
factor_n = set([i for i in range(1, n+1) if(n%i == 0)])
factor_m = set([i for i in range(1, m+1) if(m%i == 0)])
inter = [i for i in factor_n.intersection(factor_m)]
print(max(inter))