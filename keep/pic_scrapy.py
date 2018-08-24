import requests
import re


def scrapy_keep():
    domain = "https://gotokeep.com"
    response = requests.get("https://gotokeep.com/explore")
    pattern = re.compile(r'''<div data-url="/explore/more?(.*)" ''')
    find_res = pattern.findall(response.text)
    more_page_id = find_res[0]
    last_id_pattern = re.compile(r'''lastId":"(.*?)"}''')
    i = 0
    while i < 10:  # 设置爬取页面数目，一个页面大概14张左右图片
        more_page_url = "{0}/explore/more?{1}".format(domain, more_page_id)
        response = requests.get(more_page_url)
        content = response.text
        res = last_id_pattern.findall(content)
        more_page_id = res[0]
        download_pic(content, i)
        i = i + 1


def download_pic(content, num):
    pattern = re.compile(r"""(http://static1.*?jpg)""")
    res = pattern.findall(content)
    i = 0
    for item in res:
        print("=" * 40)
        print(item)
        response = requests.get(item)
        with open("./pictures/{0}{1}.jpg".format(num, i), "wb") as f:
            f.write(response.content)
        i = i + 1


if __name__ == '__main__':
    scrapy_keep()
