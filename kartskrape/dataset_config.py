# -*- coding: utf-8 -*-


SELECTION  = {
    "norge" : {
        "fylker" : {
            "type" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/fylker.json",
            "srid" : "epsg:4326"
        },
        "fylker-utm32" : {
            "type:" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm32.json",
            "srid" : "epsg:25832"
        },
        "fylker-utm33": {
            "type:" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm33.json",
            "srid" : "epsg:25833"
        },
        "fylker-utm35" : {
            "type:" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm35.json",
            "srid" : "epsg:25835"
        },
        "kommuner" : {
            "type": "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/kommuner.json",
            "sird" : "epsg:4326"
        },
        "kommuner-utm35" : {
            "type" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm35.json",
            "srid" : "epsg:25835"
        },
        "kommuner-utm33" : {
            "type" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm33.json",
            "srid" : "epsg:25833"
        },
        "kommuner-utm32" : {
            "type" : "region_geojson",
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm32.json",
            "srid" : "epsg:25832"
        }
    },
    "dekning" {
        "dtm" {
            "utm32" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
                "srid" : "epsg:25832",
                "resolution" : 50
            },
            "utm33" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33.geojson",
                "srid" : "epsg:25833",
                "resolution" : 50
            },
            "utm35" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
                "sird" : "epsg:25835",
                "resolution" : 50
            },
            "utm33-100km" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33-100km.geojson",
                "srid" : "epsg:25833",
                "resolution" : 100
            }
        }
    },
    "sjo" : {
        "celler": {
            "dtm50" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50.geojson",
                "srid" : "epsg:25833",
                "resolution": 50
            },
            "dtm50_5" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_5.geojson",
                "srid" : "epsg:25833",
                "resolution" : 5
            },
            "dtm50_25" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_25.geojson",
                "srid" : "epsg:25833",
                "resolution" : 25
            },
            "dtm50_50" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_50.geojson",
                "srid" : "epsg:25833",
                "resolution" : 50
            }
        }
    }
}

DATASETS = {
    'stedsnavn': {

    },
    'adresser': {
        'name' : 'Offisielle adresser',
        'selections' : {

        }
    },
    'sjo_dybdekurver' : {
        
    },
    'sjo_terrengmodell' : {
        'name' : 'Sjø terrengmodell',
        'selections' : {
            'sjo' : {
                'celler' : [
                    'dtm50',
                    'dtm50_5',
                    'dtm50_25',
                    'dtm50_50'
                ]
            }
        }
    },
    'grunnkrets': {

    },
    'admin' : {
        'name' : 'Administrative grenser',
        'selections' : {
            'norge' : [
                'fylker'
            ]
        }
    },
    'n50' : {
        'name' : 'Database',
        'selections' : 'file'
    }
}


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


