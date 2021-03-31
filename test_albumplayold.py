# -*- coding: utf-8 -*-

from config import driver_config
import unittest
import time
from src.page import Search
from src.page import albumdetail
from src.page import albumplay
from src.common.basepage import Base_page

class test_albumplay_case(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print ('start testing')
    #     driver=driver_config.driver_config()
    #     cls.driver=driver.get_driver()
    #     cls.device=Base_page(cls.driver)
    #     cls.search_song = Search.search(cls.driver)
    #     cls.album_detail=albumdetail.albumdetail(cls.driver)
    #     cls.album_play=albumplay.albumplay(cls.driver)
    #     # time.sleep(10)
    #     # try:
    #     #     cls.driver.find_element_by_id("com.shinyv.cnr:id/iv_ad").is_displayed()
    #     #     print("出现了插屏广告")
    #     #     cls.driver.find_element_by_id("com.shinyv.cnr:id/iv_close").click()
    #     # except Exception as e:
    #     #     print("未出现插屏广告")

    def setUp(self):
        print('开始测试')
        driver=driver_config.driver_config()
        self.driver=driver.get_driver()
        self.imgs = []
        self.addCleanup(self.cleanup)
        self.device = Base_page(self.driver)
        self.search_song = Search.search(self.driver)
        self.album_detail = albumdetail.albumdetail(self.driver)
        self.album_play = albumplay.albumplay(self.driver)
        time.sleep(10)
        try:
            self.driver.find_element_by_id("com.shinyv.cnr:id/iv_ad").is_displayed()
            print("出现了插屏广告")
            self.driver.find_element_by_id("com.shinyv.cnr:id/iv_close").click()
        except Exception as e:
            print("未出现插屏广告")

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def cleanup(self):
        pass

    def test01_playsong(self):
        '''当前播放的单曲是否是所选择的专辑'''
        # time.sleep(10)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        time.sleep(3)
        self.assertEqual(self.album_play.get_albumtitle(),"测试专辑8")
        self.add_img()
        # self.device.get_img()
    def test02_play_status(self):
        '''播放中'''
        # time.sleep(5)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        time.sleep(3)
        seekbar_begin=self.album_play.get_play_seekbar()
        time.sleep(3)
        seekbar_end=self.album_play.get_play_seekbar()
        self.assertNotEqual(seekbar_begin,seekbar_end)  #验证进度条进度是否一样判断是否播放状态
        # self.device.get_img()
        self.add_img()
    def test03_play_status(self):
        '''暂停播放'''
        # time.sleep(5)
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_play()
        seekbar_begin=self.album_play.get_play_seekbar()
        print(seekbar_begin)
        time.sleep(5)
        seekbar_end=self.album_play.get_play_seekbar()
        print(seekbar_end)
        self.assertEqual(seekbar_begin,seekbar_end)  #验证进度条进度是否一样判断是否播放状态
        # self.device.get_img()
        self.add_img()
    def test04_play_next_song(self):
        '''播放下一首'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_next_song()
        self.assertEqual(self.album_play.get_play_song_name(),"4")
        self.add_img()
    def test05_play_previous_song(self):
        '''播放上一首'''
        self.search_song.searchkeywords_firstone("测试专辑8")
        self.album_detail.selectfirstsong()
        self.album_play.click_previous_song()
        self.assertEqual(self.album_play.get_play_song_name(),"2")
        self.add_img()

    def tearDown(self) -> None:
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print('test finished')
    #     cls.driver.quit()



if __name__=="__main__":
    unittest.main()