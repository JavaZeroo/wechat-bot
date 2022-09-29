import logging
logging.basicConfig(filename='running.log', encoding='utf-8', level=logging.DEBUG)
from pathlib import Path
import requests
import datetime
from easydict import EasyDict as edict
NOW = datetime.datetime.now()
CACHE_DIR = Path('cache')


def write_cache_file(filename, content):
    """
    Caches the given file with the given content.
    """
    path = CACHE_DIR / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(str(content), encoding="utf-8")
    return path


def read_cache_file(filename):
    """
    Returns the content of the given file.
    """
    path = CACHE_DIR / filename
    if path.exists():
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
    print(read_cache_file("test1"))