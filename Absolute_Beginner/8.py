'''

You will be provided with a number. Print the number of days in the month corresponding to that number.

Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".

Input Description:
The input is in the form of a number.

Output Description:
Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

Sample Input :
8

Sample Output :
31

'''

x = int(input())
y,z,b = 30,31,28
if(x in range(1,8)):
  if(x==2):
    print(b)
  elif(x%2==0):
    print(y)
  else:
    print(z)
elif(x in range(8,13)):
  print(z if(x%2==0) else y)
else:
  print("Error")