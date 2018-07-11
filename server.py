from flask import Flask, render_template, request
from src.NameCrawler import NameCrawler
from src.TrieSuggester import TrieSuggester
import time

app = Flask(__name__)

nameCrawler = NameCrawler()
names = getattr(nameCrawler, 'names')
namesLower = getattr(nameCrawler, 'namesLower')
root = TrieSuggester()
root.insert(namesLower)

@app.route('/trie/index')
def runCrawler():
    return render_template('index.html', namesLower=namesLower)

@app.route('/trie/search', methods = ['POST'])
def search():
    if request.method == 'POST':
        prefix = request.form['prefix'].lower()

        startTime1 = time.time()
        lowerCaseMatch1 = root.search(prefix)
        elapsedTime1 = time.time() - startTime1
        result1 = getCaseSensitiveResult(lowerCaseMatch1)

        startTime2 = time.time()
        lowerCaseMatch2 = alternateSearch(prefix)
        elapsedTime2 = time.time() - startTime2
        result2 = getCaseSensitiveResult(lowerCaseMatch2)

        return render_template('index.html', result1=result1, elapsedTime1=elapsedTime1, result2=result2, elapsedTime2=elapsedTime2)

def alternateSearch(prefix):
    result = []
    for string in namesLower:
        if string.startswith(prefix):
            result.append(string)
    return result

def getCaseSensitiveResult(lowerCaseMatch):
    result = []
    for string in lowerCaseMatch:
        for i in range(0, len(names)):
            if string == names[i].lower():
                result.append(names[i])
    return result

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4600)