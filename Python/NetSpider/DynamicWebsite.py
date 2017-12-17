import requests
import re
import json


def crawl(page):
    pn = page * 8
    url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6875&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=%E7%BE%8E%E9%A3%9F&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=" + str(
        pn
    ) + "&rn=8&cb=jQuery110200319478991186668_1472651805605&_=1472651805613"
    res = requests.get(url)
    json_str_re = re.compile("{.*}")
    json_str = json_str_re.search(res.text).group()
    food_dict = json.loads(json_str)
    for food in food_dict["data"][0]["disp_data"]:
        print(food["ename"])


if __name__ == '__main__':
    crawl(1)
