# -*- coding: utf-8 -*-

# From https://github.com/atlefren/skdata/blob/master/get_geojson_url.py

URLS = {
    'fylker': '/json/norge/fylker.json',
    'fylker-utm35': '/json/norge/fylker-utm35.json',
    'fylker-utm33': '/json/norge/fylker-utm33.json',
    'fylker-utm32': '/json/norge/fylker-utm32.json',
    'kommuner': '/json/norge/kommuner.json',
    'kommuner-utm35':  '/json/norge/kommuner-utm35.json',
    'kommuner-utm33':  '/json/norge/kommuner-utm33.json',
    'kommuner-utm32':  '/json/norge/kommuner-utm32.json',
    'dtm-dekning-utm32': '/json/dekning/dtm/utm32.geojson',
    'dtm-dekning-utm33': '/json/dekning/dtm/utm33.geojson',
    'dtm-dekning-utm33-100km':  '/json/dekning/dtm/utm33-100km.geojson',
    'dtm-dekning-utm35':  '/json/dekning/dtm/utm35.geojson',
    'dtm-sjo': '/json/dekning/sjo/celler/dtm50.geojson',
    'dtm-sjo-5': '/json/dekning/sjo/celler/dtm50_5.geojson',
    'dtm-sjo-25': '/json/dekning/sjo/celler/dtm50_25.geojson',
    'dtm-sjo-50': '/json/dekning/sjo/celler/dtm50_50.geojson',
    'raster-32': '/json/dekning/raster/32.geojson',
    'raster-33': '/json/dekning/raster/33.geojson',
    'raster-35': '/json/dekning/raster/35.geojson',
    'raster-n50': '/json/dekning/raster/n50.geojson',
    'raster-n250': '/json/dekning/raster/n250_ny.geojson',
    'raster-n500': '/json/dekning/raster/n500_ny.geojson',
    'raster-n1000': '/json/dekning/raster/n1000_ny.geojson',
    'dybdedata_50m': '/json/norge/dybdedata_50m.geojson',
}


def get_geojson_url(service_type):
    url = URLS.get(service_type, None)
    if url is not None:
        return 'http://www.norgeskart.no%s' % url
    return None