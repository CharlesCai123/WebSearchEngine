#coding=utf-8
#!/usr/bin/env python3
# encoding=utf-8
# 导入爬虫包
from selenium import webdriver
# 睡眠时间
import time
import re
import os
import requests


# 打开编码方式utf-8打开

# 睡眠时间 传入int为休息时间，页面加载和网速的原因 需要给网页加载页面元素的时间
def s(int):
    time.sleep(int)


# html/body/div[1]/table/tbody/tr[2]/td[1]/input
# http://dmfy.emindsoft.com.cn/common/toDoubleexamp.do

if __name__ == '__main__':
    # 查询的文件位置
    # fR = open('D:\\test.txt','r',encoding = 'utf-8')

    # 模拟浏览器，使用谷歌浏览器，将chromedriver.exe复制到谷歌浏览器的文件夹内
    chromedriver = "chromedriver"
    #chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
    # 设置浏览器
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    # 最大化窗口 用不用都行
    browser.maximize_window()
    #  header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

    # 要爬取的网页
    neirongs = []  # 网页内容
    response = []  # 网页数据
    travel_urls = []
    urls = []
    titles = []
    writefile = open("docs.txt", 'w', encoding='UTF-8')
    url = 'http://travel.yunnan.cn/yjgl/index.shtml'
    # 第一页
    browser.get(url)
    response.append(browser.page_source)
    print(response)
    # 休息时间
    s(3)

    # 第二页的网页数据
    # browser.find_element_by_xpath('// *[ @ id = "downpage"]').click()
    # s(3)
    # print(response.append(browser.page_source))
    # s(3)

    # 第三页的网页数据
    # browser.find_element_by_xpath('// *[ @ id = "downpage"]').click()
    # s(3)
    # response.append(browser.page_source)

    # 3.用正则表达式来删选数据
    reg = r'href="(//travel.yunnan.cn/system.*?)"'
    # 从数据里爬取data。。。
    # 。travel_urls 旅游信息网址
    for i in range(len(response)):
        travel_urls = (re.findall(reg, response[i]))

    # 打印出来放在一个列表里
    for i in range(len(travel_urls)):
        #writefile = open("docs.txt", 'w', encoding='UTF-8')
        url1 = 'http:' + travel_urls[i]
        urls.append(url1)
        print(url1)
        print(url)
        browser.get(url1)
        content = browser.find_element_by_xpath("//div[@class='xcc font14 yh ohd clear']").text
        print(content)
       # 获取标题作为文件名
        b = browser.page_source
        travel_name = browser.find_element_by_xpath('//*[@id="layer213"]').text
        titles.append(travel_name)
    print(titles)
    print(urls)
    for j in range(len(titles)):
        writefile.write(str(j) + '\t\t' + titles[j] + '\t\t' + str(urls[j]) + '\n')

    s(1)
    browser.close()

