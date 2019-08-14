import requests
from bs4 import BeautifulSoup

def SessionGoogle(url_login, url_auth, login, pwd):
    """Login with google."""
    ses = requests.session()
    login_html = ses.get(url_login)
    soup_login = BeautifulSoup(login_html.content).find("form").find_all("input")
    my_dict = {}
    for u in soup_login:
        if u.has_attr("value"):
            my_dict[u["name"]] = u["value"]
    return ses.post(url_auth, data=my_dict)
