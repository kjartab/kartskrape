#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from selection import Selection
from kartverket_api import KartverketApiHelper
from forms import KartverketForm
from dataset_config import dataset_config



class Datasets(object):

    def __init__(self, username, password):
        
        self.kapi = KartverketApiHelper(username, password)
        self.kapi.login()

        self.selection = Selection()
        self.forms = KartverketForm()
        
        self.data_dir = self.setup_data_dir('datatest')

    def setup_data_dir(self, data_dir):
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        return data_dir

    def confirm_bestilling(self, checkout_id, res):
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form = self.bestilling_forms.get_confirm_form(form_build_id, form_token)
        return self.kapi.post("http://data.kartverket.no/download/checkout/"+checkout_id+"/checkout", form)

    def get_bestilling_page(self, dataset):
        url = dataset_config[dataset]['url']
        res = self.kapi.get(url)
        return res

    def post_bestilling_page(self, dataset, res):

        url = "http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv"
        # url = dataset_config[dataset]['url']
        res = self.kapi.get(url)
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)

        selections = self.selection.get_adresser_fylker()
        filer_string = "\"" + "\", \"".join(selections) + "\""

        data = {
            "product_id": product_id,
            "form_token": form_token,
            "form_id": form_id,
            "line_item_fields[field_selection][und][0][value]" : filer_string,
            "line_item_fields[field_selection_text][und][0][value]" : len(selections),
            "quantity" : len(selections),
            "op" : "Legg i kurv"
        }

        res = self.kapi.post(url, data)

        return res

    def get_checkout(self):
        url = "http://data.kartverket.no/download/checkout"
        res = self.kapi.get(url)
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


    def download(self, data_selection):
        data_selection = self.selection.get_adresser_fylker()
        url = "http://data.kartverket.no/download/system/files/matrikkeldata/adresser/"
        for file in data_selection:
            self.kapi.download_file("datatest", url + "/" + file)


    def order_dataset(self, dataset):
        
        res1 = self.get_bestilling_page(dataset)        
        res2 = self.post_bestilling_page(dataset, res1)        
        res3 = self.get_checkout()
        res4 = datasets.post_fortsett_bestilling(res3)




def log_html(res, view):
    f = open('views/' + view + '.html', 'w')
    f.write(res.text.encode('utf8'))


if __name__ == "__main__":

    datasets = Datasets("Kjartanb", "kjartan1")
    datasets.order_dataset("adresser")
    datasets.download("adresser")


