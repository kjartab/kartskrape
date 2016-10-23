import json
from jinja2 import Template
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

class KartverketForm(object):

    def get_adresse_form(self):
        return "test"


    def get_file(self, filename):
        f = open(filename, 'r')
        return f.read()

    def get_leggtilfiler_form(self, form_token, form_build_id, product_id, selections):
        print selections, len(selections)
        print form_token, form_build_id, product_id, selections


        sel_string = "\"" + "\", \"".join(selections) + "\""
        multipart = """------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="product_id"

            """ + str(product_id) + """
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="form_build_id"

            """ + form_build_id + """
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="form_token"

            """ + form_token + """
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="form_id"

            commerce_cart_add_to_cart_form_""" + str(product_id) + """
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="line_item_fields[field_selection][und][0][value]"

            [""" + sel_string + """]
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="line_item_fields[field_selection_text][und][0][value]"

            """ + str(len(selections)) + """ filer
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="quantity"

            """ + str(len(selections)) + """
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY
            Content-Disposition: form-data; name="op"

            Legg i kurv
            ------WebKitFormBoundaryDXcsEa32cZCoJVSY--"""

        return multipart

    def get_form(self, form_build_id, form_token, product_id, files):
        form = Template(self.get_file("post_bestilling.j2")).render({
            'form_build_id' : form_build_id,
            'form_token' : form_token,
            'file_count' : len(files),
            'product_id' : product_id,
            'selections' : "\"" + "\", \"".join(files) + "\""
            })

        return form

    def get_confirm_form(self, form_build_id, form_token):
        form = Template(self.get_file("confirm_bestilling.j2")).render({
        # form = Template(self.get_file("test_post_bestilling")).render({
            'form_build_id' : form_build_id,
            'form_token' : form_token
            })
        return form