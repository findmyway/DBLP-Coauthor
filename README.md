DBLP-Coauthor-Mining(从DBLP数据集中挖掘合作者)
=============
详细说明
-------------
		详细说明请查看[数据挖掘实战之DBLP中合作者挖掘（Python+Hadoop)](http://www.tianjun.ml/essays/20)<br />

文件说明
-------------
### getAuthors.py
下载DBLP数据集``dblp.xml``到该目录下，[http://dblp.uni-trier.de/xml/](http://dblp.uni-trier.de/xml/)<br />运行``getAuthors.py`` 得到``authors.txt``文件
### encode.py
运行该文件后将对上一步得到的``authors.txt``文件编码（安装作者姓名出现的顺序依次以正整数编码）得到编码后的文件``authors_encoded.txt``，以及作者姓名与编码对应的文件``authors_index.txt``，其对应关系为姓名所在的行号减1即为其编码ID（ID从0开始）
### view.data.py
读取``authors.txt``，统计不同支持度下有多少作者，同时绘制曲线，确定支持度阈值大概范围
### final.py
主要借鉴了《机器学习实战》中的例子，将结果写入了 ``result*.txt``文件，注意最后的结果增加了置信度过滤。
### mapper.py & reduce.py
第一轮MapReduce的Map和Reduce所用到的文件，其实质就是一个wordCount的过程
### mapper2.py & reduce2.py
第二轮MapReduce的Map和Reduce所用到的文件，注意在这里的输出并给出没有完整的挖掘结果，而是输出的条件模式集，有空的话再转化一下。（本s实验目的只是验证FP-growth在分布式下实现的可能性，所以没有给出完整的结果）

