#密碼重試程式
#password = 'a123456'
#讓使用者重複輸入密碼
#最多輸入3次
#如果正確 印出"密碼正確!!!!!!"
#如果不正確 印出"密碼錯誤! 還有_次機會^^"

password = 'a123456'
i = 3 #剩餘機會
while i > 0 :
	pwd = input('輸入密碼: ')
	if pwd == password:
		print('密碼正確!!!!!!!!!')
		break #逃出迴圈
	else:
		i = i - 1
		print('密碼錯誤! 還有', i,'次機會')
		
			