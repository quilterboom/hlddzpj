import requests
import re
import json


class Req_Da:

    # 发钻石
    def zhuanshi(self,uin):
        url = 'http://100.97.150.137/cgi-bin/ddz2/Tool_MacroTool?uin={}&lotus=lotus'.format(uin)
        data = {
            'cmd': 1,
            'uin': uin,
            'accounttype': 1,
            'clienttype': 64,
            'gameid': 260,
            'mailid': 2017022201,
            'richtext': 0,
            'lotus':'lotus'
        }
        Request_url = requests.post(url,data=data)
        print(Request_url)

    # 内网将老号变成新号-ios
    def change_info_ios(self,uin,accounttype,key0=26007):
        url1 = "http://100.97.150.137/cgi-bin/ddz2/cube_tool?uin={}&lotus=lotus".format(uin)
        data = {'op': 1,
            'uin': uin,
            'accounttype': accounttype,
            'clienttype': 263,
            'gameid': 260,
            'cubeid': 3000051,
            'keyCount': 2,
            'key0': key0,
            'key1': 0,
            'ftype': 0,
            'fid': 6,
            'fvalue': 0,
            'lotus': 'lotus'
            }
        Request_url = requests.post(url1, data=data)
        if 'update OK' in Request_url.text:
            print('ok 1')
        print(Request_url.text)

        url2 = 'http://100.97.150.137/cgi-bin/ddz2/change_PlayerInfo?uin={}&lotus=lotus'.format(uin)
        data2 = {'gender': -1,
                'level': -1,
                'exp': -1,
                'tot': -1,
                'uin': uin,
                'accounttype': accounttype,
                'clienttype': 263,
                'gameid': 260,
                'cmd': 1,
                'win': -1,
                'lose': -1,
                'title': 0,
                'medal': 0,
                'cur_season_best_title': 0,
                'title_season': -1,
                'title_rank_score': -1,
                'punish_flag': -1,
                'punish_end_time': -1,
                'max_cwin_times': -1,
                'lotus': 'lotus'
                }
        Request_url2 = requests.post(url2, data=data2)
        if len(Request_url2.text) == 49:
            print('ok 2')
        print(Request_url2.text)

        url3 = 'http://100.97.150.137/cgi-bin/ddz2/cube_tool?uin={}&lotus=lotus'.format(uin)
        data = {'op': 0,
                'uin': uin,
                'accounttype': accounttype,
                'clienttype': 263,
                'gameid': 260,
                'cubeid': 3000071,
                'keyCount': 2,
                'key0': 260,
                'key1': 3,
                'lotus': 'lotus'
                }
        Request_url3 = requests.post(url3, data=data)
        if 'delete OK' or 'delete failed' in Request_url3.text:
            print('ok 3')
        print(Request_url3.text)

    # 内网将老号变成新号-Android
    def change_info(self,uin,accounttype,key0=26007):
        url1 = "http://100.97.150.137/cgi-bin/ddz2/cube_tool?uin={}&lotus=lotus".format(uin)
        data = {'op': 1,
                'uin': uin,
                'accounttype': accounttype,
                'clienttype': 64,
                'gameid': 260,
                'cubeid': 3000051,
                'keyCount': 2,
                'key0': key0,
                'key1': 0,
                'ftype': 0,
                'fid': 6,
                'fvalue': 0,
                'lotus': 'lotus'
                }
        Request_url = requests.post(url1, data=data)
        if 'update OK' in Request_url.text:
            print('ok 1')
        print(Request_url.text)

        url2 = 'http://100.97.150.137/cgi-bin/ddz2/change_PlayerInfo?uin={}&lotus=lotus'.format(uin)
        data2 = {'gender':-1,
                'level': -1,
                'exp': -1,
                'tot': -1,
                'uin': uin,
                'accounttype': accounttype,
                'clienttype': 64,
                'gameid': 260,
                'cmd': 1,
                'win': -1,
                'lose': -1,
                'title': 0,
                'medal': 0,
                'cur_season_best_title': 0,
                'title_season': -1,
                'title_rank_score': -1,
                'punish_flag': -1,
                'punish_end_time': -1,
                'max_cwin_times': -1,
                'lotus': 'lotus'
                }
        Request_url2 = requests.post(url2,data=data2)
        if len(Request_url2.text) == 49:
            print('ok 2')
        print(Request_url2.text)

        url3 = 'http://100.97.150.137/cgi-bin/ddz2/cube_tool?uin={}&lotus=lotus'.format(uin)
        data = {'op':0,
                'uin': uin,
                'accounttype': accounttype,
                'clienttype': 64,
                'gameid': 260,
                'cubeid': 3000071,
                'keyCount': 2,
                'key0': 260,
                'key1': 3,
                'lotus': 'lotus'
                }
        Request_url3 = requests.post(url3,data=data)
        if 'delete OK' or 'delete failed' in Request_url3.text:
            print('ok 3')
        print(Request_url3.text)

    def pushgcm(self,uin,accounttype,realpushts,expectpushts,subid=1,subseq=-1,subts=-1,subcnt=-1,clienttype=64):
        """
        为负数时仅查询
        :param uin:
        :param realpushts:实际推送时间
        :param expectpushts: 计划推送时间
        :param clienttype:
        :return:
        """
        #修改推送时间
        url = 'http://100.97.150.137/cgi-bin/ddz2/pushgcm_tool?uin={}&lotus=lotus'.format(uin)
        data = {
            "uin": uin,
            "accounttype": accounttype,
            "clienttype":clienttype,
            "gameid": 260,
            "subid": subid,
            "subseq": subseq,
            "subts": subts,
            "subcnt": subcnt,
            "realpushts": realpushts,
            "expectpushts": expectpushts,
            "lotus": "lotus"
        }
        res = requests.post(url,data)
        print(res.text)

    # 20200108更新，删除cude记录
    def change_qqinfo_by_clear_cudeinfo(self,uin,accout=4):

        url2 = 'http://100.97.150.137/cgi-bin/ddz2/cube_tool?' \
               'uin={}&' \
               'lotus=lotus&' \
               'uin={}&' \
               'accounttype={}&' \
               'clienttype=136&' \
               'gameid=260&' \
               'cubeid=3000051&' \
               'keyCount=2&' \
               'key0=26010'.format(uin, uin, accout)
        data2 = {
            'op': 0,
            'uin': uin,
            'accounttype': accout,
            'clienttype': 136,
            'gameid': 260,
            'cubeid': 3000051,
            'keyCount': 2,
            'key0': 26010,
            'key1': 0,
            'lotus': 'lotus'
        }

        b = requests.post(url2, data2)
        print(b.text)

        url = 'http://100.97.150.137/cgi-bin/ddz2/cube_tool?' \
              'uin=1958200380&' \
              'lotus=lotus&' \
              'uin={}&' \
              'accounttype={}&' \
              'clienttype=136&' \
              'gameid=260&' \
              'cubeid=3000071&' \
              'keyCount=2&' \
              'key0=260&' \
              'key1=8'.format(uin,accout)
        data = {
            'op': 0,
            'uin': uin,
            'accounttype': accout,
            'clienttype': 136,
            'gameid': 260,
            'cubeid': 3000071,
            'keyCount': 2,
            'key0': 260,
            'key1': 8,
            'lotus': 'lotus'
        }

        a = requests.post(url,data)
        print(a.text)



    def newpackdata(self,uin,accounttype=1,clienttype=64,key0=26007,fid=6,fvalue=0):
        """
        :param uin:
        :param accounttype 1:WeChat  4:QQGameUin  2:OpenIDQQ
        :param clienttype: 64:Android  13:IOS  32:PC  Android-小程序:136  IOS-小程序:263
        :param key0:玩一玩第一个主键是26009 小游戏是26007
        :param fid:
        :param fvalue:
        FiledIndex和FiledVaule是对应关系，FiledIndex=6，FiledVaule是领了第几天；FiledIndex=10，FiledVaule是领奖的时间戳
        :return:
        """
        # 初始化新人礼包天数
        url = "http://100.97.150.137/cgi-bin/ddz2/cube_tool?uin={}&lotus=lotus".format(uin)
        data = {
            "op":1,
            "uin":uin,
            "accounttype":accounttype,
            "clienttype":clienttype,
            "gameid": 260,
            "cubeid": 3000051,
            "keyCount": 2,
            "key0": key0,
            "key1": 0,
            "ftype": 0,
            "fid": fid,
            "fvalue": fvalue,
            "lotus": "lotus"
        }
        res = requests.post(url,data)
        print(res.text)
        print(eval(res.text)['resultstr'])



    # 发放物品
    def things(self,uin,num):
        url = 'http://100.97.150.137/cgi-bin/ddz2/express_item?uin={}&lotus=lotus'.format(uin)
        data = {
            'itemtype': 3,
            'itemseq':0,
            'uin': uin,
            'accounttype': 4,
            'clienttype': 32,
            'gameid': 260,
            'id':num,
            'count':1,
            'lotus': 'lotus'
        }
        Request_url = requests.post(url, data=data)
        print(Request_url)

    # 查询新人红包任务状态
    def findmissin(self,uin,missionID):
        url = r'http://100.97.150.137/cgi-bin/tools/mission_tool?' \
              r'callback=jQuery191042089042208649574_1564711056546&' \
              r'inputuin={}&gameid=260&' \
              r'clienttype=136&' \
              r'sceneid=3260&' \
              r'missionid={}&' \
              r'optype=8&' \
              r'cgiLotusIP=10.209.1.99&' \
              r'cgiLotusPort=24558&_=1564711056577'.format(uin,missionID)
        res = requests.get(url)
        print(res.text)
        r_res = re.sub('\)', '', re.sub('jQuery191042089042208649574_1564711056546\(', '', res.text))
        print(json.loads(r_res))

    # 放弃新人红包任务
    def dealmissin(self,uin,missionid):
        url = r'http://100.97.150.137/cgi-bin/tools/mission_tool?' \
              r'callback=jQuery191042089042208649574_1564711056546&' \
              r'inputuin={}&gameid=260&clienttype=136&' \
              r'sceneid=3260&' \
              r'missionid={}&' \
              r'optype=8&' \
              r'cgiLotusIP=10.209.1.99&' \
              r'cgiLotusPort=24558&_=1564711056577'.format(uin,missionid)
        res = requests.get(url)
        r_res = re.sub('\)', '', re.sub('jQuery191042089042208649574_1564711056546\(', '', res.text))
        print(json.loads(r_res))

    # 领取新人红包任务
    def getmissin(self,uin,missionid):
        url = r'http://100.97.150.137/cgi-bin/tools/mission_tool?callback=jQuery191042089042208649574_1564711056546' \
              r'&inputuin={}' \
              r'&gameid=260' \
              r'&clienttype=136' \
              r'&sceneid=3260' \
              r'&missionid={}' \
              r'&optype=8' \
              r'&cgiLotusIP=10.209.1.99' \
              r'&cgiLotusPort=24558&_=1574822842490'.format(uin,missionid)
        res = requests.get(url)
        r_res = re.sub('\)', '', re.sub('jQuery191042089042208649574_1564711056546\(', '', res.text))
        print(json.loads(r_res))

    # 查询物品数量136
    def getthingcount_andriod_136(self,uin,thingid):
        if thingid == 40000001:
            a = do_reqd.getdouzi(uin,136)
            return a,None,None
        else:
            url = "http://100.97.150.137/cgi-bin/ddz2/get_item?" \
                  "uin={}&" \
                  "lotus=lotus&" \
                  "uin={}&" \
                  "accounttype=1&" \
                  "clienttype=136&" \
                  "gameid=260&" \
                  "id0={}".format(uin,uin,thingid)
            data = {'uin': uin,
                    'accounttype': 1,
                    'clienttype': 136,
                    'gameid': 260,
                    'id0': thingid,
                    'id1': 0,
                    'lotus': 'lotus'
                    }
            a = requests.post(url,data=data)
            try:
                # 数量
                c = eval(a.text).get('info')[0].get('count')
                # buytime
                bt = eval(a.text).get('info')[0].get('buy_time')
                # validtime
                vt = eval(a.text).get('info')[0].get('valid_time')
                # 如果vt为0，那么道具就是永久的，所以只要返回count。反之，道具是时效的，需要返回相应的数据进行计算
                if vt == 0:
                    return c,None,None
                else:
                    return c,int(bt),int(vt)
            except Exception as e:
                return None

    # 查询物品数量263
    def getthingcount_ios_263(self,uin, thingid):
        if thingid == 40000001:
            a = do_reqd.getdouzi(uin,263)
            return a,None,None
        else:
            url = "http://100.97.150.137/cgi-bin/ddz2/get_item?" \
                  "uin={}&" \
                  "lotus=lotus&" \
                  "uin={}&" \
                  "accounttype=1&" \
                  "clienttype=263&" \
                  "gameid=260&" \
                  "id0={}".format(uin, uin, thingid)
            data = {'uin': uin,
                    'accounttype': 1,
                    'clienttype': 263,
                    'gameid': 260,
                    'id0': thingid,
                    'id1': 0,
                    'lotus': 'lotus'
                    }
            a = requests.post(url, data=data)
            try:
                # 数量
                c = eval(a.text).get('info')[0].get('count')
                # buytime
                bt = eval(a.text).get('info')[0].get('buy_time')
                # validtime
                vt = eval(a.text).get('info')[0].get('valid_time')
                # 如果vt为0，那么道具就是永久的，所以只要返回count。反之，道具是时效的，需要返回相应的数据进行计算
                if vt == 0:
                    return c, None, None
                else:
                    return c, int(bt), int(vt)
            except Exception as e:
                return None

    def getthingcount_andriod_64(self,uin, thingid):
        if thingid == 40000001:
            a = do_reqd.getdouzi(uin,64)
            return a,None,None
        else:
            url = "http://100.97.150.137/cgi-bin/ddz2/get_item?" \
                  "uin={}&" \
                  "lotus=lotus&" \
                  "uin={}&" \
                  "accounttype=1&" \
                  "clienttype=64&" \
                  "gameid=260&" \
                  "id0={}".format(uin, uin, thingid)
            data = {'uin': uin,
                    'accounttype': 1,
                    'clienttype': 64,
                    'gameid': 260,
                    'id0': thingid,
                    'id1': 0,
                    'lotus': 'lotus'
                    }
            a = requests.post(url, data=data)
            try:
                # 数量
                c = eval(a.text).get('info')[0].get('count')
                # buytime
                bt = eval(a.text).get('info')[0].get('buy_time')
                # validtime
                vt = eval(a.text).get('info')[0].get('valid_time')
                # 如果vt为0，那么道具就是永久的，所以只要返回count。反之，道具是时效的，需要返回相应的数据进行计算
                if vt == 0:
                    return c, None, None
                else:
                    return c, int(bt), int(vt)
            except Exception as e:
                return None

    # 查询豆子
    def getdouzi(self,uin,client):
        url = 'http://100.97.150.137/cgi-bin/ddz2/express_item?' \
              'uin={}&' \
              'lotus=lotus&' \
              'itemtype=4&' \
              'id=40000001&' \
              'uin={}&' \
              'accounttype=1&' \
              'clienttype={}&' \
              'gameid=260'.format(uin,uin,client)

        data = {
            'itemtype': 4,
            'id': 40000001,
            'count': 0,
            'uin': uin,
            'accounttype': 1,
            'clienttype': client,
            'gameid': 260,
            'lotus': 'lotus'
        }

        a = requests.post(url,data=data)
        if len(eval(a.text).get('Item')) == 0:
            return '查不到数据'
        else:
            return eval(a.text).get('Item')[0].get('Count')

    # 清除合并标记
    def clearbj(self,uin):
        url = 'http://100.97.150.137/cgi-bin/ddz2/TcaplusLimitTool?' \
              'uin={}&' \
              'lotus=lotus&' \
              'Key1=2609999&' \
              'uin={}&' \
              'accounttype=1&' \
              'clienttype=263&' \
              'gameid=260&' \
              'cmd=1'.format(uin,uin)
        data = {
            'Key1': 2609999,
            'uin': uin,
            'accounttype': 1,
            'clienttype': 64,
            'gameid': 260,
            'cmd': 1,
            'lotus': 'lotus'
        }

        requests.post(url,data)
        print('清除标记')

