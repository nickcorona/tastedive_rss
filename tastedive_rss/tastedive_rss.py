import http.cookiejar

from bs4 import BeautifulSoup
import mechanize
import requests

from tastedive_rss import conf # put your credentials here

# store credentials in cookie
cr = http.cookiejar.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cr)

# avoid 403
br.set_handle_robots(False)
br.addheaders = [
    (
        "User-agent",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    )
]


br.open(conf.URL_LOGIN)

br.select_form(class_="form-horizontal")
br.form["email"] = conf.EMAIL
br.form["password"] = conf.PASSWORD
br.submit()
bs = BeautifulSoup(br.open(conf.URL_MOVIE), "html.parser")

movieList = bs.findAll("div", {"class": ["tk-Resource-title"]})
for name in movieList:
    print(name.get_text())
