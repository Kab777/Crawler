import re
import urllib
from time import sleep
from urllib.request import Request, urlopen

def open_url(url, re_pattern):
    address = Request(url)
    address.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64)')
    html_file = urlopen(url).read().decode('utf-8')
    pattern = re.compile(re_pattern)
    items = re.findall(pattern, html_file)
    return items

web_page = 'http://date.jobbole.com/page/'
pattern_1= '<div class="media-body">\s*?<.+>\s*<a target="_blank" href="(.+)">(.+)</a><label'
pattern_2= '<div class="p-entry">[\S\s]+?????:(.+?)<[\S\s]+???:(.+?)<[\S\s]+???.+?:(.+?)<[\S\s]+???:(.+?)<[\S\s]+?src="(.+?)"'
my_urls=[]
for x in range(4,7):
    items=open_url(web_page+str(x), pattern_1)
    for item in items:
        my_urls.append(item[0])
    print(items)
for my_url in my_urls:
    sleep(10)
    print("processing webpage:" + my_url)
    new_items=open_url(my_url, pattern_2)
    #print("get image:" +new_items[0]+"\n")
    for new_item in new_items:
        filename = "C:/Users/Junyu/Desktop/engl119/photo/" + new_item[0]+" "+new_item[1]+" "+new_item[2]+" "+new_item[3]+"."+new_item[4].split('.')[-1]
        print("filename:   " +filename)
        try:
            urllib.request.urlopen(new_item[4])
            urllib.request.urlretrieve(new_item[4], filename)
            sleep(10)
        except OSError:
            print("??????????\n")