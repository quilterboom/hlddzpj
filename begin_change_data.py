from seleweb import WebReq
from requestdate import do_reqd
import time

# 将老号变成新号
# 确认在手机上进行了清空用户操作
def clear_user_data_qq_andrion(uin):
    # 获取新人红包和新人教程任务
    WebReq().get_newteacher_andrion(uin)
    WebReq().get_newhongpage_andrion(uin)
    # 清空数据
    do_reqd.change_info(uin, accounttype=4,key0=26010)
    do_reqd.change_qqinfo_by_clear_cudeinfo(uin)
    do_reqd.newpackdata(uin,accounttype=4, clienttype=64, key0=26009, fid=6, fvalue=0)
    do_reqd.newpackdata(uin,accounttype=4, clienttype=64, key0=26009, fid=10, fvalue=0)

def clear_user_data_qq_ios(uin):
    # 获取新人红包和新人教程任务
    WebReq().get_newteacher_ios(uin)
    WebReq().get_newhongpage_ios(uin)
    # 清空数据
    do_reqd.change_info_ios(uin, accounttype=4,key0=26010)
    do_reqd.newpackdata(uin,accounttype=4, clienttype=263, key0=26009, fid=6, fvalue=0)
    do_reqd.newpackdata(uin,accounttype=4,clienttype=263, key0=26009, fid=10, fvalue=0)

def clear_user_data_andrion(uin):
    # 获取新人红包和新人教程任务
    WebReq().get_newteacher_andrion(uin)
    WebReq().get_newhongpage_andrion(uin)
    # 清空数据
    do_reqd.change_info(uin,accounttype=1)
    do_reqd.newpackdata(uin,clienttype=64,key0=26009,fid=6,fvalue=0)
    do_reqd.newpackdata(uin, clienttype=64, key0=26009, fid=10, fvalue=0)

def clear_user_data_ios(uin):
    # 获取新人红包和新人教程任务
    WebReq().get_newteacher_ios(uin)
    WebReq().get_newhongpage_ios(uin)
    # 清空数据
    do_reqd.change_info_ios(uin,accounttype=1)
    do_reqd.newpackdata(uin, clienttype=263, key0=26009, fid=6, fvalue=0)
    do_reqd.newpackdata(uin, clienttype=263, key0=26009, fid=10, fvalue=0)

if __name__ == '__main__':
    #clear_user_data_ios(1870270008)
    clear_user_data_andrion(1588506121)
    #clear_user_data_qq_andrion(2268090412)
