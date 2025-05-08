def nencrypt(string,magic='ytsidleyyds'):
    import random,encrypt,onezero
    # magic='ytsidleyyds'
    newadd=""
    xvlie=[]
    for i in range(len(magic)):
        t=random.randint(0,100)
        while (chr(t)=='\n'):
            t = random.randint(0, 100)
        newadd+=chr(ord(magic[i])+t)
        xvlie.append(t)
    strs=list(string)

    for i in range(len(xvlie)):
        if (i<len(string)):
            strs[i]=(chr(ord(string[i])+xvlie[i]))
    strss=""
    for i in strs:
        strss+=i
    # print(strss)
    fe=strss+newadd

    re=encrypt.encrypt(fe)
    out=''
    #third encrypt
    for item in re:
        out+=onezero.to_bin(ord(item))
    return out
def ndecrypt(string,magic='ytsidleyyds'):
    try:
        import decrypt,onezero
        t=''
        out=''
        for item in string:
            t+=item
            if len(t)==50:
                out+=chr(onezero.bin2dec(t))
                t=''
        string=out
        # print(string,2)
        sec=decrypt.decrypt(string)
        # sec=string
        getkey1=sec[-(len(magic)):]
        xvlie=[]
        for i in range(len(getkey1)):
            xvlie.append(ord(getkey1[i])-ord(magic[i]))
        # print(xvlie)
        # print(getkey1)
        strs=list(sec[:-(len(magic))])
        # print(strs)
        for  i in range(len(xvlie)):
            if (i < (len(sec)-len(magic))):
                strs[i]=(chr(ord(sec[i]) - xvlie[i]))
        strss=""
        for i in strs:
            strss+=i
        return strss
    except Exception as e:
        print("error,passwd error or other error!!!",e)
        return -1
# print(ndecrypt(nencrypt("赖宸铭",'1'),'21'))
# a=nencrypt("123")
# print(a)
# b=ndecrypt(a)
# print(b)