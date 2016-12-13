# -*- coding: utf-8 -*-
import json
from bs4 import BeautifulSoup

def get_input_val(response, form_name):         
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        return soup.find('input', {'name' : form_name}).get('value')
    except:
        return None

def get_form_build_id(response):
    return get_input_val(response, 'form_build_id')

def get_form_id(response):
    return get_input_val(response, 'form_id')

def get_form_product_id(response):
    return get_input_val(response, 'product_id')

def get_form_token(response):
    return get_input_val(response, 'form_token')


def get_selection(res):    
    line = next(line for line in res.text.split('\n') if
                line.startswith('jQuery.extend(Drupal.settings'))
    kms_widget = json.loads(
            line.replace('jQuery.extend(Drupal.settings, ', '').replace(');', '')
        ).get('kms_widget', {})

    return kms_widget