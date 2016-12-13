# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import yaml
import json

baseurl = "http://data.kartverket.no"

def build_datasets(filter=[]):
    next_link = "/download/content/geodataprodukter?korttype=All&aktualitet=All&datastruktur=All&dataskema=All"
    datasets = []
    while next_link:
        url = baseurl + next_link
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        pager_next = soup.find('li', {'class': 'pager-next'})
        temp = parse_datasets(res)
        for d in temp:
            if not any(x in d['name'] for x in filter):
                datasets.append(d)
        if pager_next:
            next_link = pager_next.find('a')['href']
        else:
            next_link = None
    return datasets


def parse_datasets(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    views = soup.findAll('div', {'class': 'views-row'})
    datasets = []
    for view in views:
        div = view.find('div', {'class': 'views-field-body'})
        if div != -1:
            el = div.find('a')
            datasets.append({
                'link' : el['href'],
                'id' : el['href'].replace("/download/content/", ""),
                'name' : el.text
            })

    return datasets

def get_select_for_dataset(link):
    url = "http://data.kartverket.no"
    res = requests.get(url + '/' +link)
    line = next(line for line in res.text.split('\n') if
                line.startswith('jQuery.extend(Drupal.settings'))
    kms_widget = json.loads(
            line.replace('jQuery.extend(Drupal.settings, ', '').replace(');', '')
        ).get('kms_widget', {})    
    return kms_widget



def get_selection_file(name):
    url = "http://www.norgeskart.no/json"
    if name.startswith('dtm-dekning'):
        res = name.split('-')
        url += "/" + res[1] + '/' + res[0] + '/' + res[2] + '.geojson'

    elif name.startswith(('dtm-sjo')):
        res = name.split('-')
        url += "/dekning/sjo/celler/dtm50_" + res[2] + '.geojson'

    elif name.startswith(('raster')):
        url += "/dekning/" + "/".join(name.split('-')) + '.geojson'

    else: 
        url += '/norge/' +  name + '.json'
    res = requests.get(url)
    return json.loads(res.text)


def save_selection_file(directory, name, geojson):
    with open(directory + '/' + name, 'w') as fp:
        json.dump(geojson, fp)

datasets = build_datasets(filter=[
    'Illustrasjonskart', 
    'Raster', 
    'kommuneinndeling', 
    'Digital terrengmodell', 
    'UTM 32', 
    'UTM 35', 
    'TEST',
    'N1000 Kartdata',
    'N500 Kartdata',
    'N250 Kartdata',
    'N5000 Kartdata'
    ] )

with open('config/datasets.yaml', 'w') as fp:
    yaml.safe_dump(datasets, stream=fp, encoding='utf-8', allow_unicode=True)

# selections = dict()
# for d in datasets:
#     sel_name = d['selection']['service_name']
#     if sel_name and sel_name not in selections:
#         file = get_selection_file(sel_name)
#         selections[sel_name] = file
#         save_selection_file('config/selections', sel_name + '.json', file)
