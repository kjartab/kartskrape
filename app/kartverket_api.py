import requests
from bs4 import BeautifulSoup
from kartverket_config import config

class KartverketApi(object):

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.url = config['url']

    def get_login_payload(self, username, password, form_build_id):
        return {
            'name': username,
            'pass': password,
            'form_build_id': form_build_id,
            'form_id':'user_login_block',
            'op':'Logg inn'
        }

    def get_login_page(self):
        res = requests.get(self.url['login_page'])
        return res

    def get_input_val(self, response, form_name):         
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            return soup.find('input', {'name' : form_name}).get('value')
        except:
            return None

    def get_form_build_id(self, response):
        return self.get_input_val(response, 'form_build_id')

    def get_form_id(self, response):
        return self.get_input_val(response, 'form_id')

    def get_form_product_id(self, response):
        return self.get_input_val(response, 'form_product_id')

    def get_form_token(self, response):
        return self.get_input_val(response, 'form_token')

    def get_form_action_by_id(self, response, idsel):  
        # print response.text       
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            return soup.find('form').get('action')
        except:
            return None

    def verify_login_response(self, response):
        print response

    def login(self):
        response = self.get_login_page()
        print response
        form_build_id = self.get_form_build_id(response)
        if form_build_id:
            payload = self.get_login_payload(self.username, self.password, form_build_id)
            session = self.create_session()
            res = session.post(self.url['authenticate'], data = payload)
            self.verify_login_response(res)
            self.cookies = res.cookies.get_dict()
            self.session = session
        else:
            raise Exception("no form build id found")

    def get(self, url):
        return self.session.get(url)

    def post(self, url, payload):
        return self.session.post(url, data=payload)


    def download_file(self, data_dir, url):
        local_filename = data_dir + '/' + url.split('/')[-1]
        r = self.session.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)
        return local_filename

    def create_session(self):
        return requests.Session()


if __name__ == "__main__":
    kapi = KartverketApi("Kjartanb", "kjartan1")
    kapi.login()

    res = kapi.get("http://data.kartverket.no/download/mine/downloads")
    print res
    print res.text