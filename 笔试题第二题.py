import sys
key = input()
key = key.split(" ")
if len(key)!=2:
    print("输入格式错误")
    sys.exit()
else:
    k = int(key[1])
    str_ = key[0]

    str_new = str_
    for i in range(min(k,len(str_))):
        str_0 = str_[:i]
        str_1 = str_[i]
        str_2 = str_[i+1:]
        if str_1 in str_0:
            str_new = str_new[:i]+'-'+str_new[i+1:]
    for i in range(k,len(str_)):
        str_0 = str_[:i-k]
        str_1 = str_[i-k:i]
        str_2 = str_[i]
        str_3 = str_[i+1:]
        if str_2 in str_1:
                
            str_new = str_new[:i]+'-'+str_new[i+1:]
    result = str_new
print(result)