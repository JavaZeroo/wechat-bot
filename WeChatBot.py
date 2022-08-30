import requests
import datetime
import yaml
import os

config_dir = 'config.yaml'
NOW = datetime.datetime.now()


class WeChatBot():

    def __init__(self, corpid, corpsecret) -> None:
        """
        """
        self.corpid = corpid
        self.corpsecret = corpsecret
        self._checkconfig()
        pass
   
    def _checkconfig(self):

        if os.path.exists(config_dir):
            with open(config_dir, 'r') as f:
                data = yaml.load(f, Loader=yaml.Loader)
                if self._is_expired(data):
                    self.access_token = self._get_access_token()
                else:
                    self.access_token = data['access_token']['key']
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
            res = requests.get(url, timeout=10).json()
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

    def send_massage(title, url="blog.jimmyisme.top"):
        """
        参数	是否必须	说明
        touser	否	成员ID列表（消息接收者，多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
        toparty	否	部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        totag	否	标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为@all时忽略本参数
        msgtype	是	消息类型，此时固定为：textcard
        agentid	是	企业应用的id，整型。企业内部开发，可在应用的设置页面查看；第三方服务商，可通过接口 获取企业授权信息 获取该参数值
        title	是	标题，不超过128个字节，超过会自动截断（支持id转译）
        description	是	描述，不超过512个字节，超过会自动截断（支持id转译）
        url	是	点击后跳转的链接。最长2048字节，请确保包含了协议头(http/https)
        btntxt	否	按钮文字。 默认为“详情”， 不超过4个文字，超过自动截断。
        enable_id_trans	否	表示是否开启id转译，0表示否，1表示是，默认0
        enable_duplicate_check	否	表示是否开启重复消息检查，0表示否，1表示是，默认0
        duplicate_check_interval	否	表示是否重复消息检查的时间间隔，默认1800s，最大不超过4小时
        """
        body = {}
        pass

if __name__=="__main__":
    corpid = 'wwf210418e935eb1d1'
    corpsecret = '-wCwLjdsNM-Gwao6l4m-7jta2_Ecerq-5N76E8IBJ3o'
    bot = WeChatBot(corpid, corpsecret)