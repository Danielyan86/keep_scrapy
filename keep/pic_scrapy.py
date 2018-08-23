import requests
import re


def download_pic(content, num):
    pattern = re.compile(r"""(http://static1.*?jpg)""")
    res = pattern.findall(content)
    i = 0
    for item in res:
        print("="*40)
        print(item)
        response = requests.get(item)
        with open("./pictures/{0}{1}.jpg".format(num, i), "wb") as f:
            f.write(response.content)
        i = i + 1


if __name__ == '__main__':
    domain = "https://gotokeep.com"
    response = requests.get("https://gotokeep.com/explore")
    # print(response.content)
    pattern = re.compile(r'''<div data-url="/explore/more?(.*)" ''')
    find_res = pattern.findall(response.text)
    more_page_id = find_res[0]
    # find_res = pattern.search(response.text)
    print(find_res)
    last_id_pattern = re.compile(r'''lastId":"(.*?)"}''')
    i = 0
    while i < 20:
        more_page_url = "{0}/explore/more?{1}".format(domain, more_page_id)
        response = requests.get(more_page_url)
        content = response.text
        res = last_id_pattern.findall(content)
        more_page_id = res[0]
        download_pic(content, i)
        i = i + 1
