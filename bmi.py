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

#elif weight / (height ** 2) >= 18.5 and < 24
#	print('體重正常')

#if age < 13:
#	print('目前念國小')
#elif age >= 13 and age < 18:
#	print('目前唸國中')
#elif age >= 18 and age < 23:
#	print('目前還是大學生吧！')
#elif age >= 75:
#	print('您退休了吧？')
#else:
#	print('現在您應該是社會人士囉！')