class PlayTree:
    # 清空种树记录
    def clear_user_tree_andriod(self,uin):
        self.head = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
        }
        self.url = 'http://100.97.150.137/cgi-bin/ddz2/plantTree_tool?uin={}&' \
                   'lotus=lotus&uin={}&' \
                   'accounttype=1' \
                   '&clienttype=136' \
                   '&gameid=260'.format(uin,uin)
        self.data = {
            "uin": uin,
            "lotus": "lotus",
            "accounttype": 1,
            "clienttype": 136,
            "gameid": 260,
        }
        a = requests.post(url=self.url,data=self.data,headers=self.head)
        #a = requests.get(self.url)
        if 0 == eval(a.text)['errorCode']:
            print('ok')
        else:
            print(f'错误码:{eval(a.text)["errorCode"]}')

    def clear_user_tree_ios(self,uin):
        self.url = 'http://100.97.150.137/cgi-bin/ddz2/plantTree_tool?uin={}&' \
                   'lotus=lotus&uin={}&' \
                   'accounttype=1' \
                   '&clienttype=263' \
                   '&gameid=260'.format(uin, uin)
        self.data = {
            "uin": uin,
            "lotus": "lotus",
            "uin": uin,
            "accounttype": 1,
            "clienttype": 263,
            "gameid": 260,
        }
        a = requests.post(url=self.url, data=self.data)
        # a = requests.get(self.url)
        if 0 == eval(a.text)['errorCode']:
            print('ok')
        else:
            print(f'错误码:{eval(a.text)["errorCode"]}')

    # 发果实
    def set_tree_count_andriod(self,uin,count):
        url = 'http://100.97.150.137/cgi-bin/ddz2/express_item?uin=1699251698&' \
              'lotus=lotus&' \
              'itemtype=3&' \
              'uin={}&' \
              'accounttype=1&' \
              'clienttype=136&' \
              'gameid=260&' \
              'id=35000079&' \
              'count={}'.format(uin,count)
        data = {
            "itemtype": 3,
            "itemseq": 0,
            "uin": uin,
            "accounttype": 1,
            "clienttype": 136,
            "gameid": 260,
            "id": 35000079,
            "count": count,
            "expressflag": 0,
            "lotus": "lotus"
        }

        a = requests.post(url=url,data=data)
        print(f'果实数:{eval(a.text)["Item"][0]["Count"]}')

    def set_tree_count_ios(self, uin, count):
        url = 'http://100.97.150.137/cgi-bin/ddz2/express_item?uin=1699251698&' \
              'lotus=lotus&' \
              'itemtype=3&' \
              'uin={}&' \
              'accounttype=1&' \
              'clienttype=263&' \
              'gameid=260&' \
              'id=35000079&' \
              'count={}'.format(uin, count)
        data = {
            "itemtype": 3,
            "itemseq": 0,
            "uin": uin,
            "accounttype": 1,
            "clienttype": 263,
            "gameid": 260,
            "id": 35000079,
            "count": count,
            "expressflag": 0,
            "lotus": "lotus"
        }

        a = requests.post(url=url, data=data)
        print(f'果实数:{eval(a.text)["Item"][0]["Count"]}')

