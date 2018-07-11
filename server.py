from flask import Flask, render_template, request
from src.NameCrawler import NameCrawler
from src.TrieSuggester import TrieSuggester

app = Flask(__name__)

nameCrawler = NameCrawler()
names = getattr(nameCrawler, 'names')
root = TrieSuggester()
root.insert(names)

@app.route('/trie/index')
def runCrawler():
    return render_template('index.html', names=names)

@app.route('/trie/search', methods = ['GET', 'POST'])
def search():
    if request.method == 'POST':
        prefix = request.form['prefix']
        result = root.search(prefix)
        return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4600)