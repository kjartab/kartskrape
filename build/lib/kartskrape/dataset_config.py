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

dataset_config = [
    {
        "key" : "adresser",
        "source" : "kartverket-std",
        "name" : 'Offisielle adresser',
        "download_base_url" : "http://data.kartverket.no/download/system/files/matrikkeldata/adresser",
        "substitution" : { "id" : "id", "properties" : ["n"] },
        "products" : {
            "utm33-csv" : {
                "rel_url" : "offisielle-adresser-utm33-csv",
                "file_pattern" : "Adressedata_%s_%s_UTM33_CSV.zip",
                "selection" : selection["norge"]["fylker"]
            },
            "utm33-sosi" : {
                "rel_url" : "offisielle-adresser-utm33-sosi",
                "file_pattern" : "Adressedata_%s_%s_UTM33_SOSI.zip",
                "selection" : selection["norge"]["fylker"]
            }
        }
    },
    {
        "key" : "sjo_terrengmodell",
        "name" : 'Sjø terrengmodell',
        "source" : "kartverket-std",
        "download_base_url" : "http://data.kartverket.no/download/system/files/sjodata/terrengdata",
        "substitution" : {  "properties" : ["n"] },
        "products" : {
            "50m-utm33" : {
                "rel_url" : "sjø-terrengmodell-50m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_50m_DEM.zip",
                "download_path" : "50m",
                "selection" : selection['sjo']['celler']['dtm50_50']
            },
            "25m-utm33" : {
                "rel_url" : "sjø-terrengmodell-25m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_25m_DEM.zip",
                "download_path" : "25m",
                "selection" : selection['sjo']['celler']['dtm50_25']
            },
            "5m-utm33" : {
                "rel_url" : "sjø-terrengmodell-5m-utm33",
                "file_pattern" : "Sjodata_terrengmodell_%s_UTM33_5m_DEM.zip",
                "download_path" : "5m",
                "selection" : selection['sjo']['celler']['dtm50_5']
            }
        }
    },

    {
        "key" : "stedsnavn", 
        "name" : "Stedsnavn",
        "source" : "kartverket-std",
        "download_base_url" : "http://data.kartverket.no/download/system/files/stedsnavn",
        "substitution" : { "id" : "fid", "properties" : ["n"] },
        "products":  {
            "wgs84-geojson" : {
                "file_pattern" : "Stedsnavn_Norge_WGS84_geoJSON.zip",
                "selection" : "file",
                "path" : "landsdekkende"
            },
            "utm33-sosi" : {
                "url" : "stedsnavn-ssr-wgs84-geojson",
                "file_pattern" : "Stedsnavn_%s_%s_UTM33_CSV.zip",
                "selection" : selection["norge"]["fylker"],
                "path" : "fylker"
            }
        }
    },
    {
        "key" : "terrengmodell-metadata",
        "name": "Terrengmodell metdata",
        "source": "hoydedata",
        "products" : {
            "metadata" : {
                "url" : "https://hoydedata.no/LaserInnsyn/Home/DownloadFile?filename=NHM_Metadata_20161107.zip"
            }
        }
    },
    {
        "key" : "terrengmodell_dtm",
        "name" : "Terrengmodell DTM",
        "source" : "hoydedata",
        "download_base_url": "https://hoydedata.no/LaserInnsyn/Home/DownloadFile",
        "products" : {
            "dtm-10m" : {
                "url_params" : "?filename=",
                "filename" :  "DTM10_%s%s%s.zip",
                "selection" : "file"
            },
            "dtm-50m" : {
                "url_params" : ["filename"],
                "filename" :  "DTM50_%s%s%s.zip",
                "selection" : "file"
            }
        }
    },
    {
        "key" : "terrengmodell_dom",
        "name" : "Terrengmodell DOM",
        "source" : "hoydedata",
        "download_base_url": "https://hoydedata.no/LaserInnsyn/Home/DownloadFile",
        "products" : {
            "dom-10m" : {
                "url_params" : ["filename"],
                "filename" :  "DOM10_%s%s%s.zip",
                "selection" : "file"
            },
            "dom-50m" : {
                "url_params" : ["filename"],
                "filename" :  "DOM50_%s%s%s.zip",
                "selection" : "file"
            }
        }
    }
]
