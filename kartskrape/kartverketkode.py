
# def get_files(name):

#     filename = None
#     if not data.get("feature"):
#         filename = name + conf.selection_details
#     else:
#         filename = (data['attributes'].get('f') || data['feature'] + '_' + name) + selection_details

#     if dataformat == 'MrSID':
#         filename = service_layer + '_' + filename.split('_') + '_' + dataformat + '.sid'
#     else:
#         filename = service_layer + '_' + filename.split('_') + '_' + dataformat + '.zip'

#     filename = filename.replace('æ', 'e');
#     filename = filename.replace('Æ', 'E');
#     filename = filename.replace('ø', 'o');
#     filename = filename.replace('Ø', 'O');
#     filename = filename.replace('å', 'a');
#     filename = filename.replace('Å', 'A');

    # var filelist = Array();

    #     var name = data["attributes"]["n"];
    #     //alert('Name: '+name);
    #     var filename;
    #     if (!data["feature"]) {
    #       filename = name + conf.selection_details;
    #     } else {
    #       filename = (data["attributes"]["f"] || data["feature"] + "_" + name) + conf.selection_details;
    #     }

    #     if (conf.dataformat == 'MrSID') {
    #       filename = conf.service_layer + "_" + filename.split(" ").join("_") + '_' + conf.dataformat + '.sid';
    #     } else {
    #       filename = conf.service_layer + "_" + filename.split(" ").join("_") + '_' + conf.dataformat + '.zip';
    #     }
    #     filename = filename.replace(/æ/g, 'e');
    #     filename = filename.replace(/Æ/g, 'E');
    #     filename = filename.replace(/ø/g, 'o');
    #     filename = filename.replace(/Ø/g, 'O');
    #     filename = filename.replace(/å/g, 'a');
    #     filename = filename.replace(/Å/g, 'A');
    #     var path = filename;
    #     //-
    #     if (data["cmd"] == "featureSelected") {
    #       files[path] = filename;
    #     }
    #     if (data["cmd"] == "featureUnselected") {
    #       delete files[path];
    #     }

    #     list = "<ul>\n"
    #     count = 0;

    #     var i = 0;
    #     for (var key in files) {
    #       filelist[i] = key;
    #       list += " <li>" + key + "</li>\n";
    #       i++;
    #     }
    #     list = list + "</ul>\n"
    #     reslist.innerHTML = list;