#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from selection import Selection
from kartverket_api import KartverketApi
from forms import KartverketForm
from dataset_config import dataset_config



class Datasets(object):

    def __init__(self, username, password):
        self.kapi = KartverketApi(username, password)
        self.selection = Selection()
        self.forms = KartverketForm()
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







    def log_file(self, content, name):
        f = open('views/' + name, 'w')
        f.write(content.encode('utf8'))


    def log_html(self, res, view):
        f = open('views/' + view + '.html', 'w')
        f.write(res.text.encode('utf8'))


    # 1 - get the first website
    def get_bestilling_page(self, dataset):
        url = dataset_config[dataset]['url']
        res = self.kapi.get(url)
        return res

    # 2 - post with form from website
    def post_bestilling_page(self, dataset, res):


        # multipart/form-data; boundary=----WebKitFormBoundarySlFkEb2FPktJOiG5


        url = dataset_config[dataset]['url']
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)


        fylke_files = self.selection.get_adresser_fylker()
        form = self.forms.get_form(form_build_id, form_token, product_id, fylke_files)        

        self.log_file(form, "2_post_data")


        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',

            'Accept-Language':'no,en-US;q=0.8,en;q=0.6',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            # 'Content-Length':'1037',
            'Content-Type':'multipart/form-data; boundary=------WebKitFormBoundaryUEaEigMCsDJdaUei',
            # 'Cookie':'nmstat=1476775889656; __utmt=1; SESSc0f02e716d49c80a20ced8b7ad16362a=QBymbZQpoxkT552GAsXbO3X-6ja5hL7e-zOIa5m91Gc; has_js=1; __utma=96173449.553203959.1477094421.1477094421.1477127185.2; __utmb=96173449.4.10.1477127185; __utmc=96173449; __utmz=96173449.1477094421.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
            # 'Host':'data.kartverket.no
            'Origin':'http://data.kartverket.no',
            'Referer':'http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv',
            'Upgrade-Insecure-Requests':'1'


        }

        
        res = self.kapi.post(url, form, headers)
        return res


    # 3 - get location from response and run GET request - 
    def get_checkout(self):
        url = "http://data.kartverket.no/download/checkout"
        res = self.kapi.get(url)
        return res


    # 4 - get checkout 
    def get_checkout_id(self, res):
        return res


    # 5 - get checkout with id
    def get_checkout_id_checkout(self, dataset, res):
        return res


    # 6 - FORTSETT button in web app
    def post_fortsett_bestilling(self, res):

        url = "http://data.kartverket.no"

        form_action = self.kapi.get_form_action_by_id(res, "commerce-checkout-form-checkout")

        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        print form_action
        url = url + form_action
        form = self.forms.get_confirm_form(form_build_id, form_token)
        print form

        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',

            'Accept-Language':'no,en-US;q=0.8,en;q=0.6',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            # 'Content-Length':'1037',
            'Content-Type':'Content-Type:application/x-www-form-urlencoded',

            'Origin':'http://data.kartverket.no',
            'Referer': url,
            'Upgrade-Insecure-Requests':'1'
        }



        res = self.kapi.post(url, form, headers)

        self.log_html(res, "bestilling_done")
        return res

    # 4 - get 

    # 5

    # 6

    # 7

def test_all():

    datasets = Datasets("Kjartanb", "kjartan1")
    
    res1 = datasets.get_bestilling_page("adresser")
    datasets.log_html(res1, "1_get")

    res2 = datasets.post_bestilling_page("adresser", res1)
    datasets.log_html(res2, "2_post")


    # datasets.log_file(res2.headers, "headers")
    res3 = datasets.get_bestilling_page("adresser")
    datasets.log_html(res3, "3_get")

    res4 = datasets.get_checkout()
    datasets.log_html(res4, "4_get")

    res5 = datasets.post_fortsett_bestilling(res4)
    print res5
    datasets.log_html(res5, "5_post")

def log_html(res, view):
    f = open('views/' + view + '.html', 'w')
    f.write(res.text.encode('utf8'))

def test_post():
# <input type="hidden" name="form_build_id" value="form--GeJAX8k2pvraMPvtttEhAwTfTRnvNAaItuWqq7fdF4">
# <input type="hidden" name="form_token" value="Y1wPjZ7FLRFm21gDaKPyeuAUSh55l4-4P5wdU-Y4IJk">

        bid = "143899"
        form_build_id =  "form--GeJAX8k2pvraMPvtttEhAwTfTRnvNAaItuWqq7fdF4"
        form_token = "Y1wPjZ7FLRFm21gDaKPyeuAUSh55l4-4P5wdU-Y4IJk"

        url = "http://data.kartverket.no/download/checkout/" +bid +"/checkout" 

        jar = requests.cookies.RequestsCookieJar()
        jar.set('SESSc0f02e716d49c80a20ced8b7ad16362a', 'pFFdRhXTZFDoUspO19QhJUBtf5zM7erBGOr84JeKsDI')

        payload = {
            'op' : 'Fortsett', 
            'form_build_id': 'form-KDCQk9OLkzyJmjeyrPFkieckCWKuae48bnqZm2mLQPU',
            'form_token' : 'GFHg1-ZLqaj9YOB-Xj2sPEvGO2kYdege4B9Qde1TVmM',
            'form_id' : 'commerce_checkout_form_checkout'
            }

        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Content-Type':'Content-Type:application/x-www-form-urlencoded',
            'Origin':'http://data.kartverket.no',
            'Referer': url,
            'Upgrade-Insecure-Requests':'1',
            'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=pFFdRhXTZFDoUspO19QhJUBtf5zM7erBGOr84JeKsDI"
        }

# <input type="hidden" name="form_build_id" value="form-KDCQk9OLkzyJmjeyrPFkieckCWKuae48bnqZm2mLQPU">


# <input type="hidden" name="form_token" value="GFHg1-ZLqaj9YOB-Xj2sPEvGO2kYdege4B9Qde1TVmM">
        return requests.post(url, data=payload, headers=headers, cookies=jar)


if __name__ == "__main__":

    res = test_post()
    log_html(res, "test")