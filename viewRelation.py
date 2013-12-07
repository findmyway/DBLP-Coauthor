# -*- coding: utf-8 -*-
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import codecs
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc")
def createEdge(nodeX):
    with codecs.open('authors.txt','r','utf-8') as f:
        for line in f:
            line = line.strip().split(',')
            if line[-1] == '':
                line.remove('')
            if nodeX in line and len(line) >1:
                line.remove(nodeX)
                for author in line:
                    yield (author,nodeX)
def makeFreqDic():
    print "Creating FreqDic..."
    with codecs.open('authors.txt','r','utf-8') as f:
        freqDic = {}
        for line in f:           
            line = line.strip().split(',')
            if line[-1] == '':
                line.remove('')               
            for author in line:
                freqDic[author] = freqDic.get(author,0) + 1
        return freqDic
def main(freqDic,nodeX):
    G = nx.Graph()
    print "Adding edge..."
    for A,B in createEdge(nodeX):
        edgeDic = G.get_edge_data(A,B,default = {'weight':0})
        G.add_edge(A, B, weight = edgeDic['weight'] + 1)
    nodes = G.nodes()
    nodes.remove(nodeX)
    shells = [[nodeX], nodes]
    pos = nx.shell_layout(G,shells)
    print "Drawing nodes..."
    nodeSize = [10*freqDic[n] for n, dic in G.nodes_iter(data=True)]
    nodeColors = np.random.rand(len(nodeSize))
    nx.draw_networkx_nodes(G, pos, node_size=nodeSize,node_color= nodeColors,alpha=0.7)
    print "Drawing edges..."
    edgeWidth = [edata['weight'] for u,v,edata in G.edges(data=True)]
    edgeColor = np.random.rand(G.number_of_edges())
    nx.draw_networkx_edges(G, pos, width = edgeWidth, edge_color=edgeColor,alpha=0.35)
    print "Adding label..."
    select_labels = {n:n for n,d in G.nodes_iter(data=True) if freqDic[n] >= 80}
    select_labels[nodeX]= nodeX
    nx.draw_networkx_label(G,pos,labels = select_labels,font_size=8,alpha=0.3)
    title = str(nodeX) + u"与其合作者之间的关系网络"
    plt.title(title, size=15,fontproperties=font)
    plt.text(0.5, 0.94,  u"# 节点大小对应该作者发表文章总次数",
             horizontalalignment='center',
             size=10,color='r',verticalalignment='center',
             transform=plt.gca().transAxes,
             fontproperties=font)
    plt.text(0.5, 0.97,  u"# 节点之间连线粗细对应该两个作者一起发表文章总次数",
             horizontalalignment='center',
             size=10,color='r',verticalalignment='center',
             transform=plt.gca().transAxes,
             fontproperties=font)
    plt.axis('off')
    fileName = str(nodeX) + ".png"
    plt.savefig(fileName,transparent=True,dpi=500)
    plt.show()

if __name__ == '__main__':
    freqDic = makeFreqDic()
    nodeX = u'Irith Pomeranz'
    main(freqDic, nodeX)
