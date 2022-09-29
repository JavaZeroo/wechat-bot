###
# 火车票  https://www.free-api.com/use/520
# 土味 https://api.lovelive.tools/api/SweetNothings
# https://www.free-api.com/doc/374
# 农历 https://www.free-api.com/use/547
# 假期 http://timor.tech/api/holiday/
###

import logging
logging.basicConfig(filename='running.log', encoding='utf-8', level=logging.DEBUG)
from WeChatBot import WeChatBot
from easydict import EasyDict as edict
import datetime
import requests
from utils import *
NOW = datetime.datetime.now()
LOCATION = '101280105'
KEY = 'e67b0a19d4d14bb4a525ed5cd686c020'

def main():
   corpid = 'wwf210418e935eb1d1'
   corpsecret = '-wCwLjdsNM-Gwao6l4m-7jta2_Ecerq-5N76E8IBJ3o'
   agentid = 1000002
   bot = WeChatBot(agentid, corpid, corpsecret)
   title = f"今天是{NOW.strftime('%Y-%m-%d')}"
   description = f"测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>测试消息\n<b>测试html</b>"
   proxies={
      'http':'socks5://110.40.190.64:2016', 
      'https':'socks5://110.40.190.64:2016'
   }
   weather = get_weather(api='qweather', data={'location': LOCATION, 'key':KEY})
   life = get_life(data={'location': LOCATION, 'key':KEY})
   bot.set_proxies(proxies)
   bot.send_massage(title=title, description=weather)

   pass


if __name__=="__main__":
   main()