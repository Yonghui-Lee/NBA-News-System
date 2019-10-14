import time
from urllib.request import urlopen
import re


# if has Chinese, apply decode()

for m in range(2, 101):
    url = "https://voice.hupu.com/nba/%d" %m
    print(url)
    html = urlopen(url).read().decode("utf8", "ignore")
    print("open")
    f = open('hu.txt', 'a')
    res = re.findall(r'<a href="https://voice.hupu.com/nba/(\d*?).html"', html)
    for r in res:
        f.write(r + '\n')
    print(m)
    time.sleep(0.2)




