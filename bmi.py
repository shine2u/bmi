weight = input('請輸入體重（公斤）：')
weight = float(weight)
height = input('請輸入身高（公尺）：')
height = float(height)
bmi = weight / (height ** 2)


if bmi < 18.5:
	print('過輕')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
elif bmi >= 35:
	print('重度肥胖')
else:
	print('體重正常') 

