# -*- coding:utf-8 -*-

"""
NAME: 简单的天气预报软件
"""
__version__ = '0.1'
__author__ = 'thinkerleo'

import urllib2
import logging
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')




def get_whether(citycode):
    try:
        url = "http://php.weather.sina.com.cn/xml.php?city=" + citycode + "&password=DJOYnieT8234jlsK&day=0"
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        str = response.read().decode('utf-8')
    except  Exception:
        print('网络错误!')
        os._exit(1)

    try:
        city = str.split('<city>',1)[1].split('</city>',1)[0]
    except IndexError :
        print('请输入正确的城市名称！')
        os._exit(1)

    status1_day = str.split('<status1>',1)[1].split('</status1>',1)[0]
    status2_night = str.split('<status2>',1)[1].split('</status2>',1)[0]

    direction1_day = str.split('<direction1>',1)[1].split('</direction1>',1)[0]
    direction2_night = str.split('<direction2>',1)[1].split('</direction2>',1)[0]

    power1_day = str.split('<power1>',1)[1].split('</power1>',1)[0]
    power2_night = str.split('<power2>',1)[1].split('</power2>',1)[0]

    temperature1_day = str.split('<temperature1>',1)[1].split('</temperature1>',1)[0]
    temperature2_night = str.split('<temperature2>',1)[1].split('</temperature2>',1)[0]

    chy_shuoming =  str.split('<chy_shuoming>',1)[1].split('</chy_shuoming>',1)[0]

    pollution_l = str.split('<pollution_l>',1)[1].split('</pollution_l>',1)[0]

    ktk_l = str.split('<ktk_l>',1)[1].split('</ktk_l>',1)[0]

    zwx_s = str.split('<zwx_s>',1)[1].split('</zwx_s>',1)[0]

    nowdatetime = str.split('<udatetime>',1)[1].split('</udatetime>',1)[0]

    str1 = ''
    str1 = str1 + '天气预报\n'
    str1 = str1 + "白天天气：%s " %status1_day.encode('utf-8')
    str1 = str1 + "夜晚天气：%s\n" %status2_night.encode('utf-8')
    str1 = str1 + "白天温度：%s " %temperature1_day.encode('utf-8')
    str1 = str1 + "夜晚温度：%s\n" %temperature2_night.encode('utf-8')
    str1 = str1 + "穿衣建议：%s\n" %chy_shuoming.encode('utf-8')
    str1 = str1 + "空调开关建议：%s\n" %ktk_l.encode('utf-8')
    str1 = str1 + "紫外线等级：%s\n" %zwx_s.encode('utf-8')
    str1 = str1 + "发布时间：%s\n" % nowdatetime.encode('utf-8')
    return str1

if __name__ == '__main__':
    city = raw_input('请输入要查询的城市：')
    print get_whether(city.encode('gb2312'))