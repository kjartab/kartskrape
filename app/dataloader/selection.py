#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selection_config import selections
import requests


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
            
        return fylke_selections
