"""加密"""
def encrypt(strs):
    import random
    string=strs
    str_list=[]
    for i in string:
        str_list.append(int(ord(i)))
    key_list=[]
    for i in range(len(str_list)):
        
        key_list.append(random.randint(10,32))
    
    return_list=[]
    x_a_list=[]
    xa=0#*+
    for i in range(len(str_list)):
        xa=random.randint(0,1)#0==*,1==+
        if xa==0:
            return_list.append(str_list[i]*key_list[i])
            x_a_list.append(xa)
        else:
            return_list.append(str_list[i]+key_list[i])
            x_a_list.append(xa)
    return_list1=''
    for i in range(len(return_list)):
        return_list1=return_list1+chr(return_list[i])
    key_list1=''
    for i in key_list:
        key_list1=key_list1+chr(i)
    x_a_list1=''
    for i in x_a_list:
        x_a_list1=x_a_list1+chr(i)
    returns=return_list1+key_list1+x_a_list1+'n'
    return returns

