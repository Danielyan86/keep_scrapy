import requests
import re


def scrapy_keep(page_number):
    domain = "https://gotokeep.com"
    response = requests.get("https://gotokeep.com/explore")
    pattern = re.compile(r'''<div data-url="/explore/more?(.*)" ''')
    find_res = pattern.findall(response.text)
    more_page_id = find_res[0]
    last_id_pattern = re.compile(r'''lastId":"(.*?)"}''')
    i = 0
    while i < page_number:  # 设置爬取页面数目，一个页面大概14张左右图片
        more_page_url = "{0}/explore/more?{1}".format(domain, more_page_id)
        response = requests.get(more_page_url)
        content = response.text
        res = last_id_pattern.findall(content)
        more_page_id = res[0]
        download_pic(content)
        i = i + 1


def download_pic(content):
    pattern = re.compile(r"""(http://static1.*?jpg)""")  # 再返回json数据中匹配图片格式URL
    res = pattern.findall(content)
    pattern_file_name = re.compile(r'''\d{4}/\d{2}/\d{2}/\d{2}/(.*)''') # 获取图片hash id
    for item in res:
        print(item)
        res = pattern_file_name.search(item)
        if res:
            file_name = res.groups()[0]
            response = requests.get(item)
            with open("./pictures/{0}".format(file_name), "wb") as f:
                f.write(response.content)
        else:
            raise AssertionError("can't get file name")


if __name__ == '__main__':
    page_number = 2
    scrapy_keep(page_number)
