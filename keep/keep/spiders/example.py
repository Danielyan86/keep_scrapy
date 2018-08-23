# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re
import requests


class KeepSpider(scrapy.Spider):
    name = 'keep'
    allowed_domains = ['gotokeep.com']
    start_urls = ['https://gotokeep.com/explore']
    pattern = re.compile(r'"(http.*jpg.*)" class|(http.*jpg.*)\)"')

    def parse(self, response):
        # print(response.body)
        print("=" * 100)
        text_list = (response.xpath("//div[@class='img']").extract())
        # print(text_list)
        # response.body is a result of render.html call; it contains HTML processed by a browser.
        i = 0
        for item in text_list:
            try:
                res = self.pattern.search(item)
                if res:
                    for pic_url in res.groups():
                        if pic_url:
                            response = requests.get(pic_url)
                    with open("./pictures/{0}.jpg".format(i), "wb") as f:
                        f.write(response.content)
            except Exception as e:
                print(e)
                print(item)
            i = i + 1

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 3}, )

    # def parse_result(self, response):
    #     # magic responses are turned ON by default,
    #     # so the result under 'html' key is available as response.body
    #     html = response.body
    #
    #     # you can also query the html result as usual
    #     title = response.css('title').extract_first()
    #
    #     # full decoded JSON data is available as response.data:
    #     png_bytes = base64.b64decode(response.data['png'])


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # parse 方法每次接收到一个在start_requests里面请求的URL的response
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-{0}.html'.format(page)
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
