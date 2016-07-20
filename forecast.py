# -*- coding:utf-8 -*-

import urllib.parse,json
import urllib.request

city = input("输入城市中文名：")
citycode = urllib.request.quote(city.encode('gb2312'))



url = "http://php.weather.sina.com.cn/xml.php?city=" + citycode + "&password=DJOYnieT8234jlsK&day=0"
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
str = response.read().decode('utf-8')

city = str.split('<city>',1)[1].split('</city>',1)[0]

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

udatetime = str.split('<udatetime>',1)[1].split('</udatetime>',1)[0]

print("城市：%s\n" %city)
print("白天天气：%s" %status1_day)
print("夜晚天气：%s\n" %status2_night)

print("白天风向：%s" %direction1_day)
print("夜晚风向：%s\n" %direction2_night)

print("白天风力：%s" %power1_day)
print("夜晚风力：%s\n" %power2_night)

print("白天温度：%s" %temperature1_day)
print("夜晚温度：%s\n" %temperature2_night)
print("穿衣建议：%s\n" %chy_shuoming)
print("污染等级：%s\n" %pollution_l)
print("空调开关建议：%s\n" %ktk_l)
print("紫外线等级：%s\n" %zwx_s)
print("数据更新时间：%s\n" %udatetime)


