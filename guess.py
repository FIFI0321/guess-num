import random

r = random.randint(1,100)
while True:
	num = input ('請輸入數字: ')
	num = int (num)
	if num == r :
		print ('你猜對了!!')
		break
	elif num > r :
		print ('你猜錯了,數字要更小')
	elif num < r :
		print ('你猜錯了,數字要更大')

