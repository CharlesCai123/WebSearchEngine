from index import Indexer
import jieba
import operator
import math
 
'''
搜索
返回结果：(相关问题,相似度)列表
搜索步骤：
    1.分词
    2.计算tf-idf,找出候选doc
    3.对文档排序

BM25算法

BM25算法原理

BM25是一种用来评价搜索词和文档之间相关性的算法，它是一种基于概率检索模型提出的算法。
BM25属于bag-of-words模型，bag-of-words模型只考虑document中词频，不考虑句子结构或者语法关系之类，
把document当做装words的袋子，具体袋子里面可以是杂乱无章的。对每一个搜索查询，我们很容易给每个文档定义
一个“相关分数”。当用户进行搜索时，我们可以使用相关分数进行排序而不是使用文档出现时间来进行排序。
这样，最相关的文档将排在第一个，无论它是多久之前创建的（当然，有的时候和文档的创建时间也是有关的）。

我们要从最简单的、基于统计的方法说起。这种方法不需要理解语言本身，而是通过统计词语的使用、匹配和基于文档中特有词的普及率的权重等情况来决定“相关分数”。

这个算法不关心词语是名词还是动词，也不关心词语的意义。它唯一关心的是哪些是常用词，那些是稀有词。如果一个搜索语句中包括常用词和稀有词，最好让包含稀有词的文档的评分高一些，同时降低常用词的权重。
 
'''
class Searcher:
 
    def __init__(self, index):
        self.index = index
 
    def search(self, query):
        term_list = []
        query = query.split()
        for entry in query:
            # 分词
            term_list.extend(jieba.cut_for_search(entry))
 
        # 计算tf-idf,找出候选doc
        tf_idf = {}
        for term in term_list:
            if term in self.index.inverted:
                for doc_id, fre in self.index.inverted[term].items():
                    if doc_id in tf_idf:
                        tf_idf[doc_id] += (1 + math.log10(fre)) * self.index.idf[term]
                    else:
                        tf_idf[doc_id] = (1 + math.log10(fre)) * self.index.idf[term]
        # 排序
        sorted_doc = sorted(tf_idf.items(), key=operator.itemgetter(1), reverse=True)
 
        res = [self.index.id_doc[doc_id] for doc_id, score in sorted_doc]
        return res
