# -*- coding: utf-8 -*-



selection  = {
    "norge" : {
        "fylker" : {
            "url" : "http://www.norgeskart.no/json/norge/fylker.json",
            "srid" : 4326
        },
        "fylker-utm32" : {
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm32.json",
            "srid" : 25832
        },
        "fylker-utm33": {
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm33.json",
            "srid" : 25833
        },
        "fylker-utm35" : {
            "url" : "http://www.norgeskart.no/json/norge/fylker-utm35.json",
            "srid" : 25835
        },
        "kommuner" : {
            "url" : "http://www.norgeskart.no/json/norge/kommuner.json",
            "sird" : 4326
        },
        "kommuner-utm35" : {
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm35.json",
            "srid" : 25835
        },
        "kommuner-utm33" : {
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm33.json",
            "srid" : 25833
        },
        "kommuner-utm32" : {
            "url" : "http://www.norgeskart.no/json/norge/kommuner-utm32.json",
            "srid" : 25832
        }
    },
    "dekning" : {
        "dtm" : {
            "utm32" : {
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
                "srid" : 25832
            },
            "utm33" : {
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33.geojson",
                "srid" : 25833
            },
            "utm35" : {
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
                "sird" : 25835
            },
            "utm33-100km" : {
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33-100km.geojson",
                "srid" : 25833
            }
        }
    },
    "sjo" : {
        "celler": {
            # "dtm50" : {
            #     "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50.geojson",
            #     "srid" : 25833,
            #     "resolution": 50
            # },
            "dtm50_5" : {
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_5.geojson",
                "srid" : 25833,
                "resolution" : 5
            },
            "dtm50_25" : {
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_25.geojson",
                "srid" : 25833,
                "resolution" : 25
            },
            "dtm50_50" : {
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_50.geojson",
                "srid" : 25833,
                "resolution" : 50
            }
        }
    }
}

baseurl = "http://data.kartverket.no/download/content"

datasets = {
    "adresser": {
        "name" : 'Offisielle adresser',
        "products" : {
            "utm33-csv" : {
                "rel_url" : "offisielle-adresser-utm33-csv",
                "file_pattern" : "Adressedata_%s_%s_UTM33_SOSI.zip",
                "substitution" : [ "id", "n" ],
                "selection" : selection["norge"]["fylker"]
            }
        }
    },
    'sjo_terrengmodell' : {
        "name" : 'Sjø terrengmodell',
        "products" : {
            "50m-utm33" : {
                "rel_url" : "sjø-terrengmodell-50m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_50m_DEM.zip",
                "substitution" : ["n"],
                "selection" : selection['sjo']['celler']['dtm50_50']
            },
            "25m-utm33" : {
                "rel_url" : "sjø-terrengmodell-25m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_25m_DEM.zip",
                "substitution" : ["n"],
                "selection" : selection['sjo']['celler']['dtm50_25']
            },
            "5m-utm33" : {
                "rel_url" : "sjø-terrengmodell-5m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_5m_DEM.zip",
                "substitution" : ["n"],
                "selection" : selection['sjo']['celler']['dtm50_5']
            }
        }
    },
    'stedsnavn': {
        "name" : "Stedsnavn",
        "products":  {
            "wgs84-geojson" : {
                "url" : "stedsnavn-ssr-wgs84-geojson",
                "file_pattern" : "",
                "selections" : "file"
            }
        }
    }
}
    #,
    # 'admin' : {
    #     'name' : 'Administrative enheter',
    #     "products" : {
    #         ""
    #     }
    #     "url" : "administrative-enheter-norge-wgs-84-hele-landet-geojson",
    #     "selection_type" : "file",
    #     "selection" : {
    #         "file_name" :  "Grensedata_Norge_WGS84_Adm_enheter_geoJSON.zip"
    #     }
    # },
    # "postsoner" : {
    #     "name" : "Postsoner",
    #     "url" : "digitale-postnummergrenser-utm33-shape-hele-landet",
    #     "selection_type" : "file",
    #     "selection" : {
    #         "file_name" : ""
    #     }
    # },


    # 'sjo_dybdekurver' : {
    #     "name" : "Dybdekurver sjø",
    #     "url" : "sjø-dybdekurver-utm33-600m-grid-shape",
    #     "selection" : {
    #         "type" : "file"
    #     }
    # },
    # 'sjo_terrengmodell' : {
    #     'name' : 'Sjø terrengmodell',
    #     'selection' : {
    #         "type" : "geojson",
    #         "selections" : selection['sjo']['celler']
    #     },
    #     "url" :  "sjø-terrengmodell-50m-utm33",
    # },
    # 'admin' : {
    #     'name' : 'Administrative grenser',
    #     'selection' : {
    #         "type" : "file",
    #         "selections" : {
    #             "csv" : {
    #                 "url" : "offisielle-adresser-utm33-csv"
    #             },
    #             "sosi" : {
    #                 "url" : "offisielle-adresser-utm33-sosi"
    #             }
    #         }
    #     }
    # }
    # 'n50' : {
    #     'name' : 'Database',
    #     'selections' : 'file'
    # }


# dataset_config = {
#     'stedsnavn' : {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/stedsnavn-ssr-wgs84-geojson'
#     },
#     'adresser' : {
#         'selection' : 'fylke',
#         'url' : 'http://data.kartverket.no/download/content/offisielle-adresser-utm33-csv'
#     },
#     'vbase' : {
#         'selection' : 'fylke',
#         'url' : 'http://data.kartverket.no/download/content/vbase-utm-33-fylkesinndeling'
#     },
#     'sjo_dybdekurver' : {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/sjø-dybdekurver-utm33-600m-grid-shape'
#     },
#     'sjo_terrengmodell_25m': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
#     },
#     'sjo_terrengmodell_50m': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
#     },
#     'sjo_terrengmodell_5m': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/sjø-terrengmodell-25m-utm33'
#     },
#     'grunnkrets': {
#         'selection' : '',
#         'url' : 'http://data.kartverket.no/download/content/statistiske-enheter-grunnkretser-utm-33-hele-landet'
#     },
#     'terrengmodell_10m_utm33': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-33'
#     },
#     'terrengmodell_10m_utm32': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-32'
#     },
#     'terrengmodell_10m_utm35': {
#         'selection' : 'grid',
#         'url' : 'http://data.kartverket.no/download/content/digital-terrengmodell-10-m-utm-35'
#     },
#     'admin_utm33': {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/administrative-enheter-norge-wgs-84-hele-landet-geojson'
#     },
#     'admin_wgs84': {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/administrative-enheter-norge-utm-33-hele-landet'
#     },
#     'elveg_adresser' : {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/elveg-adresser-utm-33-hele-landet'
#     },
#     'elveg_geometri': {
#         'selection' : 'hele_landet',
#         'url' : 'http://data.kartverket.no/download/content/elveg-geometri-utm-33-hele-landet'
#     },
#     'n50_pg_db' : {
#         'type' : 'url_download',
#         'selection' : None,
#         'url' : 'http://data.kartverket.no/data/kartdata/n50/landsdekkende/Kartdata_Norge_UTM33_N50_PostGIS.zip'
#     }
# }


