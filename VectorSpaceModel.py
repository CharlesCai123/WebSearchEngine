#coding=utf-8
# 关键词统计和词频统计，以列表形式返回
'''
向量空间模型原理

向量空间模型(vector space   model)概念简单，把对文本内容的处理简化为向量空间中的向量运算，
并且它以空间上的相似度表达语义的相似度，直观易懂。当文档被表示为文档空间的向量，就可以通过计算向量
之间的相似性来度量文档间的相似性。文本处理中最常用的相似性度量方式是余弦距离。

搜索引擎需要计算“用户查询”和爬下来的众多”网页“之间的相似度，从而把最相似的排在最前返回给用户。

3.4.2代码实现原理

代码主要使用的算法是tf-idf

tf：term frequency 词频

idf：inverse document frequency 倒文档频率

主要思想是：如果某个词或短语在一篇文章中出现的频率高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类。

第一步：把每个网页文本分词，成为词包（bag of words）。

第三步：统计网页（文档）总数M。

第三步：统计第一个网页词数N，计算第一个网页第一个词在该网页中出现的次数n，再找出该词在所有文档中出现的次数m。则该词的tf-idf 为：n/N * 1/(m/M)  （还有其它的归一化公式，这里是最基本最直观的公式）

第四步：重复第三步，计算出一个网页所有词的tf-idf 值。

第五步：重复第四步，计算出所有网页每个词的tf-idf 值。
'''
def Count(resfile):
    t = {}
    infile = open(resfile, 'r', encoding='utf-8-sig')
    f = infile.readlines()
    count = len(f)
    # print(count)
    infile.close()
    s = open(resfile, 'r', encoding='utf-8-sig')
    i = 0
    while i < count:
        line = s.readline()
    # 去换行符
        line = line.rstrip('\n')
        # print(line)
        words = line.split(" ")
        #   print(words)
 
        for word in words:
            if word != "" and t.__contains__(word):
                num = t[word]
                t[word] = num + 1
            if word !="":
                t[word] = 1
        i = i + 1
    # 字典按键值降序
    dic = sorted(t.items(), key=lambda t: t[1], reverse=True)
    # print(dic)
    # print()
    s.close()
    return (dic)
 
def MergeWord(T1, T2):
 
    MergeWord = []
    duplicateWord = 0
    for ch in range(len(T1)):
        MergeWord.append(T1[ch][0])
    for ch in range(len(T2)):
        if T2[ch][0] in MergeWord:
            duplicateWord = duplicateWord + 1
        else:
            MergeWord.append(T2[ch][0])
    # print('重复次数 = ' + str(duplicateWord))
    # 打印合并关键词
    # print(MergeWord)
    return MergeWord
 
# 得出文档向量
def CalVector(T1, MergeWord):
    TF1 = [0] * len(MergeWord)
    for ch in range(len(T1)):
        TermFrequence = T1[ch][1]
        word = T1[ch][0]
        i = 0
    while i < len(MergeWord):
        if word == MergeWord[i]:
            TF1[i] = TermFrequence
            break
        else:
            i = i + 1
        # print(TF1)
    return TF1
 
 
def CalConDis(v1, v2, lengthVector):
    # 计算出两个向量的乘积
    B = 0
    i = 0
    while i < lengthVector:
        B = v1[i] * v2[i] + B
        i = i + 1
    # print('乘积 = ' + str(B))
    # 计算两个向量的模的乘积
    A = 0
    A1 = 0
    A2 = 0
    i = 0
    while i < lengthVector:
        A1 = A1 + v1[i] * v1[i]
        i = i + 1
    # print('A1 = ' + str(A1))
 
    i = 0
    while i < lengthVector:
        A2 = A2 + v2[i] * v2[i]
        i = i + 1
        # print('A2 = ' + str(A2))
 
    A = math.sqrt(A1) * math.sqrt(A2)
    print('两篇文章的相似度 = ' + format(float(B) / A, ".3f"))


