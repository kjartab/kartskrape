# -*- coding: utf-8 -*-
import requests
import json

def get_selection_file(name):
    print name
    url = "http://www.norgeskart.no/json"
    if name.startswith('dtm-dekning'):
        res = name.split('-')
        url += "/" + res[1] + '/' + res[0] + '/' + res[2] + '.geojson'

    elif name.startswith(('dtm-sjo')):
        res = name.split('-')
        url += "/dekning/sjo/celler/dtm50_" + res[2] + '.geojson'

    elif name.startswith(('raster')):
        url += "/dekning/" + "/".join(name.split('-')) + '.geojson'

    else: 
        url += '/norge/' +  name + '.json'
    res = requests.get(url)
    return json.loads(res.text)


def build_file_names(selection):

    service_layer = selection['service_layer']
    dataformat = selection['dataformat']
    selection_type = selection['selection_type']
    selection_details = selection['selection_details']
    service_name = selection['service_name']
    print selection
    selection_file = get_selection_file(service_name)
    # print selection_file
    # for feature in selection_file['features']
    # data['attributes']
    # service_layer
    # data["attributes"]["f"] || data["feature"] + "_" + service_name + selection_details
    files = []
    if selection_file:
        for f in selection_file['features']:
            fname = f['properties']['n']
            fid = f['id']
            # print selection_details
            # print service_layer, fid, fname, selection_details
            files.append(make_file_name(service_layer, fid, fname, selection_details, dataformat))    
        print files
        return files
    
    filename = None
    # if (dataformat == 'MrSID'):
    #     filename = service_layer + "_" + filename.split(" ").join("_") + '_' + dataformat + '.sid';
    # else:
    #     filename = service_layer + "_" + filename.split(" ").join("_") + '_' + dataformat + '.zip';
    if not filename:
        return selection_details

    return filename

def make_file_name(service_layer, fid, fname, selection_details, dataformat):
    filename =  service_layer + u'_' + str(fid) + u'_' + fname +  selection_details+ '_' + dataformat +'.zip'
    filename.replace(u'ø', u'o').replace(u'Ø',u'O').replace(' ', '_')
    return filename
        # var name = data["attributes"]["n"];
        # //alert('Name: '+name);
        # var filename;
        # if (!data["feature"]) {
        #   filename = name + conf.selection_details;
        # } else {
        #   filename = (data["attributes"]["f"] || data["feature"] + "_" + name) + conf.selection_details;
        # }

        # if (conf.dataformat == 'MrSID') {
        #   filename = conf.service_layer + "_" + filename.split(" ").join("_") + '_' + conf.dataformat + '.sid';
        # } else {
        #   filename = conf.service_layer + "_" + filename.split(" ").join("_") + '_' + conf.dataformat + '.zip';
        # }
        # filename = filename.replace(/æ/g, 'e');
        # filename = filename.replace(/Æ/g, 'E');
        # filename = filename.replace(/ø/g, 'o');
        # filename = filename.replace(/Ø/g, 'O');
        # filename = filename.replace(/å/g, 'a');
        # filename = filename.replace(/Å/g, 'A');
