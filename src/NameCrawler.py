import requests

class NameCrawler:
    'Class for crawling programming language names on Wikipedia'

    def __init__(self):
        self.names = []
        self.namesLower = []
        self.url = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=links&titles=List_of_programming_languages&pllimit=500'
        self.getNames(self.url)

    def getNames(self, url):
        response = requests.get(url)
        res = response.json()
        query = res['query']
        pages = query['pages']
        pageid = pages['144146']
        fullList = pageid['links']
        for item in fullList:
            self.names.append((item['title']))
            self.namesLower.append((item['title']).lower())

        if 'continue' in res:
            con = res['continue']
            if 'plcontinue' in con:
                url = self.url + '&plcontinue=' + con['plcontinue']
                self.getNames(url)