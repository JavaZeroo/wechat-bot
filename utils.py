import logging
logging.basicConfig(filename='running.log', encoding='utf-8', level=logging.DEBUG)
from pathlib import Path
import requests
import datetime
from easydict import EasyDict as edict
import json
NOW = datetime.datetime.now()
CACHE_DIR = Path('cache')
LOCATION = '101280105'
KEY = 'e67b0a19d4d14bb4a525ed5cd686c020'

def write_cache_file(filename, content):
    """
    Caches the given file with the given content.
    """
    path = CACHE_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    if str(filename).endswith('.json'):
        with open(path, 'w') as f:
            json.dump(content, f)
    else:
        path.write_text(str(content), encoding="utf-8")
    return path


def read_cache_file(filename):
    """
    Returns the content of the given file.
    """
    path = CACHE_DIR / filename
    if path.exists():
        if str(filename).endswith('.json'):
            with open(path, 'r') as f:
                return json.load(f)
        return path.read_text(encoding="utf-8")
    else:
        return None


# 待处理返回值
def get_weather(api='vvhan', data=None, cache_path=Path('weather.json')):
    """
    data需要为一个字典
    """
    assert data is None or isinstance(data, (dict, edict))
    if data is not None and isinstance(data, dict):
        data = edict(data)
    weather = read_cache_file(cache_path)
    if weather is None:
        logging.debug("No weather cache found. Download weather info")
        if api == 'vvhan':
            weather = edict(requests.get(f'https://api.vvhan.com/api/weather?city=广州').json())
        elif api == 'qweather':
            weather = edict(requests.get(f'https://devapi.qweather.com/v7/weather/now?location={data.location}&key={data.key}').json())
        else:
            raise Exception(f"api:{api} is error or not support. \nOnly support:\napi.vvhan.com\nqweather.com")
        write_cache_file(cache_path, weather)
    else:
        logging.debug("Found weather cache.")
    return weather


def get_life(data=None, cache_path=Path('life.json')):
    """
    data需要为一个字典
    """
    assert data is None or isinstance(data, (dict, edict))
    if data is not None and isinstance(data, dict):
        data = edict(data)
    life = read_cache_file(cache_path)
    try:
        life = edict(life)
        cache_time = datetime.datetime.strptime(life.updateTime, "%Y-%m-%dT%H:%M+08:00")
        if cache_time.date() != NOW.date():
            raise Exception("")
    except:
        life = edict(requests.get(f'https://devapi.qweather.com/v7/indices/1d?type=0&location={data.location}&key={data.key}').json())
        write_cache_file(cache_path, life)
    return life


# 未完成
def get_holiday():
    try:
        holiday = edict(requests.get(f'http://timor.tech/api/holiday/next/').json())
        logging.debug('获取节日成功')
    except:
        logging.warning('获取节日失败！！')
        return None
    
    return holiday

# 待处理返回值
def get_trainTicket(depart, dest, time=NOW):
    url = f'http://huoche.tuniu.com/yii.php?r=train/trainTicket/getTickets&primary[departureDate]={time}&primary[departureCityName]={depart}&primary[arrivalCityName]={dest}'
    trainTicket = edict(requests.get(url).json())

if __name__=="__main__":
    (get_life(data={'location': LOCATION, 'key':KEY}))