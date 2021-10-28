# Task 5: wrong_5_002
# 错误原因：原第6行、现第8行的if条件中漏掉了n[i]=='y'的判定。
# 修改方案：对现第8行的if条件进行修改，加入n[i]=='y'的判定。
def fun(input):
    n=input.lower()
    res=''
    for i in range(len(n)):
        if(n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='o' or n[i]=='u' or n[i]=='y'):
            continue
        else:
            res=res+n[i]
    k='.'
    for i in range(len(res)):
        m='.'
        if(i==0):
            k=k+res[i]
        else:
            k=k+m+res[i]
    return(k)

# 获取输入数值时的代码段
str1=input()
print(fun(str1))
