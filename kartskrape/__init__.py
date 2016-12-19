#!/usr/bin/env python
# -*- coding: utf-8 -*-


__title__ = 'kartskrape'
__version__ = '0.0.1'


"""
Kartskrape

A library for downloading data from Kartverket

:copyright: (c) 2016 by Kjartan Bjørset.
:license: Apache 2.0, see LICENSE for more details.
"""

from dataset_downloader import DatasetDownloader

def login(username, password):
    dl = DatasetDownloader(username, password)
    # dl.login(username, passwor)
    # dl.get_datasets()
    
    for key in dl.datasets:
        print key, dl.datasets[key] 
        # print d[k].get_name()
        # print k.get_name()

    