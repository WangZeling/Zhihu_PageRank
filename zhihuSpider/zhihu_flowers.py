# -*- coding: utf-8 -*-
# @Author: WangZeling
# @Date:   2019-11-18 22:25:39
# @Last Modified by:   WangZeling
# @Last Modified time: 2019-11-21 13:20:41
# @E-mail:1525148145@qq.com
import requests
import re
import sys
import os
import time

#Maintain a global list to prevent repeated crawls
global_ID_list=[]

# Modify the recursive call depth
sys.setrecursionlimit(2000)

#get the list of zhihu id and name
def get_idnames(url):
	headers={"User-Agent":"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}
	r=requests.get(url,headers=headers)
	r.encoding ='utf-8'
	idlist = re.findall('''{"id":".*?","urlToken":"(.*?)","name":".*?",".*?''',r.text)
	namelist = re.findall('''{"id":".*?","urlToken":".*?","name":"(.*?)",".*?''',r.text)
	return idlist,namelist
# Recursive crawler entry url
firsturl = 'https://www.zhihu.com/org/ji-qi-zhi-xin-65/followers'
headers={"User-Agent":"Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}
r=requests.get(firsturl,headers=headers)
r.encoding ='utf-8'
# Use regular expression matching
idlist = re.findall('''{"id":".*?","urlToken":"(.*?)","name":".*?",".*?''',r.text)
namelist = re.findall('''{"id":".*?","urlToken":".*?","name":"(.*?)",".*?''',r.text)
aid = 0

print(namelist)
def fact(theidlist,thenamelist):
	namelist=[]
	idlist=[]
	for i in range(len(theidlist)):
		url='https://www.zhihu.com/people/{}/followers'.format(theidlist[i])
		time.sleep(3)
		idlist,namelist=get_idnames(url)
		
		# Prevent repeated crawling
		global global_ID_list
		global_ID_list.append(theidlist[i])
		
		for lenth in range(len(idlist)):
			if idlist[lenth] in global_ID_list:
				pass
			else:
				print(namelist[lenth]+','+thenamelist[i])
				with open(r'E:\360MoveData\Users\ASUS\Desktop\tmp\zhihuall\zhihuflowers_flowers.txt','a',encoding='utf-8') as f:
					f.write(namelist[lenth]+','+thenamelist[i])
					f.write('\n')
				with open(r'E:\360MoveData\Users\ASUS\Desktop\tmp\zhihuall\zhihuflowers_flowers_id.txt','a',encoding='utf-8') as f:
					try:
						f.write(namelist[lenth]+';'+idlist[lenth]+','+thenamelist[i]+';'+theidlist[lenth])
						# exception handling 
					except IndexError as e:
						print(e,'IndexError: list index out of range')
					f.write('\n')
	fact(idlist,namelist)
# Call recursive functions
fact(idlist,namelist)
