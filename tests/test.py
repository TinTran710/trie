import unittest
from src.TrieSuggester import TrieSuggester
from src.NameCrawler import NameCrawler
from pprint import pprint

class TestTrie(unittest.TestCase):

    def setUp(self):
        pass

    def testTotalNameCrawler(self):
        nameCrawler = NameCrawler()
        names = getattr(nameCrawler, 'names')
        self.assertEqual(728, len(names))
    def testCorrectNameCrawler(self):
        nameCrawler = NameCrawler()
        names = getattr(nameCrawler, 'names')
        self.assertEqual('A++', names[0])

    def testTrieSuggesterSingleResult(self):
        nameCrawler = NameCrawler()
        namesLower = getattr(nameCrawler, 'namesLower')
        root = TrieSuggester()
        root.insert(namesLower)
        result = root.search('pyt')
        expectedResult = 'Python (programming language)'.lower()
        self.assertEqual(expectedResult, result[0])

    def testTrieSuggesterMultipleResult(self):
        nameCrawler = NameCrawler()
        namesLower = getattr(nameCrawler, 'namesLower')
        root = TrieSuggester()
        root.insert(namesLower)
        result = root.search('ab')
        self.assertEqual(5, len(result))



if __name__ == '__main__':
    unittest.main()
