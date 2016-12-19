# -*- coding: utf-8 -*-
from config import urls

class Dataset(object):

    def __init__(self, datasetid, name):
        self.id = datasetid
        self.name = name
        self.url =  urls.kartverket["download-content"] + self.id