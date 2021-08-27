# CUC_Report_Epidemic
中国传媒大学疫情健康报告打卡
### 一、使用Requests
需要修改url1:填报的网址,  
模拟提交一次，Chrome f12 复制cookie，  
post_data复制后修改其中的两个日期为变量。
### 二、使用Selenium
#### 测试环境
```
Ubuntu 20.04.2 LTS (GNU/Linux 5.8.0-1038-oracle x86_64)
python Python 3.8.8
selenium 4.0.0-beta-4
```
#### 文件说明
`c.txt`存放cookies，一般为json格式，可使用[EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)插件导出。
#### 安装Selenium 4
`pip install selenium==4.0.0.b4`
#### 下载对应的Chrome和ChromeDriver
Linux，Mac，Windows都可以，安装方法自行百度。  
Chrome：https://www.google.com/chrome/  
ChromeDriver：https://chromedriver.chromium.org/downloads  
#### 获取自己的cookies
打开https://www.jiandaoyun.com/dashboard#  
使用企业微信扫码登录，Chrome可通过“EditThisCookie”插件导出cookies；
#### Linux下可配合crontab定时运行
先看linux上有没有crontab，没有百度安装一下；  
安装好的，输入：`crontab -e`  
按`i`：  
`0 7 * * * cd /path/to/pyfile && nohup /path/to/python -u CUC_Report.py>log.txt 2>&1 &`  
输入`:wq`保存   
查看刚设置的定时任务：   
`crontab -l`
#### 注意
1.ChromeDriver和CUC_Report.py放在同一文件夹下；  
2.一定要下载对应的Chrome和ChromeDriver；  
3.Selenium 4当前为beta测试版，支持Chrome开发工具协议（Chrome DevTools Protocol），支持原生Chrome开发工具“DevTools”调用，这里使用了模拟地理位置信息。[了解更多](https://www.selenium.dev/zh-cn/documentation/support_packages/chrome_devtools/)
#### 效果
运行完成会自动截图保存，效果如下：  
<img width="400px" src="https://github.com/deweyshi/CUC_Report_Epidemic/blob/main/CUC_Report_by_Selenium/2021-08-26-5.png">
#### 后记
主要解决了几个难点，网上资料很少：  
1.给网站获取地理信息的权限，[source](https://www.linw1995.com/blog/%E5%A6%82%E4%BD%95%E5%9C%A8%E6%97%A0%E5%A4%B4%E6%A8%A1%E5%BC%8F%E4%B8%8B%E7%9A%84%E8%B0%B7%E6%AD%8C%E6%B5%8F%E8%A7%88%E5%99%A8%E8%AE%BE%E7%BD%AE%E5%9C%B0%E7%90%86%E4%BD%8D%E7%BD%AE/). 
```
driver.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://www.jiandaoyun.com/",
        "permissions": ["geolocation"]
    },
)
```
2.虚拟地理位置信息，[source](https://www.selenium.dev/zh-cn/documentation/support_packages/chrome_devtools/). 
```
map_coordinates = dict({
    "latitude": 120.909000,
    "longitude": 120.554600,
    "accuracy": 1
})
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", map_coordinates)
```
3.类似滑动选择日期时间的网页组件，如何用selenium操作？因为是模拟的手机页面，尝试过Touch Actions，但是一直报错，无法解决，只能退其次选择Action Chains。使用过程中发现滑动偏移量不能太大，否则会到手机宽高以外，那么就只能多操作几次。
```
syszd_select_l = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/div[3]/div/div[2]/div[1]/div'))
)
webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -350).perform()
webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -350).perform()
webdriver.ActionChains(driver).drag_and_drop_by_offset(syszd_select_l, 0, -335).perform()
 ```
