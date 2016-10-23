#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kartverket_api import KartverketApi 
from selection import Selection
import os
import requests


def log_html(res, view):
    f = open('views/' + view + '.html', 'w')
    f.write(res.text.encode('utf8'))


def test_post_files():

    url = "http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv"
    
    headers = {
        'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=Cvfpati7pU-p6exgyqhEJeVBIfSGN2djcIBrmNKFvx0"
    }
    res = requests.get(url, headers=headers)
    kapi = KartverketApi("Kjartanb", "kjartan1")
    kapi.login()

    form_build_id = kapi.get_form_build_id(res)
    form_token = kapi.get_form_token(res)
    form_id =  kapi.get_form_id(res)
    product_id =  kapi.get_form_product_id(res)



    multipart = """------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="product_id"

109057
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="form_build_id"

""" + form_build_id + """
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="form_token"

""" + form_token + """
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="form_id"

commerce_cart_add_to_cart_form_109057
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="line_item_fields[field_selection][und][0][value]"

["Adressedata_20_Finnmark_UTM33_CSV.zip"]
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="line_item_fields[field_selection_text][und][0][value]"

1 filer
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="quantity"

1
------WebKitFormBoundaryDXcsEa32cZCoJVSY
Content-Disposition: form-data; name="op"

Legg i kurv
------WebKitFormBoundaryDXcsEa32cZCoJVSY--"""


    selection = Selection()
    files = selection.get_adresser_fylker()


    headers = {
        "Content-Type" : "multipart/form-data; boundary=----WebKitFormBoundaryDXcsEa32cZCoJVSY",
        'Cookie' : "SESSc0f02e716d49c80a20ced8b7ad16362a=Cvfpati7pU-p6exgyqhEJeVBIfSGN2djcIBrmNKFvx0"
    }

    pres = requests.post(url, data=multipart, headers=headers)
    

    log_html(pres, "postmulti")
    url = "http://data.kartverket.no/download/cart"
    res = requests.get(url, headers=headers)
    log_html(pres, "dls")
    return pres




        # return requests.post(url, data=payload, headers=headers)


if __name__ == "__main__":

    test_post_files()


