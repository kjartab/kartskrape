#!/usr/bin/env python
# -*- coding: utf-8 -*-


__title__ = 'kartskrape'


"""
Kartskrape

A library for downloading data from Kartverket

:copyright: (c) 2016 by Kjartan Bjorset.
:license: Apache 2.0, see LICENSE for more details.
"""

import datasets
from dataset_downloader import DatasetDownloader

def get_datasets():
    return datasets.load()

def list_datasets():
    dsets = get_datasets()
    for key, dataset in dsets.items():
        print dataset.id

def download_dataset(username, password, datasetname, download_directory):
    dl = DatasetDownloader(username, password)
    dsets = get_datasets()
    return dl.download(dsets[datasetname], download_directory)





