import requests
import yaml
import os
from WeChatBot import WeChatBot


# 发送微信应用消息
# def sendWxMsg(title,desc):
#    # 从redis获取token
#    access_token = cache.get('wx_access_token')
#    sendbody={
#       "touser": touser,
#       "toparty": toparty,
#       "totag": totag,
#       "msgtype": "textcard",
#       "agentid": agentid,
#       "textcard" : {"title" : title,"description" : f"\n<div class=\"gray\">{desc}</div>","url" : "www.baidu.com","btntxt":"更多"
#          },
#       "safe": 0,
#       "enable_id_trans": 0,
#       "enable_duplicate_check": 0
#    }
#    try:
#       res = requests.post(f"{wxurl}/cgi-bin/message/send?access_token={access_token}", json=sendbody,timeout=10)
#       print(f"发送结果：{res.json()}")
#    except requests.exceptions.RequestException as e:
#       print(e)
#       return "发送异常！"
#    if res.json()['errcode'] != 0:
#     print('access_token可能失效或错误，重新获取')
#       access_token = getWxToken()
#       res = requests.post(f"{wxurl}/cgi-bin/message/send?access_token={access_token}", json=sendbody,timeout=10)
#       print(f"发送结果：{res.json()}")
#    return res.text

def main():
   corpid = 'wwf210418e935eb1d1'
   corpsecret = '-wCwLjdsNM-Gwao6l4m-7jta2_Ecerq-5N76E8IBJ3o'
   bot = WeChatBot(corpid, corpsecret)
   
   pass


if __name__=="__main__":
   main()