do_reqd = Req_Da()
do_tree = PlayTree()

if __name__ == '__main__':
    Req_Da().change_qqinfo_by_clear_cudeinfo(1001498297)
    #findmissin(1870270008,1976)
    #dealmissin(1843671502,1976)
    #getmissin(1870270008,1976)
    #Req_Da.change_info(1010758683)
    #change_info_ios(1843671502)
    #uin = '814067292'
    #newpackdata(uin,clienttype=64,key0=26009,fid=6,fvalue=0)
    #newpackdata(uin,clienttype=64,key0=26009,fid=10,fvalue=0)
    #pushgcm(1620963203,0,0,3,0,0,0,64)
    #pushgcm(1843671502,1568105484,1568105484)
    #zhuanshi(1950849200)
    #things(1561043882, 32010038)
    # list = [32010014,32010015,32010016,32010017,32010018,32010019,32010020,32010021,32010022,32010031,32010032,32010034,32010036,32010038,32010040,32010041,32010045]
    # for i in list:
    #     things(1796753262,i)
    # PlayTree().clear_user_tree_ios(1939962121)
    # PlayTree().clear_user_tree_andriod(1843671502)
    # PlayTree().clear_user_tree_andriod(2279783642)
    #Req_Da.getthingcount_andriod_64(1381048589,30020007)
    # b = Req_Da.getdouzi(1010758683,263)
    # print(b)