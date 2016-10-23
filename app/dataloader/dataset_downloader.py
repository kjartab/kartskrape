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
        print form_action

        checkout_id = form_action.split('/')[-2]
        print checkout_id
        res = self.kapi.get('http://data.kartverket.no/download/checkout')
        res = self.kapi.get('http://data.kartverket.no/download/checkout/' + checkout_id)
        res = self.kapi.get('http://data.kartverket.no/download/checkout/' + checkout_id + '/checkout')

        return self.confirm_bestilling(checkout_id, res)







    # def log_file(self, content, name):
    #     f = open('views/' + name, 'w')
    #     f.write(content.encode('utf8'))


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


        # multipart/form-data; boundary=----WebKitFormBoundaryDXcsEa32cZCoJVSY


        url = dataset_config[dataset]['url']
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        form_id = self.kapi.get_form_id(res)
        product_id = self.kapi.get_form_product_id(res)


        files = self.selection.get_adresser_fylker()
        # form = self.forms.get_form(form_build_id, form_token, product_id, fylke_files)        
        formdata = self.forms.get_leggtilfiler_form(form_token, form_build_id, product_id, files)

        headers = {
        #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #     'Accept-Encoding':'gzip, deflate',

        #     'Accept-Language':'no,en-US;q=0.8,en;q=0.6',
        #     'Cache-Control':'max-age=0',
        #     'Connection':'keep-alive',
        #     # 'Content-Length':'1037',
            'Content-Type':'multipart/form-data; boundary=----WebKitFormBoundaryDXcsEa32cZCoJVSY',
        #     # 'Cookie':'nmstat=1476775889656; __utmt=1; SESSc0f02e716d49c80a20ced8b7ad16362a=QBymbZQpoxkT552GAsXbO3X-6ja5hL7e-zOIa5m91Gc; has_js=1; __utma=96173449.553203959.1477094421.1477094421.1477127185.2; __utmb=96173449.4.10.1477127185; __utmc=96173449; __utmz=96173449.1477094421.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
        #     # 'Host':'data.kartverket.no
        #     'Origin':'http://data.kartverket.no',
        #     'Referer':'http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv',
        #     'Upgrade-Insecure-Requests':'1'


        }

        # self.log_file(form, "2_post_data")
        # url = "https://www.search.kartan.no/_search"
        # 

        res = self.kapi.post(url, formdata, headers)

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
    def s2post_fortsett_bestilling(self, res):

        url = "http://data.kartverket.no"


        form_action = self.kapi.get_form_action_by_id(res, "commerce-checkout-form-checkout")
        print form_action
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        print form_build_id
        print form_token
        url = url + form_action
        # url = "http://data.kartverket.no/download/checkout/" +  + "/checkout"
        # form = self.forms.get_confirm_form(form_build_id, form_token)

        payload = {
            'op' : 'Fortsett', 
            'form_build_id': form_build_id,
            'form_token' : form_token,
            'form_id' : 'commerce_checkout_form_checkout'
        }

        # headers = {
        #     'Content-Type':'Content-Type:application/x-www-form-urlencoded'
        #     # 'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=pFFdRhXTZFDoUspO19QhJUBtf5zM7erBGOr84JeKsDI"
        # }


        res = self.kapi.post(url, payload)

        self.log_html(res, "bestilling_done")
        return res

    def post_fortsett_bestilling(self, res):

        url = "http://data.kartverket.no"

        self.log_html(res, "bestilling_bekreft")

        form_action = self.kapi.get_form_action_by_id(res, "commerce-checkout-form-checkout")
        form_build_id = self.kapi.get_form_build_id(res)
        form_token = self.kapi.get_form_token(res)
        selections = self.selection.get_adresser_fylker()
        product_id = self.kapi.get_form_product_id(res)

        fomrdata = self.forms.get_confirm_form(form_token, form_build_id)
        # formdata = self.forms.get_fortsett_form(form_token, form_build_id, product_id, selections)

        url = url + form_action
        headers = {
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'cartche-Control':'max-age=0',
            # 'Connection':'keep-alive',
            # 'Content-Type':'Content-Type:application/x-www-form-urlencoded',
            # 'Origin':'http://data.kartverket.no',
            # 'Referer': url,
            # 'Upgrade-Insecure-Requests':'1',
            'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=eJBgyjkDi3YhlflGzPP4dU4vKjEkK67tJoIMO49bH20"
        }

        res = self.kapi.post(url, payload)

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

        bid = "143919"


        url = "http://data.kartverket.no/download/checkout/" +bid +"/checkout" 



        payload = {
            'op' : 'Fortsett', 
            'form_build_id': 'form-GrFH2qiOn91T7e-_2-rU2ZDAHBz1okHVnfdiB6HFfl0',
            'form_token' : 'vF4tRYKLlqO9cIv8BLPPAjO_pnp6AMzrBMO9DkltquA',
            'form_id' : 'commerce_checkout_form_checkout'
            }

        headers = {
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Cache-Control':'max-age=0',
            # 'Connection':'keep-alive',
            # 'Content-Type':'Content-Type:application/x-www-form-urlencoded',
            # 'Origin':'http://data.kartverket.no',
            # 'Referer': url,
            # 'Upgrade-Insecure-Requests':'1',
            'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=eJBgyjkDi3YhlflGzPP4dU4vKjEkK67tJoIMO49bH20"
        }

        # <input type="hidden" name="form_build_id" value="form-GrFH2qiOn91T7e-_2-rU2ZDAHBz1okHVnfdiB6HFfl0">
        # <input type="hidden" name="form_token" value="vF4tRYKLlqO9cIv8BLPPAjO_pnp6AMzrBMO9DkltquA">
# <input type="hidden" name="form_build_id" value="form-7HbJvrKmr4ELIu3NVcNMSWurM-BSRf2JOJ_sQUL7YkY">
# <input type="hidden" name="form_token" value="vF4tRYKLlqO9cIv8BLPPAjO_pnp6AMzrBMO9DkltquA">
# <input type="hidden" name="form_build_id" value="form-KDCQk9OLkzyJmjeyrPFkieckCWKuae48bnqZm2mLQPU">


# <input type="hidden" name="form_token" value="GFHg1-ZLqaj9YOB-Xj2sPEvGO2kYdege4B9Qde1TVmM">
        return requests.post(url, data=payload, headers=headers)


if __name__ == "__main__":

    # res = test_post()
    # log_html(res, "test")
    # test_all()
    # 
    test_post_files()


