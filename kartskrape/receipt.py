# -*- coding: utf-8 -*-
import datetime 

class OrderReceipt(object):

    def __init__(self, dataset, files, html_result):
        self.dataset = dataset
        self.files = files
        self.html = html_result
        # self.expires = datetime.now() + timedelta(hours=23, minutes=45)

    def download_links(self):
        return [self.dataset.download_path + '/' + f for f in self.files]