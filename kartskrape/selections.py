# -*- coding: utf-8 -*-

URLS  = {
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
                "srid" : "epsg:25832"
            },
            "utm33" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33.geojson",
                "srid" : "epsg:25833"
            },
            "utm35" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
                "sird" : "epsg:25835"
            },
            "utm33-100km" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/dtm/utm33-100km.geojson",
                "srid" : "epsg:25833"
            }
        }
    },
    "sjo" : {
        "celler": {
            "dtm50" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50.geojson",
                "srid" : "epsg:25833"
            },
            "dtm50_5" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_5.geojson",
                "srid" : "epsg:25833"
            },
            "dtm50_25" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_25.geojson",
                "srid" : "epsg:25833"
            },
            "dtm50_50" : {
                "type" : "grid_geojson",
                "url" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_50.geojson",
                "srid" : "epsg:25833"
            }
        }
    }
}



# selection_files = {

        
#         "fylker" : "http://www.norgeskart.no/json/norge/fylker.json",
#         "fylker-utm35" : "http://www.norgeskart.no/json/norge/fylker-utm35.json",
#         "fylker-utm32" : "http://www.norgeskart.no/json/norge/fylker-utm32.json",
#         "fylker-utm33" : "http://www.norgeskart.no/json/norge/fylker-utm33.json",

#         "kommuner" : "http://www.norgeskart.no/json/norge/kommuner.json",
#         "kommuner-utm35" : "http://www.norgeskart.no/json/norge/kommuner-utm35.json",
#         "kommuner-utm33" : "http://www.norgeskart.no/json/norge/kommuner-utm33.json",

#         "utm32" : "http://www.norgeskart.no/json/dekning/dtm/utm32.geojson",
#         "utm33" : "http://www.norgeskart.no/json/dekning/dtm/utm33.geojson",
#         "utm33-100km" : "http://www.norgeskart.no/json/dekning/dtm/utm33-100km.geojson",
#         "utm35" : "http://www.norgeskart.no/json/dekning/dtm/utm35.geojson",

#         "dtm50" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50.geojson",
#         "dtm50_5" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_5.geojson",
#         "dtm50_25" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_25.geojson",
#         "dtm50_50" : "http://www.norgeskart.no/json/dekning/sjo/celler/dtm50_50.geojson",

#         "32" : "http://www.norgeskart.no/json/dekning/raster/32.geojson",
#         "33" : "http://www.norgeskart.no/json/dekning/raster/33.geojson",
#         "35" : "http://www.norgeskart.no/json/dekning/raster/35.geojson",
#         "n50" : "http://www.norgeskart.no/json/dekning/raster/n50.geojson",
#         "n250_ny" : "http://www.norgeskart.no/json/dekning/raster/n250_ny.geojson",
#         "n500_ny" : "http://www.norgeskart.no/json/dekning/raster/n500_ny.geojson",
#         "n1000_ny" : "http://www.norgeskart.no/json/dekning/raster/n1000_ny.geojson",
        
#         "dybdedata_50m" : "http://www.norgeskart.no/json/norge/dybdedata_50m.geojson",
#         "500m" : "http://www.norgeskart.no/json/norge/500m.geojson"
#     }