'''


Design and develop a health application that computes the Body Mass Index (BMI) of the individuals given with height and weight of persons and suggest the diet plan.

Input Description:
The first line of the input consists of two space-separated integer values H and W indicating the height and weight of the person in centimeter and kilograms respectively.

Output Description:
The first line of the output should consist of the BMI value of the person.

where, BMI = Weight(in Kilogram) / (Height(in meter) * Height(in meter))

Note: Round the BMI decimal values up to one decimal places

The second line of the output should consist of the diet plan suggestion according to their BMI value as below.

19 - 25 = Maintain your Current Diet Plan
Below 19 = Follow a Calorie Surplus Diet Plan
Above 25 = Follow a Calorie Deficit Diet Plan

Sample Input :
188 107

Sample Output :
30.3
Follow a Calorie Deficit Diet Plan

'''

H, W = tuple(map(int, input().strip().split()))
H = H/100
BMI = round(W/ (H*H), 1)
print(BMI)
if(19<=BMI<=25):
  print("Maintain your Current Diet Plan")
elif(BMI<19):
  print("Follow a Calorie Surplus Diet Plan")
elif(BMI>25):
  print("Follow a Calorie Deficit Diet Plan")