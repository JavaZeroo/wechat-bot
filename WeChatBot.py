import requests
import datetime
import yaml
import os

config_dir = 'config.yaml'
NOW = datetime.datetime.now()


class WeChatBot():

    def __init__(self, agentid, corpid, corpsecret) -> None:
        """
        """
        self.agentid = agentid
        self.corpid = corpid
        self.corpsecret = corpsecret
        self.proxies = None
        self._checkconfig()
        pass
   


    def set_proxies(self, proxies):
        self.proxies = proxies
        try:
            res = requests.get('http://ip-api.com/json', timeout=10, proxies=self.proxies).json()
            print("Using ip %s" % res['query'])
        except Exception as e:
            print("Proxies may not be available")
            print(e)


    def send_massage(self, title, description, touser='@all', toparty='@all', totag='@all', url="blog.jimmyisme.top"):
        body = {
            "touser" : touser,
            "toparty" : toparty,
            "totag" : totag,
            "msgtype" : "textcard",
            "agentid" : self.agentid,
            "textcard" : {
                        "title" : title,
                        "description" : description,
                        "url" : url,
            },
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        # print(body)
        post_url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.access_token}"
        try:
            res = requests.post(post_url, json=body,timeout=10, proxies=self.proxies).json()
        except requests.RequestException as e:
            raise Exception(f"Cannot post message: {e}")
        error_code = res['errcode']
        if error_code == 0:
            print("Succeful send message")
            pass    
        else:
            check_error = f"https://open.work.weixin.qq.com/devtool/query?e={error_code}"
            raise Exception(f"Return with Error Code {error_code}\nPlease Check in {check_error}")


    def _checkconfig(self):

        if os.path.exists(config_dir):
            with open(config_dir, 'r') as f:
                data = yaml.load(f, Loader=yaml.Loader)
                if self._is_expired(data):
                    self.access_token = self._get_access_token()
                else:
                    self.access_token = data['access_token']['key']
                    print(self.access_token)
                    pass
        else:
            self.access_token = self._get_access_token()
        self._create_config()


    def _create_config(self):
        data = {'access_token': {'key': self.access_token, 'expired_at': (NOW + datetime.timedelta(seconds=7200)).strftime("%Y-%m-%d %H:%M:%S")}}
        with open(config_dir, 'w') as f:
            yaml.dump(data, f)
        pass


    def _is_expired(self, data):
        expire_at = data['access_token']['expired_at']
        if expire_at is None:
            return True
        expire_at = datetime.datetime.strptime(expire_at, "%Y-%m-%d %H:%M:%S")
        if expire_at > NOW:
            print('Not expired')
            return False
        else:
            print('Expired')
            return True


    def _get_access_token(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        try:
            res = requests.get(url, timeout=10, proxies=self.proxies).json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Cannot get access_token: {e}")

        error_code = res['errcode']
        if error_code == 0:
            access_token=res['access_token']
            print(f"access_token={access_token}")
            return access_token
        else:
            check_error = f"https://open.work.weixin.qq.com/devtool/query?e={error_code}"
            raise Exception(f"Return with Error Code {error_code}\nPlease Check in {check_error}")


if __name__=="__main__":
    corpid = 'wwf210418e935eb1d1'
    corpsecret = '-wCwLjdsNM-Gwao6l4m-7jta2_Ecerq-5N76E8IBJ3o'

    bot = WeChatBot(corpid, corpsecret)


