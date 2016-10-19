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

    def get_form_build_id(self):
        response = self.get_login_page()
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            return soup.find('input', {'name' : 'form_build_id'}).get('value')
        except:
            return None


    def login(self):
        form_build_id = self.get_form_build_id()
        if form_build_id:
            payload = self.get_login_payload(self.username, self.password, form_build_id)
            session = self.create_session()
            res = session.post(self.url['authenticate'], data = payload)
            self.cookies = res.cookies.get_dict()
            self.session = session
        else:
            raise Exception("no form build id found")

    def get(self, url):
        return self.session.get(url)

    def create_session(self):
        return requests.Session()


if __name__ == "__main__":

    # print kapi.get_login_page()
    kapi.login()

    res = kapi.get("http://data.kartverket.no/download/mine/downloads")
    print res
    print res.text