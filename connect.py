import urllib.request,urllib.error,urllib.parse
import ssl
import bs4 as BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

shandle = urllib.request.urlopen('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin', context=ctx )

for i in shandle:
    print(i.decode())
soup = BeautifulSoup(shandle, 'html.parser')
tag = soup('a')