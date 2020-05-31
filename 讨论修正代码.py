info = {
     '张三0': {'age': 20, '电话': 5879960, '职位': '员工0', '工资': '5000'},
     '张三1': {'age': 21, '电话': 5879961, '职位': '员工1', '工资': '5001'},
     '张三2': {'age': 22, '电话': 5879962, '职位': '员工2', '工资': '5002'},
     '张三3': {'age': 23, '电话': 5879963, '职位': '员工3', '工资': '5003'},
     '张三4': {'age': 24, '电话': 5879964, '职位': '员工4', '工资': '5004'},
     '张三5': {'age': 25, '电话': 5879965, '职位': '员工5', '工资': '5005'},
     '张三6': {'age': 26, '电话': 5879966, '职位': '员工6', '工资': '5006'},
     '张三7': {'age': 27, '电话': 5879967, '职位': '员工7', '工资': '5007'},
     '张三8': {'age': 28, '电话': 5879968, '职位': '员工8', '工资': '5008'},
     '张三9': {'age': 29, '电话': 5879969, '职位': '员工9', '工资': '5009'},
 }


#
# x = input("请输入你要查找的人名")
# if x in info:
#     print(info[x])



print("输入查询方式，name or tel?")
search_way = input(">>> ")
if search_way == 'name':
    name = input("input name :")
    print(info.get(name, "输出错误，没找到这个人"))#没有这个key，就返回默认值
elif search_way == 'tel':
     tel = int(input("input tel: "))
     a = 'False' #先赋值a一个值，表示目前还未匹配到信息
     for i in info:
         # break
         # for v in info[i].items():
             # print(type(v))
             if info[i]['电话'] == tel : #两个条件需同时成立 
                 print("name: ", i, info[i])
                 a = 'True' #匹配到信息后，重新给a赋值
     if a != 'True': #判断是否匹配成功
         print("Wrong telphone number.")
else:
     print("inputing is wrong...")