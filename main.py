from flask import Flask, request, render_template, redirect, url_for
from index import Indexer
from search import Searcher
import jieba

from urllib import parse
import json

app = Flask(__name__, static_url_path='')


@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST' and request.form.get('query'):
        query = request.form['query']
        return redirect(url_for('search', query=query))

    return render_template('index.html')


@app.route("/q/<query>", methods=['POST', 'GET'])
def search(query):
    docs = searcher.search(query)
    terms = list(jieba.cut_for_search(query))
    result = highlight(docs, terms)
    return render_template('search.html', docs=result, value=query, length=len(docs))


def highlight(docs, terms):
    result = []
    print()
    for doc in docs:
        content = doc.get('title')
        for term in terms:
            content = content.replace(term, '<em><font color="red">{}</font></em>'.format(term))
        result.append((doc.get('link'), content))
    return result


index = Indexer("docs.txt")
searcher = Searcher(index)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)