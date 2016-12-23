# from kartskrape.utils import generate_config
import unittest
import os 
# import kartskrape
from kartskrape import html

class TestHtml(unittest.TestCase):

    def get_file(self, filename):
        path = os.path.dirname(os.path.realpath(__file__)) + "/" + filename
        with open(path) as f:
            return f.read()
        
    def test_get_download_url(self):
        res = self.get_file("mine_downloads.html")
        order_id = "147626"
        res = html.get_download_url(res, order_id)
        self.assertEquals(res, "http://data.kartverket.no/download/system/files/grensedata/landsdekkende")

    def test_get_download_url2(self):
        res = self.get_file("mine_downloads2.html")
        order_id = "147750"
        res = html.get_download_url(res, order_id)
        self.assertEquals(res, "http://data.kartverket.no/download/system/files/grensedata/landsdekkende")

    def test_get_download_url3(self):
        res = self.get_file("mine_downloads2.html")
        order_id = "147748"
        res = html.get_download_url(res, order_id)
        self.assertEquals(res, "http://data.kartverket.no/download/system/files/grensedata/landsdekkende")

if __name__ == '__main__':

    unittest.main()
