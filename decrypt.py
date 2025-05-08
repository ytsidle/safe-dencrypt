def decrypt(strings):

    strs = strings
    str_list = []
    return_list = []
    key_list = []
    list1 = []
    x_a_list = []
    for i in strs:
        str_list.append(i)
    str_list.pop()

    for i in range(len(str_list)//3):            
        return_list.append(ord((str_list[i])))
    for i in range(len(str_list)//3):
        x_a_list.append(ord(str_list[(len(str_list)//3)*2+i]))
    for i in range(len(str_list)//3):
        key_list.append(ord(str_list[(len(str_list)//3)*1+i]))
    for i in range(len(return_list)):
        if x_a_list[i] == 0:
            list1.append(return_list[i]/key_list[i])
        else:
            list1.append(return_list[i]-key_list[i])
    txt = ''
    for i in list1:
        # print(int(i))
        txt = txt+chr(int(i))
    return txt

