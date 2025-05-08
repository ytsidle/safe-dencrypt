def to_bin(value):#十进制数据，二进制位宽
	num=50
	bin_chars = ""
	temp = value
	for i in range(num):
		bin_char = bin(temp % 2)[-1]
		temp = temp // 2
		bin_chars = bin_char + bin_chars
	return bin_chars.upper()#输出指定位宽的二进制字符串
def bin2dec(string_num): 
	
	while (string_num[0]=='0' and len(string_num)!=1):
		string_num=string_num[1:]
	return int(string_num, 2)  
# print(to_bin(99999999999999999999))
# out=''
# #third encrypt
# for item in "123":
#     out+=to_bin(ord(item))
# print(out)
# t=''
# outs=''
# for item in out:
#     t+=item
#     if len(t)==200:
#         outs+=chr(bin2dec(t))
#         t=''

# print(outs)