# Task 10 : wrong_5_020
# 修改后的版本（含注释），具体的错误原因and修改方案在提交的Word文档中。
def fun(input1,input2):
    # ret置空，stones接收input1，colors接受input2
	ret=""
	stones = int(input1)
	colors = str(input2).upper()
	# colors_list用于存储石头颜色，初始为R、G、B三色
	colors_list = ['R', 'G', 'B']
	# 遍历input2中的输入字符串，第一遍扫描石头颜色
	for c in colors:
	    # 如果当前石头颜色没有存进color_list中，则将其添加在ret里
		if c not in colors_list:
			ret+=(c)
		else:
			continue 
	# 如果石头数>50，则给ret+石头数
	if stones > 50:
		ret+=(stones) 
	# 如果手串长度！=石头数，则给ret+手串长度	
	if len(colors) != stones:
		ret+=(str(len(colors))) 
	# ret+石头数+手串颜色字符串
	ret+=("stones: colors: "+str(stones)+str(colors)) 
	# 用于计数的count初始化为0
	count = 0
	# 设i=0~len-1，用于遍历手串颜色字符串
	for i in range(len(colors) -1):
        # 如果手串当前石头颜色==下一个石头颜色，则说明应该去掉当前石头
		if colors[i] == colors[i+1]:
			count += 1
		else:
			continue        
    # ret+最小的石头数
	ret+=("minimum stones: "+str(count))
	# 返回答案count
	return count

# 用于输入数值
input1=input()
input2=eval(input())
#print(input1)
#print(input2)
print(fun(input1,input2))
# wrong_5_020 end
