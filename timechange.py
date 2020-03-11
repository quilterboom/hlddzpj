import time
from datetime import datetime


class ChageTime:
    def chagetime(self,first,end):
        # 将时间戳转换成字符串格式
        # a = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(first))
        # # 将字符串格式的时间转换成datatime格式，便于运算
        # a1 = datetime.strptime(a,"%Y-%m-%d %H:%M:%S")
        a1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
        b = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(end))
        b1 = datetime.strptime(b,"%Y-%m-%d %H:%M:%S")
        # 进行运算
        c = b1-a1
        if int(c.seconds)/60 >= 60:
            c1 = '{}天{}小时'.format(c.days,int(c.seconds)/3600)
        else:
            c1 = '{}天{}分钟'.format(c.days,int(c.seconds)/60)
        return c1
        # if c >= 100 :
        #     return c/100
        # else:
        #     return c

do_chage = ChageTime()

if __name__ == '__main__':
    a = do_chage.chagetime(1576833597,1578038083)
    print(a)
    print(type(datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")))