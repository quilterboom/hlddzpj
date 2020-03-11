from selenium.webdriver.common.by import By

class WebEle:
    # 选择操作的按钮
    select_put_data = (By.XPATH,'//select[@id="optype"]')
    # 选择运营环境按钮
    select_yyhj = (By.XPATH,'//select[@id="cgilotus"]')
    # uin输入框
    input_uin = (By.XPATH,'//input[@id="uin"]')
    # gameid输入框
    input_gameid = (By.XPATH,'//input[@id="gameid"]')
    # clienttype输入框
    input_clienttype = (By.XPATH,'//input[@id="clientType"]')
    # sceneid输入框
    input_sceneid = (By.XPATH,'//input[@id="sceneID"]')
    # eventCount输入框
    input_eventCount = (By.XPATH, '//input[@id="eventCount"]')
    # 查询任务的missionID输入框
    enable_input_missionID = (By.XPATH, '//div[@id="divEnableMissionID"]/input[@class="missionID"]')
    # 手动完成的missionID输入框
    finish_input_missionID = (By.XPATH,'//div[@id="divEnableFinish"]/input[@class="missionID"]')
    # 领取任务的missionID输入框
    accept_input_missionID = (By.XPATH,'//div[@id="divAcceptMission"]/input[@class="missionID"]')
    # 放弃任务的missionID输入框
    cancel_input_missionID = (By.XPATH,'//div[@id="divCancelMission"]/input[@class="missionID"]')
    #执行按钮
    click_button = (By.XPATH,'//input[@type="button"]')

    # 100.97.150.137选择列表
    chance_button = (By.XPATH,'//select[@id="ddz2_module"]')
    # 选择环境
    find_hj = (By.XPATH,'//select[@id="ddz2_env"]')
    # uin输入框
    input_uin_2 = (By.XPATH,'//input[@id="input_common_uin"]')
    # accounttype输入框
    input_accountype = (By.XPATH,'//input[@id="input_common_accounttype"]')
    # clienytype 输入框
    input_clienttype_2 = (By.XPATH,'//input[@id="input_common_clienttype"]')
    # gameid输入框
    input_gameid_2 = (By.XPATH,'//input[@id="input_common_gameid"]')
    # 物品1ID输入框
    input_thingid1 = (By.XPATH,'//input[@id="input_custom_id0"]')
    # go按钮
    go_button = (By.XPATH,'//button[contains(text(),"GO")]')
    # br
    br = (By.XPATH,'//table[@id="historypara_table"]/tbody')

do_webe = WebEle()