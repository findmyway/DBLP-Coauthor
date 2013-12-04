import codecs
source = codecs.open('authors.txt','r','utf-8')
result = codecs.open('authors_encoded.txt','w','utf-8')
index = codecs.open('authors_index.txt','w','utf-8')
index_dic = {}
name_id = 0

for line in source:
    name_list = line.split(',')
    for name in name_list:
        if not (name == '\r\n'):
            if name in index_dic:
                index_dic[name][1] +=1
            else:
                index_dic[name] = [name_id,1]
                index.write(name + u'\r\n')
                name_id += 1
            result.write(str(index_dic[name][0]) + u',')
    result.write('\r\n')

source.close()
result.close()
index.close()
#print sorted(index_dic.iteritems(), key = lambda a:a[1][1])
