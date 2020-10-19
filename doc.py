import sys
import warnings

'''
倒排索引原理

倒排索引（英语：Inverted index），也常被称为反向索引、置入档案或反向档案，是一种索引方法，被用来存储在全文搜索下某个单词在一个文档或者一组文档中的存储位置的映射。
它是文档检索系统中最常用的数据结构。通过倒排索引，可以根据单词快速获取包含这个单词的文档列表。倒排索引主要由两个部分组成：“单词词典”和“倒排文件”。

倒排索引有两种不同的反向索引形式：

一条记录的水平反向索引（或者反向档案索引）包含每个引用单词的文档的列表。

一个单词的水平反向索引（完全反向索引）又包含每个单词在一个文档中的位置。

后者的形式提供了更多的兼容性（比如短语搜索），但是需要更多的时间和空间来创建。

通过上面的定义可以知道，一个倒排索引包含一个单词词典和一个倒排文件。其中单词词典包含了所有粒度的拆分词；倒排文件则保存了该词对应的所有相关信息。
'''

class Doc:
    #包含一个字典
    doc_dict = {}
    
    def __init__(self):
        self.doc_dict = {}

    def add(self,key,value):
        if self.doc_dict.get(key):
            warnings.warn('warning:this key already exists, this operation will rewrite the value!')
        self.doc_dict[key] = value
    
    def get(self,key):
        if self.doc_dict.get(key):
            return self.doc_dict[key]
        else:
            sys.stderr.write("error: this key do not exist!")
