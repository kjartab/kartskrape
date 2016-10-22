#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from kartverket_api import KartverketApi
from dataset_config import dataset_config
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
        res = self.kapi.post(url, form)
        
        return self.kapi.get(url)

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


        res = self.setup_bestilling(url, form_build_id, form_token, product_id)
        res = self.kapi.get('http://data.kartverket.no/download/checkout')

        form_action = self.kapi.get_form_action_by_id(res, 'commerce-checkout-form-checkout')


        checkout_id = form_action.split('/')[-2]
        print checkout_id
        res = self.kapi.get('http://data.kartverket.no/download/checkout')
        res = self.kapi.get('http://data.kartverket.no/download/checkout/' + checkout_id)
        res = self.kapi.get('http://data.kartverket.no/download/checkout/' + checkout_id + '/checkout')

        return self.confirm_bestilling(checkout_id, res)


if __name__ == "__main__":
    # kapi = KartverketApi("Kjartanb", "kjartan1")
    # kapi.login()

    datasets = Datasets("Kjartanb", "kjartan1")
    res = datasets.send_bestilling('adresser')
    print res
    # print res.text 