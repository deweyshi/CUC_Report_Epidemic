# -*- coding: utf-8 -*-


import requests
import time
import datetime
import logging
import sys
from bs4 import BeautifulSoup
from http.cookiejar import LWPCookieJar
import execjs
import re

# 同时打印和保存日志
logger = logging.getLogger()
logger.setLevel('INFO')
BASIC_FORMAT = "%(asctime)s %(filename)s[line:%(lineno)d] %(message)s"
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)
chlr = logging.StreamHandler() # 输出到控制台的handler
chlr.setFormatter(formatter)
chlr.setLevel('INFO')  # 也可以不设置，不设置就默认用logger的level
fhlr = logging.FileHandler('log.txt') # 输出到文件的handler
fhlr.setFormatter(formatter)
logger.addHandler(chlr)
logger.addHandler(fhlr)

class JDY:
    def __init__(self, u, p):
        self.username = u  # 用户名
        self.password = p  # 密码

        self.__session = requests.Session()
        self.__session.keep_alive = False
        self.__path = f'Cookie_{self.username}.txt'
        self.__session.cookies = LWPCookieJar(filename=self.__path)
        self.__charset = "utf-8"
        self.__sso_url = 'https://sso.cuc.edu.cn'
        self.__jdy = 'https://www.jiandaoyun.com'
        self.__jdy_url = self.__jdy + '/sso/custom/wxd6d77b944b3b0051/iss'
        self.__jdy_create = self.__jdy + '/_/data/create'
        self.__ecp_url = ''
        self.__pev_val = ''
        
        self.__tbrq = int(time.mktime(datetime.date.today().timetuple())) * 1000
        self.__tbqrrq = str(datetime.date.today().timetuple().tm_year) \
                 + '-' + str(datetime.date.today().timetuple().tm_mon) \
                 + '-' + str(datetime.date.today().timetuple().tm_mday)
        self.__headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
        }

        # 这里的表单需要自己改成自己的，建议手动抓包一次，其中的几个日期需要修改
        self.__post_data = {
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
        
    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return
        self.logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))  # 重点

    def encrypt_pwd(self):
        # logging.info('generate_rsa 初始化')
        res_des = self.__session.get(self.__ecp_url, headers=self.__headers)
        # logging.info('generate_rsa js文件请求完成')
        cp_js = execjs.compile(res_des.text)
        # logging.info('generate_rsa 通过模块导入js')
        result = cp_js.call('encryptPassword', self.password, self.__pev_val)
        # logging.info('generate_rsa 通过模块执行js')
        return result

    def sso_login(self, use_cookie):
        try:
            if use_cookie:
                # logging.info('使用本地Cookie登录。')
                self.__session.cookies.load(ignore_discard=True, ignore_expires=True)
                res = self.__session.get(self.__sso_url, headers=self.__headers)
                res.encoding = self.__charset
            else:
                raise Exception
        except:
            # logging.info('不用Cookie，使用账号密码登录。')
            self.__session.cookies.clear()
            response = self.__session.get(self.__sso_url, headers=self.__headers)
            if '统一身份认证平台' not in response.text:
                response.encoding = self.__charset
                logging.info(response.text)
                logging.info('未知错误，获取sso失败！')
                return False
            html = BeautifulSoup(response.text, "html.parser")
            re_ecp = re.search(r'src="(.*?)encrypt(.*?)"', response.text)
            self.__ecp_url = self.__sso_url + re_ecp.group(1) + 'encrypt' + re_ecp.group(2)
            # logging.info(self.__ecp_url)
            self.__pev_val = html.find('input', attrs={'id': 'pwdEncryptSalt'})['value']
            execution = html.find('input', attrs={'name': 'execution'})['value']
            event_id = html.find('input', attrs={'name': '_eventId'})['value']
            dllt = html.find('input', attrs={'id': 'dllt'})['value']
            data = {
                'username': self.username,
                'password': self.encrypt_pwd(),
                'captcha': '',
                'cllt': 'userNameLogin',
                'lt': '',
                'execution': execution,
                '_eventId': event_id,
                'dllt': dllt
            }
            # logging.info(data)
            # logging.info(self.__sso_url + '/authserver/login')
            response2 = self.__session.post(
                self.__sso_url + '/authserver/login',
                headers=self.__headers, data=data)
            response2.encoding = self.__charset
            self.__session.cookies.save(ignore_discard=True, ignore_expires=True)
            
    def jdy_submit(self):
        result0 = self.__session.get(self.__jdy_url, headers=self.__headers)
        csrf_token = re.search(r'jdy_csrf_token = "(.*?)";', result0.text).group(1)
        jdy_ver = re.search(r'{"jdy_ver":"(.*?)",', result0.text).group(1)        
        jdy_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
            "x-csrf-token": csrf_token,
            "x-jdy-ver": jdy_ver,
        }
        if '简道云登录' in result0.text:
            logging.info(result0.text)
            logging.info('You need to update your cookie!')
            sys.exit()
        result2 = self.__session.post(self.__jdy_create, headers=jdy_headers, json=self.__post_data)
        logging.info(result2.text)
        
    def main(self):
        # 建议设置为True，只需要第一次登录，后面几天可以优先使用保存的cookie
        self.sso_login(use_cookie=False)
        self.jdy_submit()
         
if __name__ == "__main__":
    # 校园账号、密码
    x = JDY('202XXXXXXXXXXX', '****************')
    x.main()
