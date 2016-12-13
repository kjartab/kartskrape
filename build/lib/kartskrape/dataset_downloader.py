#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from kartverket_api import KartverketApiHelper
from dataset import Dataset
from dataset_config import *


class DatasetDownloader(object):

    def __init__(self):
        self.data_dir = self.setup_data_dir('data')

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
        return self.kapi.post("http://data.kartverket.no/download/checkout/"+checkout_id+"/checkout", form)

    def get_bestilling_page(self, dataset, product_id):
        url = dataset.get_product_page_url(product_id)
        res = self.kapi.get(url)
        return res

    def post_bestilling_page(self, dataset, product_id, res, **kwargs):         
        url = dataset.get_product_page_url(product_id)
        files = dataset.get_product_files(product_id)
        res = self.kapi.get(url)
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)

        max_files = 50
        res = None
        for i in xrange(0, len(files), max_files):
            files[i:i+max_files]
            res = self.post_files_bestilling(files[i:i+max_files], product_id, form_token, form_id,  url)
        return res

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

    def get_checkout(self):
        res = self.kapi.get("http://data.kartverket.no/download/checkout")
        return res
    
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


    def order_dataset(self, dataset, product_id=None):
        res = self.get_bestilling_page(dataset, product_id)        
        self.post_bestilling_page(dataset, product_id, res)        
        res_checkout = self.get_checkout()
        self.post_fortsett_bestilling(res_checkout)


    def get_datasets(self):

        datasets = dict()
        for d in dataset_config:
            ds = Dataset(d)
            datasets[ds.get_key()] = ds
        return datasets

