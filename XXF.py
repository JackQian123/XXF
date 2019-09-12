#-*- coding: UTF-8 -*- 
__author__ = 'qzk'
import requests
import sys
import json
import os
import urllib3
import requests 
sys.path.append('../../')
#from common.splitUrl import splitUrl

url='https://www.sina.com.cn/'
header={'Host': 'www.sina.com.cn',
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0', 
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
      'Connection': 'close',
      'Cookie': 'UOR=,wwwm.cn,; SGUID=1564366387; ULV=39288:2:2:2:58.240.26.203_157.952481:15656026 SINL=58.240.26.203_1565602637.952480; Apache=58.240.26.203_1565602637.952481; UM_distinctid=16c8530703663-0e720be2ad514367940-1fa485307037289; CNZ09=cnzz_eid%3D-1565601264-%26n565601264; CNZZDATA489=199228608-156560165601266; lx2234',
      'Upgrade-Insecure-Requests': '1'
}
header1=header
header2=header
i = 1
k=1
header_XXF_localhost={}
header_XXF_outer={}
#构造X-Forwarded-For，伪造为内网IP
for key in header1 :
    if i ==2:
        header_XXF_localhost['X-Forwarded-For']="127.0.0.1"
    header_XXF_localhost[key]=header1[key]
    i=i+1
#将构造的header发送至服务器，并记录文本（长度a）
requests_XXF_localhost = requests.get(url=url,headers=header_XXF_localhost)
a= (len(requests_XXF_localhost.text))
##################################################################################
#构造X-Forwarded-For，伪造为外网IP
for key in header2 :
    if k ==2:
        header_XXF_outer['X-Forwarded-For']="14.14.14.14"
    header_XXF_outer[key]=header2[key]
    k=k+1
#将构造的header发送至服务器，并记录文本（长度b）
requests_XXF_outer = requests.get(url=url,headers=header_XXF_outer)
b =(len(requests_XXF_outer.text))
###################################################################################
#判断文本内容（长度），若是一致的话，说明X-Forwarded-For并不影响服务器对IP的判断
if a==b:
    print ('不存在XXF内网绕过漏洞')   
