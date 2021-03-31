# -*- coding: utf-8 -*-

'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


class Base_page:
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,*loc):
        '''重写find_element方法，显式等待'''
        try:
            WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def send_keys(self,value,*loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def swipeUp(self,t=500, n=1):
        '''向上滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self,t=500, n=1):
        '''向下滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self,t=500, n=1):
        '''向左滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.25
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)

    def swipRight(self,t=500, n=1):
        '''向右滑动屏幕'''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.25
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)
    '''以下是两种截图方式，暂时未使用，只用来保存在本地，无法在测试报告展示'''
    # def take_screenShot(self, name="takeShot"):
    #     '''
    #     method explain:获取当前屏幕的截图
    #     parameter explain：【name】 截图的名称
    #     Usage:
    #         device.take_screenShot(u"个人主页")   #实际截图保存的结果为：2018-01-13_17_10_58_个人主页.png
    #     '''
    #     day = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    #     fq = "..\\screenShots\\" + day
    #     # fq =os.getcwd()[:-4] +'screenShots\\'+day    根据获取的路径，然后截取路径保存到自己想存放的目录下
    #     tm = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    #     type = '.png'
    #     filename = ""
    #     if os.path.exists(fq):
    #         print(fq)
    #         filename = fq + "\\" + tm + "_" + name + type
    #     else:
    #         os.makedirs(fq)
    #         filename = fq + "\\" + tm + "_" + name + type
    #     # c = os.getcwd()
    #     # r"\\".join(c.split("\\"))     #此2行注销实现的功能为将路径中的\替换为\\
    #     self.driver.get_screenshot_as_file(filename)
    # def get_img(self):
    #     # self.logger = logging.getLogger(__name__)
    #     file_path = 'D:/python/pom_adv/report/screenshots/'
    #     rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    #     screen_name = file_path + rq + '.png'
    #     self.driver.get_screenshot_as_file(screen_name)
    #     # try:
    #     #     self.driver.get_screenshot_as_file(screen_name)
    #     #     # self.logger.info("Had take screenshot and save to folder : /screenshots")
    #     # except NameError as e:
    #     #     # self.logger.error("Failed to take screenshot! %s" % e)
    #     #     self.get_windows_img()

