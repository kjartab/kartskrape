#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        'url' : 'http://data.kartverket.no/download/content/vbase-utm-33-fylkesinndeling'
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
