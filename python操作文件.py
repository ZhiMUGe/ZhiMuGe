# # 练习题1 —— 全局替换程序：
# # 写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
# #   `python your_script.py old_str new_str filename`
# # 替换完毕后打印替换了多少处内容
#
# import sys
# # print('参数个数：', len(sys.argv))
# # print('他们是：', str(sys.argv))
#
# par = sys.argv  #从命令行 获取 用户输入的参数的列表
# path_list = sys.path #获取路径列表
# # 使用占 内存方式修改文件
# def replace_file(old_str,new_str,path_filename):
#     with open(path_filename,'r+',encoding='utf_8') as read_f:
#         info = ''
#         count = 0
#         for line in read_f:
#             # print(line,end='')
#             if old_str in line:
#                 new_info = line.replace(old_str, new_str)
#                 info += new_info
#                 count += 1
#             else:
#                 info += line
#         print('替换次数为%d' % count)
#         read_f.seek(0)  #使光标移动到文件开头
#         read_f.write(info)  #写入内容
#         read_f.truncate(read_f.tell()) # 删除掉光标当前位置 之后的内容！ 防止解码错误
# old_str = par[1]
# new_str = par[2]
# filename = '%s\%s' % (path_list[0],par[3])
# replace_file(old_str, new_str, filename)



# 练习题1 —— 全局替换程序：
# 写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
#   `python your_script.py old_str new_str filename`
# 替换完毕后打印替换了多少处内容

# import sys
# # print('参数个数：', len(sys.argv))
# # print('他们是：', str(sys.argv))
#
# par = sys.argv  #从命令行 获取 用户输入的参数的列表
# path_list = sys.path #获取路径列表
# # 使用占 内存方式修改文件
# def replace_file(old_str,new_str,path_filename):
#     with open(path_filename,'r+',encoding='utf_8') as read_f:
#         info = ''
#         count = 0
#         for line in read_f:
#             # print(line,end='')
#             if old_str in line:
#                 new_info = line.replace(old_str, new_str)
#                 info += new_info
#                 count += 1
#             else:
#                 info += line
#         print('替换次数为%d' % count)
#         read_f.seek(0)  #使光标移动到文件开头
#         read_f.write(info)  #写入内容
#         read_f.truncate(read_f.tell()) # 删除掉光标当前位置 之后的内容！ 防止解码错误
# old_str = par[1]
# new_str = par[2]
# filename = '%s\%s' % (path_list[0],par[3])
# replace_file(old_str, new_str, filename)



# f = open("info","r+",encoding='utf-8')
# info = {}
# i = 0
# while True:
#
#     account = input("请输入你的账号：")
#     if account in info:
#         i += 1
#         code = input("请输入你的密码：")
#         if code != info[account]:
#             if i == 3:
#                 print("账号已被锁定")
#                 del info[account]
#                 break
#     else:
#         code = input("设置密码：")
#         info[account] = code
#         break
# f.write(str(info))
# print(f.read())



user_name = 'alex'
password = 123
user_info = {}
count = 0
f = open('saa.txt', 'r+', encoding='utf-8')
file = f.read()
f.close()
print('请登陆'.center(30, '*'))
while count < 3:
    key = input('请输入密码 : ')
    name = input('请输入用户名 : ')
    key = int(key)
    if name in file:
        print('你的用户被锁定了')
        break
    elif name not in file:
        if name == user_name and key == password:
            print('登陆成功'.center(30, '-'))
            f2 = open('saz.txt', 'w', encoding='utf-8')
            user_info[user_name] = password
            f2.write(str(user_info))
            f2.close()
            break
        else:
            print('用户名或密码错误，请再试%s次' % (2-count))
            count += 1
        if count == 3:
            print('你的账户已被锁定'.center(30, '*'))
            f = open('saa.txt', 'r+', encoding='utf-8')
            file = f.write(name)
            f.close()
