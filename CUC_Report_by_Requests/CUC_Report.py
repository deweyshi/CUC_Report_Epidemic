import requests
import re
import time
import datetime
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def main():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "dnt": '1',
        "pragma": "no-cache",
        "referer": "https://www.jiandaoyun.com/dashboard",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": '1',
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/13.0.3 Mobile/15E148 Safari/604.1 ",
        "cookie": cookie
    }
    ss = requests.Session()
    result1 = ss.get(url1, headers=headers)
    csrf_token = re.search(r'jdy_csrf_token = "(.*?)";', result1.text).group(1)
    jdy_ver = re.search(r'{"jdy_ver":"(.*?)",', result1.text).group(1)
    headers2 = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-length": '2',
        "content-type": "application/json;charset=UTF-8",
        "dnt": '1',
        "origin": "https://www.jiandaoyun.com",
        "pragma": "no-cache",
        "referer": "https://www.jiandaoyun.com/dashboard",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "Version/13.0.3 Mobile/15E148 Safari/604.1",
        "x-csrf-token": csrf_token,
        "x-jdy-ver": jdy_ver,
        "cookie": cookie
    }
    if '简道云登录' in result1.text:
        logging.info(result1.text)
        logging.info('You need to update your cookie!')
        sys.exit()
    result2 = ss.post(url2, headers=headers2, json=post_data)
    logging.info(result2.text)


if __name__ == "__main__":
    # 需要修改url1,cookie,post_data及其中的两个日期
    url1 = "https://www.jiandaoyun.com/dashboard#/app/5f0ea52************/form/5f1039f*************"
    url2 = "https://www.jiandaoyun.com/_/data/create"
    tbrq = int(time.mktime(datetime.date.today().timetuple())) * 1000
    tbqrrq = str(datetime.date.today().timetuple().tm_year) \
             + '-' + str(datetime.date.today().timetuple().tm_mon) \
             + '-' + str(datetime.date.today().timetuple().tm_mday)
    cookie = "Hm_********************************=true"
    post_data = {
        "values": {
            "_widget_158********": {
                "data": tbrq,
                "visible": 'false'
            },
            "_widget_16*********": {
                "data": tbqrrq + "-*********-********-*****",
                "visible": 'false'
            },
        },
        "appId": "5f0ea52************",
        "entryId": "5f1039************/",
        "formId": "5f1039f************/",
        "hasResult": 'true',
        "authGroupId": -1
    }
    main()

