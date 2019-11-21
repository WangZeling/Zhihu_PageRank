
# -*- coding: utf-8 -*-
# @Author: WangZeling
# @Date:   2019-11-19 13:45:20
# @Last Modified by:   WangZeling
# @Last Modified time: 2019-11-21 13:36:57
# @E-mail:1525148145@qq.com

import networkx as nx
# Create a directed graph
G = nx.DiGraph()
# The relationship between the edges of digraphs
with open(r'E:\360MoveData\Users\ASUS\Desktop\tmp\zhihuall\all.txt','r',encoding='utf-8') as f:
	tolines=f.readlines()
	set1=set(tolines)
	tolines=list(set1)

edges=[]
for i in tolines:
	try:
		edges.append((i.split(',')[0].strip(),i.split(',')[1].strip()))
	except:
		print('something went wrong')

for edge in edges:
    G.add_edge(edge[0], edge[1])
pagerank_list = nx.pagerank(G, alpha=1)
pagerank_list_order=sorted(pagerank_list.items(),key=lambda x:x[1],reverse=True)

# print("pagerank dictionary values：", pagerank_list_order)
for i in pagerank_list_order:
	print(i[0],i[1]*100000)
