'''
A person saves his monthly saving according to given schema. He saves same amount of money which is equal to the money saved in immediate previous two months. Assume, initially he saved 1000 rupees and in first month he saved another 1000. Your task is to tell how much he had totally saved at the end of ‘n’ months

Input Description:
You will be given a number ‘n’->No. of months

Output Description:
Print the total savings at the end of ‘n’ months

Sample Input :
1

Sample Output :
2000

'''

n = int(input())
initial_savings = 1000
total_savings = initial_savings
for i in range(1,n+1):
  last_savings=1000
  if(i%2==0):
    total_savings*=i
    last_savings = total_savings
  else:
    total_savings+=(i*last_savings)
print(total_savings)