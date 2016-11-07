# -*- coding: utf-8 -*-
import requests
# import config from dataset_config
# from dataset_config import dataset_config
# from dataset_config import baseurl, datasets
from dataset_config import *

def replace_nordic_characters(nordic_str):
    return nordic_str.replace(" ", "_").replace(u'Ø', u'O').replace(u'ø', u'o').replace(u'Å', u'Aa').replace(u'å', u'aa').replace(u'Æ', u'Ae').replace(u'æ', u'ae')
           

class Dataset(object):

    def __init__(self, dataset_id):
        d = datasets[dataset_id]
        self.name = d['name']
        self.products = d['products']

    # def get_page_url(self, product_id):

    def get_product(self, product_id):
        print self.products
        print product_id
        return self.products.get(product_id)

    def get_product_page_url(self, product_id):
        product = self.get_product(product_id)
        return baseurl + "/" + product["rel_url"]


    def get_geojson_selections(self, selection=None):

        selections = []
        fylker = self.get_selection_base('fylke')

        for f in fylker['features']:
            fn = f['properties']['n']
            fid = f['id']
            fname = 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'
            fname = fname.replace(" ", "_").replace(u'Ø', u'O').replace(u'ø', u'o').replace(u'Å', u'Aa').replace(u'å', u'aa').replace(u'Æ', u'Ae').replace(u'æ', u'ae')
            fylke_selections.append(fname)
            
        return fylke_selections

        res = requests.get(selections[selection_name]['url'])
        return res.json()

    def get_files(self, product_id):

        product = self.get_product(product_id)
        selection = product["selection"]
        geojson = self.get_url_json(selection["url"])
        file_pattern = product["file_pattern"]
        subs = product["substitution"]
        files = []

        for f in geojson["features"]:
            props = f["properties"]
            fid = f["id"]
            tuples = tuple()
            if len(subs) > 0:
                for el in subs:
                    if el == "id":
                        tuples += (fid,)
                    else:
                        tuples += (props[el],)
            files.append(file_pattern % tuples)
        return files

    def get_selection(self, product_id):

        selection = None
        if selection_name:
            selection = self.selection.get(selection_name)

        elif len(self.selection.keys()) > 1:
            selection = selection.get(selection.itervalues().next())
        else:
            raise Exception("no selections")     

        sel_url = selection["definition"]["url"]
        subs = self.selection['substitution']
        file_pattern = self.selection['file_pattern']

        fc = self.get_url_json(sel_url)

        for f in fc['features']:
            fn = f['properties']['n']
            fid = f['id']
            fname = 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'
            fname = fname.replace(" ", "_").replace(u'Ø', u'O').replace(u'ø', u'o').replace(u'Å', u'Aa').replace(u'å', u'aa').replace(u'Æ', u'Ae').replace(u'æ', u'ae')
            fylke_selections.append(fname)
            
        return fylke_selections


    def get_url_json(self, url):
        res = requests.get(url)
        return res.json()




    def get_available_srids(self):
        return ""

    def order(self, srid=None, data_format=None):
        # data_format = 
        return ""

    # def get_urls(self):
    #     for key in self.config['url']['']:
    #         print key
    #     return urls
        
    def get_url(self):
        return sel



