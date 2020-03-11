from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webE import do_webe
import time


class WebReq:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout=5)

    # 打开页面操作
    def open_page(self,url='http://100.97.150.137/ddz2/mission.html'):
        self.driver.get(url)
     # 关闭页面
    def close_page(self):
        self.driver.quit()

    #获取新人教程的任务
    def get_newteacher_andrion(self,uin,yyhj='新斗地主终端测试环境99'):
        # 打开页面
        self.open_page()
        # 选择运营环境
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_yyhj)))
        se_hj.select_by_visible_text(yyhj)
        # 选择操作
        # 领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        # 定位元素并输入相关内容
        try:
            # 输入uin
            self.wait.until(ec.presence_of_element_located(do_webe.input_uin)).send_keys(uin)
            # 输入gameid
            g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid))
            g.clear()
            g.send_keys(260)
            # 输入clienttype
            c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype))
            c.clear()
            c.send_keys(136)
            # 输入sceneid
            s = self.wait.until(ec.presence_of_element_located(do_webe.input_sceneid))
            s.clear()
            s.send_keys(-1)
            # 输入领取界面的missionid
            m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
            m.clear()
            m.send_keys(2186)
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(f'没找到元素{e}')
        # 放弃任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('放弃任务')
        try:
            # 输入放弃界面的missionid
            m = self.wait.until(ec.presence_of_element_located(do_webe.cancel_input_missionID))
            m.clear()
            m.send_keys(2186)
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)

        # 再次领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        try:
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)

        # 关闭页面
        self.close_page()

    def get_newteacher_ios(self, uin, yyhj='新斗地主终端测试环境99'):
        # 打开页面
        self.open_page()
        # 选择运营环境
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_yyhj)))
        se_hj.select_by_visible_text(yyhj)
        # 选择操作
        # 领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        # 定位元素并输入相关内容
        try:
            # 输入uin
            self.wait.until(ec.presence_of_element_located(do_webe.input_uin)).send_keys(uin)
            # 输入gameid
            g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid))
            g.clear()
            g.send_keys(260)
            # 输入clienttype
            c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype))
            c.clear()
            c.send_keys(263)
            # 输入sceneid
            s = self.wait.until(ec.presence_of_element_located(do_webe.input_sceneid))
            s.clear()
            s.send_keys(-1)
            # 输入领取界面的missionid
            m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
            m.clear()
            m.send_keys(2186)
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(f'没找到元素{e}')
        # 放弃任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('放弃任务')
        try:
            # 输入放弃界面的missionid
            m = self.wait.until(ec.presence_of_element_located(do_webe.cancel_input_missionID))
            m.clear()
            m.send_keys(2186)
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)

        # 再次领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        try:
            # 点击执行
            self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)

        # 关闭页面
        self.close_page()

    # 获取新人红包的任务
    def get_newhongpage_andrion(self,uin,yyhj='新斗地主终端测试环境99'):
        # 打开页面
        self.open_page()
        # 选择运营环境
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_yyhj)))
        se_hj.select_by_visible_text(yyhj)
        # 选择操作
        # 领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        # 定位元素并输入相关内容
        try:
            # 输入uin
            self.wait.until(ec.presence_of_element_located(do_webe.input_uin)).send_keys(uin)
            # 输入gameid
            g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid))
            g.clear()
            g.send_keys(260)
            # 输入clienttype
            c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype))
            c.clear()
            c.send_keys(136)
            # 输入sceneid
            s = self.wait.until(ec.presence_of_element_located(do_webe.input_sceneid))
            s.clear()
            s.send_keys(3260)
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(f'没找到元素{e}')
        # 放弃任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('放弃任务')
        try:
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.cancel_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)
        # 再次领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        try:
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)
        # 关闭页面
        self.close_page()

    def get_newhongpage_ios(self,uin,yyhj='新斗地主终端测试环境99'):
        # 打开页面
        self.open_page()
        # 选择运营环境
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_yyhj)))
        se_hj.select_by_visible_text(yyhj)
        # 选择操作
        # 领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        # 定位元素并输入相关内容
        try:
            # 输入uin
            self.wait.until(ec.presence_of_element_located(do_webe.input_uin)).send_keys(uin)
            # 输入gameid
            g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid))
            g.clear()
            g.send_keys(260)
            # 输入clienttype
            c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype))
            c.clear()
            c.send_keys(263)
            # 输入sceneid
            s = self.wait.until(ec.presence_of_element_located(do_webe.input_sceneid))
            s.clear()
            s.send_keys(3260)
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(f'没找到元素{e}')
        # 放弃任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('放弃任务')
        try:
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.cancel_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)
        # 再次领取任务
        se_cz = Select(self.wait.until(ec.presence_of_element_located(do_webe.select_put_data)))
        se_cz.select_by_visible_text('领取任务')
        try:
            for i in [1976,1977,1978,1979]:
                # 输入领取界面的missionid
                m = self.wait.until(ec.presence_of_element_located(do_webe.accept_input_missionID))
                m.clear()
                m.send_keys(i)
                # 点击执行
                self.wait.until(ec.presence_of_element_located(do_webe.click_button)).click()
        except Exception as e:
            print(e)
        # 关闭页面
        self.close_page()

    # 获取道具数值
    def get_things_count(self,uin,clientt,thingid):
        self.open_page(url='http://100.97.150.137/ddz2/ddz2.html')
        # 点击OPtion下拉框
        se_op = Select(self.wait.until(ec.presence_of_element_located(do_webe.chance_button)))
        se_op.select_by_visible_text('3.查询物品')
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.find_hj)))
        #se_hj.select_by_visible_text('测试环境【斗地主】_99')
        se_hj.select_by_visible_text('外网环境【微信】')
        # uin
        u = self.wait.until(ec.presence_of_element_located(do_webe.input_uin_2))
        u.clear()
        u.send_keys(uin)
        # at
        a = self.wait.until(ec.presence_of_element_located(do_webe.input_accountype))
        a.clear()
        a.clear()
        a.send_keys(1)
        # clinettype
        c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype_2))
        c.clear()
        c.send_keys(clientt)
        # gameid
        g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid_2))
        g.clear()
        g.send_keys('260')
        # 物品id
        t = self.wait.until(ec.presence_of_element_located(do_webe.input_thingid1))
        t.clear()
        t.send_keys(str(thingid))
        # go
        self.wait.until(ec.presence_of_element_located(do_webe.go_button)).click()
        time.sleep(1)
        # 物品数值
        tit = self.driver.find_element(*do_webe.br).find_elements_by_tag_name('tr')
        j = tit[0].find_elements_by_tag_name('td')
        info = j[3].text
        info1 = eval(info).get('info')
        if len(info1) == 0:
            self.close_page()
            return 0
        else:
            self.close_page()
            if info1[0].get('valid_time') == 0:
                return info1[0].get('count'),None,None
            else:
                return info1[0].get('count'),info1[0].get('buy_time'),info1[0].get('valid_time')

    # 获取豆子数
    def get_douzi(self,uin,client):
        self.open_page(url='http://100.97.150.137/ddz2/ddz2.html')
        # 点击OPtion下拉框
        se_op = Select(self.wait.until(ec.presence_of_element_located(do_webe.chance_button)))
        se_op.select_by_visible_text('7.2查询欢乐豆')
        se_hj = Select(self.wait.until(ec.presence_of_element_located(do_webe.find_hj)))
        # se_hj.select_by_visible_text('测试环境【斗地主】_99')
        se_hj.select_by_visible_text('外网环境【微信】')
        # uin
        u = self.wait.until(ec.presence_of_element_located(do_webe.input_uin_2))
        u.clear()
        u.send_keys(uin)
        # at
        a = self.wait.until(ec.presence_of_element_located(do_webe.input_accountype))
        a.clear()
        a.clear()
        a.send_keys(1)
        # clinettype
        c = self.wait.until(ec.presence_of_element_located(do_webe.input_clienttype_2))
        c.clear()
        c.send_keys(client)
        # gameid
        g = self.wait.until(ec.presence_of_element_located(do_webe.input_gameid_2))
        g.clear()
        g.send_keys('260')
        # go
        self.wait.until(ec.presence_of_element_located(do_webe.go_button)).click()
        time.sleep(3)
        # 物品数值
        tit = self.driver.find_element(*do_webe.br).find_elements_by_tag_name('tr')
        j = tit[0].find_elements_by_tag_name('td')
        info = j[3].text
        info1 = eval(info).get('Item')
        if len(info1) == 0:
            self.close_page()
            return 0
        else:
            return info1[0].get('Count'),None,None


if __name__ == '__main__':
    # WebReq().get_newteacher_andrion(1843671502)
    # WebReq().get_newhongpage_andrion(1843671502)
    a = WebReq().get_douzi(1566180170,136)
    print(a)