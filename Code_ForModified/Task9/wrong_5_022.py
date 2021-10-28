# Task 9: wrong_5_022  
# 错误原因：使用capitalize()方法会导致第一个字母变为大写，后面的所有字母都变成小写。但依照题意来说，非首字母如果是大写的话则不应该被更改为小写。
# 修改方法：对字符串p进行判断，将其修正后的结果拷入字符串ans中，返回ans。
def fun(input):  
    p=input  
    ans=""
    if p[0].isupper()==False :
        ans+=p[0].upper()
        ans+=p[1:]
    else:
        ans+=p
    return(ans)  

# 获取输入数值时的代码段
# 输入格式："konjac"
str1=eval(input())
print(fun(str1))
# wrong_5_022 end
