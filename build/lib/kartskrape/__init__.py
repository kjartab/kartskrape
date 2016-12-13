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
    dl = DatasetDownloader()
    # dl.login(username, password)
    print dl.get_datasets()
