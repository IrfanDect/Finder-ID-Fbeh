from finder import Finder
from rich import print

url_list = [
        'https://www.facebook.com/Googles.09',
        'https://www.facebook.com/XDR.202211',
        'https://www.facebook.com/ismuha.fia',
        'https://www.facebook.com/viko.febrian.792',
        'https://www.facebook.com/ema.selfiana.9',
        'https://www.facebook.com/Junaa09',
        'https://www.facebook.com/ilman.hendrawan.webdev',
        'https://www.facebook.com/ronal.arteri',
        'https://www.facebook.com/ZullReall1',
        ]

for convert in url_list:
    print(Finder(link_profile="%s"%(convert)))
    print("%s %s"%(find,count))

for parser in url_list:
    for resrap in Finder(link_profile="%s"%(parser)).content:
        print(resrap)
