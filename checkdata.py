from requestdate import do_reqd
from getexcel import Excel
from seleweb import WebReq
from timechange import do_chage

path1 = r'C:\Users\v_yupengliu\Desktop\checkdata.xlsx'
# 获取合并前的数据
def get_before_136(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，如果有数据此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_andriod_136(uin,id)
            if count_t is None:
                Excel(path).write_excel(flag,3,0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag,3,count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1],count_t[2])
                    Excel(path).write_excel(flag, 3, dat)

def get_before_263(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_ios_263(uin,id)
            if count_t is None:
                Excel(path).write_excel(flag,4,0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 4, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1],count_t[2])
                    Excel(path).write_excel(flag, 4, dat)


def get_before_64(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_andriod_64(uin,id)
            if count_t is None:
                Excel(path).write_excel(flag,5,0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 5, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 5, dat)

# 通过页面请求
def web_get_brfore_136(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
        # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin,136)
            else:
                count_t = WebReq().get_things_count(uin,136,id)
            if count_t is 0:
                Excel(path).write_excel(flag, 3, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 3, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 3, dat)

def web_get_brfore_263(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin,263)
            else:
                count_t = WebReq().get_things_count(uin,263,id)
            if count_t is 0:
                Excel(path).write_excel(flag, 4, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 4, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 4, dat)

def web_get_brfore_64(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin,64)
            else:
                count_t = WebReq().get_things_count(uin,64,id)
            if count_t is 0:
                Excel(path).write_excel(flag, 5, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 5, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 5, dat)


# 获取合并后的数据
def get_after_136(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，如果有数据此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_andriod_136(uin, id)
            if count_t is None:
                Excel(path).write_excel(flag, 6, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 6, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 6, dat)

def get_after_263(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_ios_263(uin, id)
            if count_t is None:
                Excel(path).write_excel(flag, 7, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 7, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 7, dat)

def get_after_64(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据，此时返回的是一个元组，没数据返回none
            # 第一个值为count，第二个值为ft,第三个值为vt
            count_t = do_reqd.getthingcount_andriod_64(uin, id)
            if count_t is None:
                Excel(path).write_excel(flag, 8, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 8, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 8, dat)

# 通过页面请求
def web_get_after_136(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin,136)
            else:
                count_t = WebReq().get_things_count(uin,136,id)
            if count_t is 0:
                Excel(path).write_excel(flag, 6, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 6, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 6, dat)


def web_get_after_263(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin, 263)
            else:
                count_t = WebReq().get_things_count(uin, 263, id)
            if count_t is 0:
                Excel(path).write_excel(flag, 7, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 7, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 7, dat)

def web_get_after_64(uin):
    path = path1
    a = Excel(path).get_excel()
    print(a)
    flag = 1
    for i in a:
        flag += 1
        id = i.get('物品ID')
        if id is None:
            pass
        else:
            # 获取数据
            if id == 40000001:
                count_t = WebReq().get_douzi(uin,64)
            else:
                count_t = WebReq().get_things_count(uin,64,id)
            if count_t is 0:
                Excel(path).write_excel(flag, 8, 0)
            else:
                if count_t[1] is None:
                    Excel(path).write_excel(flag, 8, count_t[0])
                else:
                    dat = do_chage.chagetime(count_t[1], count_t[2])
                    Excel(path).write_excel(flag, 8, dat)

def get_before(uin):
    get_before_136(uin)
    get_before_64(uin)
    get_before_263(uin)

def get_after(uin):
    do_reqd.change_info_ios(uin)
    get_after_64(uin)
    get_after_136(uin)
    get_after_263(uin)

def web_before(uin):
    web_get_brfore_64(uin)
    web_get_brfore_136(uin)
    web_get_brfore_263(uin)

def web_after(uin):
    do_reqd.change_info_ios(uin)
    web_get_after_64(uin)
    web_get_after_136(uin)
    web_get_after_263(uin)

if __name__ == '__main__':
    #get_before_136(1843671502)
    web_before(1843671502)