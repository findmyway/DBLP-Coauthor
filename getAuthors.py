import codecs
from xml.sax import handler, make_parser
paper_tag = ('article','inproceedings','proceedings','book',
                   'incollection','phdthesis','mastersthesis','www')

class mHandler(handler.ContentHandler):
    def __init__(self,result):
        self.result = result
        self.flag = 0

    def startDocument(self):
        print 'Document Start'
        
    def endDocument(self):
        print 'Document End'
        
    def startElement(self, name, attrs):
        if name == 'author':
            self.flag = 1
                    
    def endElement(self, name):
        if name == 'author':
            self.result.write(',')
            self.flag = 0
        if (name in paper_tag) :
            self.result.write('\r\n')
        
    def characters(self, chrs):                                 # [8]
        if self.flag:
            self.result.write(chrs)

def parserDblpXml(source,result):
    handler = mHandler(result)
    parser = make_parser()
    parser.setContentHandler(handler)
        
    parser.parse(source)
    

if __name__ == '__main__':
    source = codecs.open('dblp.xml','r','utf-8')
    result = codecs.open('authors.txt','w','utf-8')
    parserDblpXml(source,result)
    result.close()
    source.close()
