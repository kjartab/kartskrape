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