'''
Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range (inclusive of L and R ).
Input Size : L <= R <= 100000(complexity O(n) read about Sieve of Eratosthenes)
Sample Testcase :
INPUT
2 5
OUTPUT
3
'''

n, m = [int(z) for z in input().split()]
prime_count = 0
for i in range(n, m+1):
  if i == 0 or i == 1:
    continue
  else:
    for j in range(2, int(i/2)+1):
      if i % j == 0:
        break
    else:
      prime_count += 1
print(prime_count)