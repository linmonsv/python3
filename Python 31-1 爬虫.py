#encoding:UTF-8
import urllib.request
import re

main_page = "http://www.bxwx.org/b/3/3116/"

pages = re.findall(re.compile(r'><a href="(\d{6}.html)">(第.+?章 .+?)</a></dd>'),urllib.request.urlopen(main_page).read().decode('gbk'))
for onepage in pages:
    print(onepage)
    urllib.request.urlretrieve(main_page + onepage[0], "D://tmp//" + onepage[1].replace("?", "") + ".html")
