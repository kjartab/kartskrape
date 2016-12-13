# -*- coding: utf-8 -*-
import requests

baseurl = "http://data.kartverket.no/download/content"

class Dataset(object):

    def __init__(self, definition):
        self.key = definition['key']
        self.name = definition['name']
        self.products = definition.get('products', [])
        self.download_base_url = definition.get('download_base_url')
        self.file_substitution = definition.get('substitution')

    def get_product(self, product_id):
        return self.products.get(product_id)
        
    def get_product_page_url(self, product_id):
        product = self.get_product(product_id)
        return baseurl + "/" + product["rel_url"]

    def get_product_download_base_url(self, product_id):
        url = self.download_base_url

        product = self.get_product(product_id)
        path = product.get("download_path")
        if path:
            url += '/' + path
        return url

    def get_products(self):
        return self.products.keys()

    def get_name(self):
        return self.name

    def get_key(self):
        return self.key

    def get_product_files(self, product_id):

        product = self.get_product(product_id)

        selection = product["selection"]

        geojson = self.get_url_json(selection["url"])
        file_pattern = product["file_pattern"]
        subs = self.file_substitution

        files = []
        print subs
        id_field = subs.get("id")
        subs = subs.get("properties", [])

        for f in geojson["features"]:

            tuples = tuple()
            props = f["properties"]
            this_id = f.get(id_field)

            if this_id:
                tuples += (this_id,)
            if len(subs) > 0:
                for el in subs:
                    tuples += (props[el],)

            fname = file_pattern % tuples
            fname = replace_nordic_characters(fname)
            files.append(fname)
        return files

    def get_url_json(self, url):
        res = requests.get(url)
        return res.json()



