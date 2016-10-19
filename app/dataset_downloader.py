#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from kartverket_api import KartverketApi

selections = {
    'fylke' : {
        'url' : 'http://www.norgeskart.no/json/norge/fylker.json'
    },
    'kommune' : {
        'url' : 'http://www.norgeskart.no/json/norge/kommuner.json'
    },
    'hele_landet' : {
        'url' : None
    },
    'dtm50_5' : {
        'url' : 'http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_5.geojson'
    },
    'dtm50_25' : {
        'url' : 'http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_25.geojson'
    },
    'dtm50_50' : {
        'url' : 'http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_50.geojson'
    },
    'dtm50_50' : {
        'url' : 'http://www.norgeskart.no/json/dekning/sjo/celler/dtm50.geojson'
    },
    'utm33' : {
        'url' : 'http://www.norgeskart.no/json/dekning/dtm/utm33.geojson'
    }
}

dataset_config = {
    'stedsnavn' : {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/stedsnavn-ssr-wgs84-geojson'
    },
    'adresser' : {
        'selection' : 'fylke',
        'url' : 'http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv'
    },
    'vbase' : {
        'selection' : 'fylke',
        'ur' : 'http://data.kartverket.no/download/content/vbase-utm-33-fylkesinndeling'
    },
    'sjo_dybdekurver' : {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/sjø-dybdekurver-utm33-600m-grid-shape'
    },
    'sjo_terrengmodell_25m': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
    },
    'sjo_terrengmodell_50m': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
    },
    'sjo_terrengmodell_5m': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
    },
    'grunnkrets': {
        'selection' : '',
        'url' : 'http://data.kartverket.no/download/content/statistiske-enheter-grunnkretser-utm-33-hele-landet'
    },
    'terrengmodell_10m_utm33': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-33'
    },
    'terrengmodell_10m_utm32': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-32'
    },
    'terrengmodell_10m_utm35': {
        'selection' : 'grid',
        'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-35'
    },
    'admin_utm33': {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/administrative-enheter-norge-wgs-84-hele-landet-geojson'
    },
    'admin_wgs84': {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/administrative-enheter-norge-utm-33-hele-landet'
    },
    'elveg_adresser' : {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/elveg-adresser-utm-33-hele-landet'
    },
    'elveg_geometri': {
        'selection' : 'hele_landet',
        'url' : 'http://data.kartverket.no/download/content/elveg-geometri-utm-33-hele-landet'
    },
    'n50_pg_db' : {
        'type' : 'url_download',
        'selection' : None,
        'url' : 'http://data.kartverket.no/data/kartdata/n50/landsdekkende/Kartdata_Norge_UTM33_N50_PostGIS.zip'
    }
}



class Selection(object):

    def get_selection_base(self, selection_name):
        res = requests.get(selections[selection_name]['url'])
        return res.json()

    def get_adresser_fylker(self):
        fylke_selections = []
        fylker = self.get_selection_base('fylke')
        for f in fylker['features']:
            fn = f['properties']['n']
            fid = f['id']
            fname = 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'
            fname = fname.replace(" ", "_").replace(u'Ø', u'O').replace(u'ø', u'o').replace(u'Å', u'Aa').replace(u'å', u'aa').replace(u'Æ', u'Ae').replace(u'æ', u'ae')
            fylke_selections.append(fname)
            # print 'Adressedata_' + str(fid) + '_' + fn + '_UTM33_CSV.zip'
        return fylke_selections

class Datasets(object):

    def __init__(self, username, password):
        self.kapi = KartverketApi(username, password)
        self.selection = Selection()
        self.bestilling_forms = BestillingForms()
        self.kapi.login()
        self.data_dir = self.setup_data_dir('datatest')

    def setup_data_dir(self, data_dir):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return data_dir

    def download(self, data_selection):
        self.kapi.download_file(self.data_dir, '')


    def checkout_bestilling(self, checkout_id):

        res = self.kapi.post("http://data.kartverket.no/download/checkout/"+checkout_id+"/checkout", data=payload)
        return res

    def setup_bestilling(self, url, form_build_id, form_token, product_id):

        fylke_files = self.selection.get_adresser_fylker()
        
        form = self.bestilling_forms.get_form(form_build_id, form_token, product_id, fylke_files)
        return self.kapi.post(url, form)

    def confirm_bestilling(self, checkout_id, res):
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form = self.bestilling_forms.get_confirm_form(form_build_id, form_token)
        return self.kapi.post("http://data.kartverket.no/download/checkout/"+checkout_id+"/checkout", form)


    def send_bestilling(self, dataset):
        url = dataset_config[dataset]['url']
        res = self.kapi.get(url)

        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)

        self.setup_bestilling(url, form_build_id, form_token, product_id)

        res = self.kapi.get('http://data.kartverket.no/download/checkout')
        
        print res.text
        form_action = self.kapi.get_form_action_by_id(res, 'commerce-checkout-form-checkout')
        checkout_id = form_action.split('/')[-2]

        res = self.checkout_bestilling(checkout_id)
        self.confirm_bestilling(self, )


import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class BestillingForms(object):

    def get_adresse_form(self):
        return "test"


    def get_file(self, filename):
        f = open(filename, 'r')
        return f.read()


    def get_form(self, form_build_id, form_token, product_id, files):
        form = Template(self.get_file("post_bestilling.j2")).render({
            'form_build_id' : form_build_id,
            'form_token' : form_token,
            'file_count' : len(files),
            'product_id' : '109057',
            'selections' : "\"" + "\", \"".join(files) + "\""
            })

        return form

    def get_confirm_form(self, form_build_id, form_token):
        return Template(self.get_file("confirm_bestilling.j2").render({
            'form_build_id' : form_build_id,
            'form_token' : form_token
            }))

datasets = Datasets("Kjartanb", "kjartan1")
# datasets.send_bestilling('adresser')
res = datasets.send_bestilling('adresser')
print res
print res.text 