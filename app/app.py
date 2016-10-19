#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

import bs4
import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

url = {
    "login": "http://data.kartverket.no/download/content/velkommen?destination=node/134",
    "base": "http://data.kartverket.no/",
    "geodataProduktPage": "http://data.kartverket.no/download/content/geodataprodukter?korttype=All&aktualitet=All&datastruktur=All&dataskema=All&page=",
    "content": "http://data.kartverket.no/download/content/",
    "selection" : {
        "fylker": "http://www.norgeskart.no/json/norge/fylker.json"
    }
}

config = {
    'data' : {
        'adresse': {
            'Adressedata_{fylkeid}_{fylkenavn_underscore}_UTM33_CSV.zip'
        }
    }
}
    

def get_selection(name):
    res = requests.get(url['selection']['fylker'])
    return res.json()

def get_download_page(page_number):
    return url['geodataProduktPage'] + page_number


def get_dataset_url(dataset):
    return url['content'] + dataset

def get_file(filename):
    f = open(filename, 'r')
    return f.read()

def login(payload):
    session = requests.Session()
    session.cookies.get_dict()
    r = session.post(url['login'], data = payload)
    # print r
    # # print r.text
    # print r.cookies
    # for k in r.cookies:
    #     print k
    print session.cookies.get_dict()
    # for cookie in r.cookies:
    #     print cookie.name, cookie.value, cookie.domain

    print r.headers
def download_dataset(dataset):
    url = get_dataset_url(dataset)
    res = requests.get(url)

    print res.text

fylke_selections = []
fylker = get_selection('fylker')
for f in fylker['features']:
    fn = f['properties']['n']
    fid = f['id']
    fname = 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'
    fname = fname.replace(" ", "_").replace(u'Ø', u'O').replace(u'ø', u'o').replace(u'Å', u'Aa').replace(u'å', u'aa').replace(u'Æ', u'Ae').replace(u'æ', u'ae')
    fylke_selections.append(fname)
    print 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'



name = "test"
template = Template('Hello {{ name }}!').render({'name' : name})


form_build_id = "test"
form_token  = "testtoken"

# print fylke_selections
# print len(fylke_selections)

Template(get_file("post_bestilling.j2")).render({
    'form_build_id' : form_build_id,
    'form_token' : form_token,
    'file_count' : len(fylke_selections),
    'product_id' : '109057',
    'selections' : "\"" + "\", \"".join(fylke_selections) + "\""
    })


login_data = {
    'name':'Kjartanb',
    'pass':'kjartan1',
    'form_build_id':'form-wf8e6XRKhmS2phKZLmcMYFsEqdccR5P_E3ZbaTRxobA',
    'form_id':'user_login_block',
    'op':'Logg inn'
}

login(login_data)
