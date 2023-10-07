'''


Create a C application to get employee information for a reputed school and print the pay-slip of employees. Consider various possible roles in the school and perform the pay-slip generation.

Input Description:
The first line of the integer input N consists of the number of employees in the given school.

It will be followed by the details of the N employees in the N number of lines in the below format:
< employee id > < name > < role > < salary per hour > < working hours >

Output Description:
For all the N employees, generate the pay slip in the below format:
< employee id>
< name >
< role >
< salary for the current month >

Separate multiple user payslips using line break between them.

Note: The Salary is calculated by multiplying the working hours and salary per hour

Sample Input :
2
1 Raja Principal 1000 240
2 Rani Vice-Principal 900 250

Sample Output :
1
Raja
Principal
240000

2
Rani
Vice-Principal
225000

'''
n = int(input())
dic = {}
for i in range(n):
  e_id, name, role, salary_hr, working_hr = tuple(map(str, input().strip().split()))
  dic[i] = [e_id, name, role, int(salary_hr), int(working_hr)]
for i, j in dic.items():
  j[3] = j[3]*j[4]
  j.remove(j[4])

for i, j in dic.items():
  for k in range(len(j)):
    print(j[k])
  print()