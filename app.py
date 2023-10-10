height = int(input("Please input your height:"))
weight = int(input("Please input your weight:"))
bmi = weight / (height / 100) ** 2
print("your weight:"+str(weight))
print("your bmi:"+str(round(bmi,2)))
