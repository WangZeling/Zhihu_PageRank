# -*- coding: utf-8 -*-
# @Author: WangZeling
# @Date:   2019-11-18 14:42:05
# @Last Modified by:   WangZeling
# @Last Modified time: 2019-11-21 13:28:18
# @E-mail:1525148145@qq.com

# from py2neo import Graph,Node,Relationship
 
# Connect to neo4j database, enter the address, user name, password
# graph = Graph('http://localhost:7474',username='neo4j',password='1')
 
with open(r'E:\360MoveData\Users\ASUS\Desktop\tmp\zhihuall\all.txt','r',encoding='utf-8') as f:
	list1=f.readlines()
set1=set(list1)
list2=list(set1)
list3=[]
for i in list2:
	try:
		list3.append(i.split(',')[0].strip())
		list3.append(i.split(',')[1].strip())
	except:
		print('only one, the false format')
Remove Duplicates
set2 = set(list3)
list4=list(set2)
a=0
for i in list4:
	a+=1
	# Print entity creation statement
	print('''create (n'''+str(a)+''':zhihuEntity { name: "'''+i.strip()+'''" })''')


