# -*- coding: utf-8 -*-
file_path=str(input("Set the path of the file to be formated : (C:/aaa/bbb/ccc.txt)"))
print("\nPrefix 'cookies_' will be added to the output file and '.txt' suffix too")
output_file=str(input("Name of the output file : (Amazon,Nike,...)"))
output_file="cookies_"+output_file+".txt"

cookie_str=""
with open(file_path, "r") as cookietoformat:
    for line in cookietoformat:
        cookie_str=cookie_str+line

cookietoformat.close()

cookie_str = cookie_str.replace('[','').replace(']','').replace(' ', '').replace('\t', '').replace('\n', '').replace('"sameSite":"unspecified"','"sameSite":"Lax"').replace('"sameSite":"lax"','"sameSite":"Lax"')
list_line=cookie_str.split("},")
len_list=len(list_line)

x=0
with open("E:/BIDOUILLE/Script/ClickBot/MyCookies/"+output_file, "w") as formated_cookies:
    for element in list_line:
        if x < len_list:
            element=element+"}\n"
            
        formated_cookies.write(element)
        x=x+1

formated_cookies.close()