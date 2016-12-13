#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
import os
import requests
from kartverket_api import KartverketApiHelper
from dataset import Dataset
import selection
import json
from config import urls

class DatasetDownloader(object):

    def __init__(self, username, password):
        self.data_dir = self.setup_data_dir('data')
        self.datasets = self.load_datasets()
        self.login(username, password)

    def login(self, username, password):
        self.kapi = KartverketApiHelper(username, password)
        self.kapi.login()

    def setup_data_dir(self, data_dir):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return data_dir

    def confirm_bestilling(self, checkout_id, res):
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form = self.bestilling_forms.get_confirm_form(form_build_id, form_token)
        return self.kapi.post(urls.kartverket["download-checkout"] + checkout_id + "/checkout", form)

    def order(self, dataset):
        res = self.kapi.get(dataset.url)

        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)
        widget = self.get_select_for_dataset(res)
        files = selection.build_file_names(widget)

        max_files = 50
        res = None
        for i in xrange(0, len(files), max_files):
            files[i:i+max_files]
            res = self.post_files_bestilling(files[i:i+max_files], product_id, form_token, form_id,  dataset.url)
        
        res = self.kapi.get(urls.kartverket["download-checkout"])
        return res

    def get_select_for_dataset(self, res):
        line = next(line for line in res.text.split('\n') if
                    line.startswith('jQuery.extend(Drupal.settings'))
        kms_widget = json.loads(
                line.replace('jQuery.extend(Drupal.settings, ', '').replace(');', '')
            ).get('kms_widget', {})    
        return kms_widget


    def post_files_bestilling(self, files, product_id, form_token, form_id,  url):

        filer_string = "[\"" + "\", \"".join(files) + "\"]"
        data = {
            "product_id": product_id,
            "form_token": form_token,
            "form_id": form_id,
            "line_item_fields[field_selection][und][0][value]" : filer_string,
            "line_item_fields[field_selection_text][und][0][value]" : len(files),
            "quantity" : len(files),
            "op" : "Legg i kurv"
        }

        return self.kapi.post(url, data)
    
    def post_fortsett_bestilling(self, res):

        url = "http://data.kartverket.no"
        form_action = self.kapi.get_form_action_by_id(res, "commerce-checkout-form-checkout")
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        url = url + form_action

        payload = {
            'op' : 'Fortsett', 
            'form_build_id': form_build_id,
            'form_token' : form_token,
            'form_id' : 'commerce_checkout_form_checkout'
            }

        res = self.kapi.post(url, payload)
        return res


    def download(self, dataset, product_id):
        data_selection = dataset.get_product_files(product_id)
        product_base_url = dataset.get_product_download_base_url(product_id)
        for file in data_selection:
            self.kapi.download_file("data", product_base_url + "/" + file)


    def order_dataset(self, dataset):
        res = self.order(dataset)
        self.post_fortsett_bestilling(res)

    def load_datasets(self):
        datasets = dict()
        with open("config/datasets.yaml", "r") as f:
            dsets = yaml.load(f)
            for d in dsets:
                datasets[d['id']] = Dataset(d['id'], d['name'])
        return datasets

if __name__ == '__main__':
    dl = DatasetDownloader("Kjartanb", "kjartan1")
    dl.order_dataset(dl.datasets['offisielle-adresser-utm33-csv'])


