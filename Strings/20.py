'''
Indian PAN card issuing authority have found some fake PAN cards. They have hired you so that you can validate PAN card for them. Your task is to develop a suitable algorithm which could check if pan is valid or not

1)Pan must have uppercase letters only.

2)It must be of 10 character only

3)From index 1 to 5 all must be letters(A-Z),last index must be letter

4)Rest all must be integer Starting from 1

Input Description:
You are given a input string which indicates the PAN number

Output Description:
Print 'pan' if it is valid PAN number, else print 'not pan'

Sample Input :
HXTPS2142R

Sample Output :
pan
'''

pan = input()
s = []
if(len(pan) == 10 and pan[0:5].isalpha() and pan[-1].isalpha()):
  for i in pan:
    if((i.isnumeric() and int(i)>=1)):
      s.append('pan')
    elif(i.isalpha() and i.isupper()):
      s.append('pan')
    else:
      s.append('not pan')

  set1 = set(s)
  if('pan' in set1 and len(set1) == 1):
    print('pan')
  else:
    print('not pan')
else:
  print('not pan')