# WebSearchEngine
A Simple Demo For WebSearch Engine Design

This is a very execution of the exact demo of the author's code using Python to make up a simple web search engine. The website is
https://blog.csdn.net/qq_35993946/article/details/88087827. The author has explained the specific knowledge in terms of a series of 
basic functions which a Web Search Engine should have, including the follow points:

1. A Crawler script used for widely collecting, picking out and saving all the information of targeted websites using RE as the dict.
2. Jieba library for splitting the key words from a sentence and the basic introduction of the principles of Inverted Index.
3. Count the matching degree of the searched word with all the document libs saved before, and then sort the documents.
4. Python Flask Tools for creating socket server communication and Web Framework Design using HTML.

Here I follow the process step by step and get the right output as an Web Search Engine does. Firstly we have to change the targeted url 
in urlCrawler.py and then execute it to collect all the information on that website by recording it into a file naming docs.txt. Here you 
have to make sure there's browser driver installed already whose version corresponds to what your browser is. And In this project, all
relevant information about http://travel.yunnan.cn/yjgl/index.shtml is recorded into docs.txt already. Afterwards we run main.py and input 
http://localhost:8080 into a browser and thereby we can see the reply when keywords entered.

This is just a very simple demo of searching engine and there's still too much work needed to be done to make the whole project perfect.
