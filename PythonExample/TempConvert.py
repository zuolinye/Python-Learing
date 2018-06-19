
#TempConvert.py

# 使用input函数从控制台获取一个信息，这个信息是由用户输入，用户输入后并保存与TemStr变量中
TempStr = input("请输入带有符号的温度值: ")

# 分支语句，判断用户输入的字符串的最后一个字符是否在列表F,f中
if TempStr[-1] in ['F', 'f']:
	# 使用eval函数对TempStr除去最后一位的其他位进行评估运算
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C', 'c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")


 