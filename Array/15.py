'''


You are given a number with duplicate digits your task is to remove the immediate duplicate digits and print the result

Input Description:
You are given a long string of digits

Output Description:
Print the desired result print -1 if result length is 0

Sample Input :
1331

Sample Output :
11


'''

n = input()
s = [char for char in n]
for i in range(len(n)):
  for j in range(1,len(n)):
    if((i+1) == j and n[i] == n[j]):
      s.remove(n[i])
      s.remove(n[j])
print(''.join(s))